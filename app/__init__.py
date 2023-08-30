from flask import Flask;
from flask_sqlalchemy import SQLAlchemy;

app = Flask(__name__);

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/sqlalchemy';
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;

db = SQLAlchemy(app);

from app.schemas import *;
from app.routes import *;