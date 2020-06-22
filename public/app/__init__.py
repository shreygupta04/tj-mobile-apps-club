from flask import Flask
from app.secret import SECRET_KEY

app = Flask(__name__,  static_url_path='')
app.config['SECRET_KEY'] = SECRET_KEY

from app import server