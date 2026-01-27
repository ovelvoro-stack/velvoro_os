import os

APP_NAME = "Velvoro Daily OS"
ENV = os.getenv("ENV", "development")

DATABASE_PATH = os.getenv("DATABASE_PATH", "velvoro.db")
