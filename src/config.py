import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    app_name: str = "EMAIL EVENT CATCHER"
    db_host: str = os.getenv("DB_HOST")
    db_username: str = os.getenv("DB_USERNAME")
    db_name: str = os.getenv("DB_NAME")
    db_password: str = os.getenv("DB_PASSWORD")
    db_url: str = (
        "postgresql://"
        + db_username
        + ":"
        + db_password
        + "@"
        + db_host
        + "/"
        + db_name
    )


settings = Settings()
