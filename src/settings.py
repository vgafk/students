import os
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.environ.get('PORT', 8000))
HOST = str(os.environ.get('GRAPH_HOST', 'localhost'))
# DB_USER = os.environ['POSTGRES_USER']
# DB_PASSWORD = os.environ['POSTGRES_PASSWORD']
# DB_SERVER = os.environ['POSTGRES_HOST']
# DB_PORT = int(os.environ['POSTGRES_PORT'])
# DB_NAME = os.environ['POSTGRES_DB_NAME']