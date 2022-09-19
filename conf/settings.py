import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

URL_LIBERAL_ULTIMAS_NOTICIAS = os.environ.get("URL_LIBERAL_ULTIMAS_NOTICIAS")
URL_LIBERAL_BASE = os.environ.get("URL_LIBERAL_BASE")
