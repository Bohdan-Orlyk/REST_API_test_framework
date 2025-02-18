import os
from dotenv import load_dotenv

load_dotenv()


class EnVariables:
    API_TOKEN = os.getenv('API_TOKEN')
    HOST = os.getenv('HOST')
