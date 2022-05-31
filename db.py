import sys, os
print(os.getcwd())
sys.path.append(os.getcwd())

from orator import DatabaseManager, Schema, Model

from config import settings


DATABASES = {
    "postgres": {
        "driver": settings.database_driver,
        "host": settings.database_hostname,
        "database": settings.database_name,
        "user": settings.database_username,
        "password": settings.database_password,
        "prefix": "",
        "port": settings.database_port
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)