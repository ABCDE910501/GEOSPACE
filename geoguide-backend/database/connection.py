import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432")
}

def get_db_connection():
    """Create and return a database connection."""
    return psycopg2.connect(**DB_CONFIG)
