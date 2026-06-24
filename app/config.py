from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "gemma3:4b")

VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "vector_store")

print("MODEL_NAME =", MODEL_NAME)