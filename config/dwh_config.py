import os
from dotenv import load_dotenv

load_dotenv()

DRIVER = os.getenv("DRIVER")
SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")
UID = os.getenv("UID")
PASSWORD = os.getenv("PASSWORD")

A1_QUERY1 = os.getenv("A1_QUERY1")
A1_QUERY2 = os.getenv("A1_QUERY2")
A2_QUERY1 = os.getenv("A2_QUERY1")
A2_QUERY2 = os.getenv("A2_QUERY2")
A3_QUERY1 = os.getenv("A2_QUERY1")
A3_QUERY2 = os.getenv("A2_QUERY2")

B1_QUERY1 = os.getenv("B1_QUERY1")
B2_QUERY1 = os.getenv("B2_QUERY1")

C1_QUERY1 = os.getenv("C1_QUERY1")

D1_QUERY1 = os.getenv("D1_QUERY1")
