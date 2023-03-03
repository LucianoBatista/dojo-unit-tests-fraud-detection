import os

workers_per_core_str = os.getenv("WORKER_PER_CORE", "1")
use_max_workers = None

host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", "8000")
use_loglevel = os.getenv("LOG_LEVEL", "info")
use_bind = f"{host}:{port}"

# concurrency = multiprocessing.cpu_count()
cores = int(os.getenv("GUNICORN_CONCURRENCY", "5"))
workers_per_core = int(workers_per_core_str)
default_web_concurrency = workers_per_core * cores
accesslog_var = os.getenv("ACCESS_LOG", "-")
use_accesslog = accesslog_var or None
errorlog_var = os.getenv("ERROR_LOG", "-")
use_errorlog = errorlog_var or None
graceful_timeout_str = os.getenv("GRACEFUL_TIMEOUT", "120")
timeout_str = os.getenv("TIMEOUT", "120")
keepalive_str = os.getenv("KEEP_ALIVE", "5")

# Gunicorn config variables
loglevel = use_loglevel
workers = default_web_concurrency
bind = use_bind
errorlog = use_errorlog
worker_tmp_dir = "/dev/shm"
accesslog = use_accesslog
graceful_timeout = int(graceful_timeout_str)
timeout = int(timeout_str)
keepalive = int(keepalive_str)

# For debugging and testing uncomment the following lines
# log_data = {
#     "loglevel": loglevel,
#     "workers": workers,
#     "bind": bind,
#     "graceful_timeout": graceful_timeout,
#     "timeout": timeout,
#     "keepalive": keepalive,
#     "errorlog": errorlog,
#     "accesslog": accesslog,
#     # Additional, non-gunicorn variables
#     "workers_per_core": workers_per_core,
#     "use_max_workers": use_max_workers,
#     "host": host,
#     "port": port,
# }
# print(json.dumps(log_data))
