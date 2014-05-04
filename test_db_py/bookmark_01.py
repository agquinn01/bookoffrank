from flask.ext.mongoengine import MongoEngine
import re 
from flask import Flask, request, render_template, redirect, abort, flash, json

from unidecode import unidecode

app = Flask(__name__)
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY']

db = MongoEngine(app)

# connect('project1')

class Page(Document):
	savedpage = StringField() 

mypage = Page(savedpage='1')