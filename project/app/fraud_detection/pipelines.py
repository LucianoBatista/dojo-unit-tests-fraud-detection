import pickle

import numpy as np
import pandas as pd
from feature_engine.encoding import OneHotEncoder
from pandas import DataFrame, Series
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split


class PreProcessingPipe:
    def __init__(self, dataset: DataFrame, X_test: DataFrame = None) -> None:
        self.dataset = dataset
        self.X_train = None
        self.X_test = X_test
        self.y_train = None
        self.y_test = None

    def validate_columns(self) -> bool:
        columns = self.dataset.columns
        if list(columns) != [
            "step",
            "type",
            "amount",
            "nameOrig",
            "oldbalanceOrg",
            "newbalanceOrig",
            "nameDest",
            "oldbalanceDest",
            "newbalanceDest",
            "isFraud",
            "isFlaggedFraud",
        ]:
            return False
        else:
            return True

    def drop_columns(self, columns: list) -> None:
        self.dataset.drop(columns, axis=1, inplace=True)

    def filter_type_classes(self, classes: list):
        self.dataset = self.dataset[~self.dataset["type"].isin(classes)]

    def train_test_splitting(self, sample_test_size: float, to_drop: list):
        X_dataset = self.dataset.drop(to_drop, axis=1)
        y_target = self.dataset[to_drop]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X_dataset,
            y_target,
            test_size=sample_test_size,
            random_state=10,
            stratify=y_target,
        )

    def label_encoding(self):
        le = preprocessing.LabelEncoder()
        le.fit(self.X_train["type"])

        # looking at the classes
        print(list(le.classes_))

        self.X_train["type"] = le.transform(self.X_train["type"])
        self.X_test["type"] = le.transform(self.X_test["type"])

    def one_hot_encoder(
        self, cat_variables: list, is_x_test: bool, model_name: str = None
    ):
        if not is_x_test:
            ohe = OneHotEncoder(variables=cat_variables)

            ohe.fit(self.X_train)
            self.X_train = ohe.transform(self.X_train)
            self.X_test = ohe.transform(self.X_test)

            with open(f"project/app/resources/encoder_{model_name}", "wb") as f:
                pickle.dump(ohe, f)
        else:
            with open("project/app/resources/ohe", "rb") as f:
                ohe = pickle.load(f)

            self.X_test = ohe.transform(self.X_test)

    def scaling(self):
        scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))

        scaler.fit(self.X_train)
        X_train_np = scaler.transform(self.X_train)
        x_test_np = scaler.transform(self.X_test)

        self.X_train = pd.DataFrame(X_train_np, columns=self.X_train.columns)
        self.X_test = pd.DataFrame(x_test_np, columns=self.X_test.columns)


class Training:
    def __init__(
        self,
        X_train: DataFrame,
        X_test: DataFrame,
        y_train: Series,
        y_test: Series,
    ) -> None:
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.lrc = None
        self.y_pred_train = None
        self.y_pred_test = None

    def fit_logistic_regression(self):
        # logistic regression classifier, default threshold is 0.5
        self.lrc = LogisticRegression()

        # fitting on training data
        _ = self.lrc.fit(self.X_train, self.y_train)

    def predict_logistic_regression(self):
        self.y_pred_train = self.lrc.predict(self.X_train)
        self.y_pred_test = self.lrc.predict(self.X_test)

    def fit_random_forest(self):
        # chute
        self.rfc = RandomForestClassifier(n_jobs=-1)
        self.rfc.fit(self.X_train, self.y_train["is_fraud"])

    def predict_random_forest(self):
        predict_proba_train = self.rfc.predict_proba(self.X_train)
        predict_proba_test = self.rfc.predict_proba(self.X_test)
        self.y_pred_train = (predict_proba_train[:, 1] >= 0.5).astype("int")
        self.y_pred_test = (predict_proba_test[:, 1] >= 0.5).astype("int")

    def calculate_metrics(self):
        # train
        accuracy_training = accuracy_score(self.y_train, self.y_pred_train)
        precision_training = precision_score(self.y_train, self.y_pred_train)
        recall_training = recall_score(self.y_train, self.y_pred_train)
        auc_training = roc_auc_score(self.y_train, self.y_pred_train)
        f1_training = f1_score(self.y_train, self.y_pred_train)

        # test
        accuracy_testing = accuracy_score(self.y_test, self.y_pred_test)
        precision_testing = precision_score(self.y_test, self.y_pred_test)
        recall_testing = recall_score(self.y_test, self.y_pred_test)
        auc_testing = roc_auc_score(self.y_test, self.y_pred_test)
        f1_testing = f1_score(self.y_test, self.y_pred_test)

        metrics_training = {
            "training": {
                "accuracy": accuracy_training,
                "recall": recall_training,
                "precision": precision_training,
                "auc": auc_training,
                "f1": f1_training,
            },
            "testing": {
                "accuracy": accuracy_testing,
                "recall": recall_testing,
                "precision": precision_testing,
                "auc": auc_testing,
                "f1": f1_testing,
            },
        }

        return metrics_training


def prediction(pickle_model, payload: dict):
    with open(pickle_model, "rb") as f:
        lr = pickle.load(f)

    print(lr)
    payload_df = pd.DataFrame(payload, index=[1])
    payload_array = np.array(payload_df)
    print(payload_array)
    y_pred = lr.predict(payload_array)
    return y_pred
