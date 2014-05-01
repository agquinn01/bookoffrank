from flask.ext.mongoengine import MongoEngine

db = MongoEngine(app)

# connect('project1')

class Page(Document):
	savedpage = StringField() 

mypage = Page(savedpage='1')