import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

class Settings():
    secret_key = os.getenv("SECRET_KEY")
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    db_name_test = os.getenv("DB_NAME_TEST")
    db_pass_encoded = quote_plus(db_pass)
    conn_string = f"postgresql://{db_user}:{db_pass_encoded}@{db_host}:{db_port}/{db_name}"
    conn_string_test = f"postgresql://{db_user}:{db_pass_encoded}@{db_host}:{db_port}/{db_name_test}"