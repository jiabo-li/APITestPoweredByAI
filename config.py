import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    DEEPSEEK_API_BASE = os.getenv("DEEPSEEK_API_BASE")
    DEEPSEEK_MODEL = "deepseek-chat"

    BASE_URL = os.getenv("BASE_URL")


    TIMEOUT = 30
    OUTPUT_DIR = "generated_tests"
    REPORT_DIR = "test_reports"