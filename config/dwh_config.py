import os
from dotenv import load_dotenv

load_dotenv()

DRIVER = os.getenv("DRIVER")
SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")
UID = os.getenv("UID")
PASSWORD = os.getenv("PASSWORD")

A_QUERY1 = os.getenv("A_QUERY1")
A_QUERY2 = os.getenv("A_QUERY2")

B_QUERY1 = os.getenv("B_QUERY1")
B_QUERY2 = os.getenv("B_QUERY2")

C_QUERY1 = os.getenv("C_QUERY1")
C_QUERY2 = os.getenv("C_QUERY2")
