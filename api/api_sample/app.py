from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import *

app = Flask(__name__)

