
import os

from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

# 0. Load and source credentials
load_dotenv()

SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DB = os.getenv("SQL_DB")
SQL_ID = os.getenv("SQL_ID")
SQL_PW = os.getenv("SQL_PW")


# 1. Connect to Azure Database
connection_string = (
    f"mssql+pyodbc://{SQL_ID}:{SQL_PW}@{SQL_SERVER}/{SQL_DB}"
    "?driver=ODBC+Driver+18+for+SQL+Server"
)

# 2. Create the SQLAlchemy engine
engine = create_engine(connection_string)

print(f"{connection_string}")
print(engine.__class__.__name__)

# 3. Query Data
query = "SELECT COUNT(*) FROM Production.Location"

with engine.connect() as connection:
    pandas_df = pd.read_sql(query, connection)
    
print(pandas_df)