import os
from dotenv import load_dotenv

def load_env():
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'credentials', '.env')
    load_dotenv(dotenv_path=dotenv_path)
