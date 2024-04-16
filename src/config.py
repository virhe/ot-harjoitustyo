import os
from dotenv import load_dotenv


dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, ".env"))
except FileNotFoundError:
    pass

DATABASE_NAME = os.getenv("DATABASE_NAME", "default.db")
DATABASE_PATH = os.path.join(dirname, "..", "data", DATABASE_NAME)
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
