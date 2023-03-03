from project.app.api import content_router


@content_router.get("/detect")
def get_content_tree(client_data: str):
    if client_data == "fraudulent":
        return {"message": "Fraudulent client"}
    else:
        return {"message": "Not fraudulent client"}
