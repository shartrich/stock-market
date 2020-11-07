import os
from dotenv import load_dotenv

load_dotenv()


PROJECT_DIRECTORY = os.path.dirname(os.path.abspath(__file__)) + '/../..'

OUTPUT_PATH = '%s/%s' % (PROJECT_DIRECTORY, 'output')
INPUT_PATH = '%s/%s' % (PROJECT_DIRECTORY, 'input')


SSH_HOST = os.getenv('SSH_HOST')
SSH_USER = os.getenv('SSH_USER')
SSH_PORT = int(os.getenv('SSH_PORT'))
SSH_PASS = os.getenv('SSH_PASS')
SQL_IP = os.getenv('SQL_IP')
SQL_HOSTNAME = os.getenv('SQL_HOSTNAME')
SQL_PORT = int(os.getenv('SQL_PORT'))

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DATABASE = os.getenv('DB_DATABASE')
DB_HOST = os.getenv('DB_HOST')

STOCKS_TABLE = os.getenv('DB_TABLE')