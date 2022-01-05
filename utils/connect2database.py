from config.dwh_config import *

import pyodbc


def connect_to_database():

    conn = pyodbc.connect(
        "DRIVER=%s;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s"
        % (DRIVER, SERVER, DATABASE, UID, PASSWORD)
    )

    conn.autocommit = True

    print("Success! Connected to the database.")

    return conn
