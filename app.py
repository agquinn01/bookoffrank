import os, datetime
from flask import Flask, request # Retrieve Flask, our framework
from flask import render_template
import operator

app = Flask(__name__)   # create our flask app



dossierItems = {}

dossierItems['00'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'00', 'title':'?', 'route':'/itemblank', 'chapter':'1'}
dossierItems['01'] = {'image':'static/img/dossier/Dossier01.jpg', 'index':'01','title':'STEVEN', 'route':'/item1', 'chapter':'1'}
dossierItems['02'] = {'image':'static/img/dossier/Dossier012.jpg', 'index':'02','title':'FRANK', 'route':'/item2', 'chapter':'1'}
dossierItems['03'] = {'image':'static/img/dossier/Dossier013.jpg', 'index':'03','title':'TOKI', 'route':'/item3', 'chapter':'1'}
dossierItems['04'] = {'image':'static/img/dossier/Dossier014.jpg', 'index':'04','title':'PILOT DETAIL', 'route':'/item4', 'chapter':'1'}
dossierItems['05'] = {'image':'static/img/dossier/Dossier015.jpg', 'index':'05','title':'PILOT HISTORY', 'route':'/item5', 'chapter':'2'}
dossierItems['06'] = {'image':'static/img/dossier/Dossier016.jpg', 'index':'06','title':'FOX', 'route':'/item6', 'chapter':'2'}
dossierItems['07'] = {'image':'static/img/dossier/Dossier017.jpg', 'index':'07','title':'SNAKE AND MOLE', 'route':'/item7', 'chapter':'2'}
dossierItems['08'] = {'image':'static/img/dossier/Dossier018.jpg', 'index':'08','title':'BEE AND OWL', 'route':'/item8', 'chapter':'2'}
dossierItems['09'] = {'image':'static/img/dossier/Dossier019.jpg', 'index':'09','title':'SALLY', 'route':'/item9', 'chapter':'2'}
dossierItems['10'] = {'image':'static/img/dossier/Dossier0110.jpg', 'index':'10','title':'CALICO', 'route':'/item10', 'chapter':'2'}
dossierItems['11'] = {'image':'static/img/dossier/MedCityCalico.png', "index":"11",'title':'CALICO WEB 1', 'route':'/item11', 'chapter':'2'}




foundItems = {}

foundItems['01'] = {"value":False,"index":"01", 'chapter':'1'}
foundItems['02'] = {"value":False,"index":"02", 'chapter':'1'}
foundItems['03'] = {"value":True,"index":"03", 'chapter':'1'}
foundItems['04'] = {"value":False,"index":"04", 'chapter':'1'}
foundItems['05'] = {"value":False,"index":"05", 'chapter':'2'}
foundItems['06'] = {"value":True,"index":"06", 'chapter':'2'}
foundItems['07'] = {"value":False,"index":"07", 'chapter':'2'}
foundItems['08'] = {"value":True,"index":"08", 'chapter':'2'}
foundItems['09'] = {"value":False,"index":"09", 'chapter':'2'}
foundItems['10'] = {"value":False,"index":"10", 'chapter':'2'}
foundItems['11'] = {"value":True,"index":"11", 'chapter':'2'}

#This is a model for how a route should work
# @app.route("/item1")
# def item1():
# 	foundItems['1'] = True
	
# 	templateData = {
# 		'currentItem' : dosseirItems['1']
# 	}
# 	# render the template, pass in the animals dictionary refer to it as 'animals'
# 	return render_template("item.html", **templateData)	
# #

@app.route("/bof1")
def text():

	currentPage = request.args.get('q','2')
	nextPage = str(int(currentPage)+1)
	if currentPage == "1":
		prevPage = "1"
	else:
		prevPage = str(int(currentPage)-1)



	templateData = {
	'title' : 'The Book of Frank',
	'page' : "1",
	'currentPage': currentPage,
	'nextPage' : nextPage,
	'prevPage' : prevPage
	}
	return render_template("bof1_test.html", **templateData)

@app.route("/itemblank")
def itemblank():
	templateData = {
	'title' : dossierItems['00']['title'],
	'image' : dossierItems['00']['image']
	}
	return render_template("item.html", **templateData)

@app.route("/item1")
def item1():
	foundItems['01']['value'] = True
	templateData = {
	'title' : dossierItems['01']['title'],
	'image' : dossierItems['01']['image']
	}
	return render_template("item.html", **templateData)

@app.route("/item2")
def item2():
	foundItems['02']['value'] = True
	dossierItems['01'] = {'image':'static/img/dossier/Dossier01.jpg', 'index':'01','title':'STEVEN', 'route':'/item1', 'chapter':'1'}
	templateData = {
	'title' : dossierItems['02']['title'],
	'image' : dossierItems['02']['image']
	}
	return render_template("item.html", **templateData)

@app.route("/item3")
def item3():
	foundItems['03']['value'] = True
	templateData = {
	'title' : dossierItems['03']['title'],
	'image' : dossierItems['03']['image']
	}
	return render_template("item.html", **templateData)

@app.route("/item4")
def item4():
	foundItems['04']['value'] = True
	templateData = {
	'title' : dossierItems['04']['title'],
	'image' : dossierItems['04']['image']
	}
	return render_template("item.html", **templateData)

@app.route("/item5")
def item5():
	foundItems['05']['value'] = True
	templateData = {
	'title' : dossierItems['05']['title'],
	'image' : dossierItems['05']['image']
	}
	return render_template("item.html", **templateData)

@app.route("/item6")
def item6():
	foundItems['06']['value'] = True
	templateData = {
	'title' : dossierItems['06']['title'],
	'image' : dossierItems['06']['image']
	}
	return render_template("item.html", **templateData)

@app.route("/item7")
def item7():
	foundItems['07']['value'] = True
	templateData = {
	'title' : dossierItems['07']['title'],
	'image' : dossierItems['07']['image']
	}
	return render_template("item.html", **templateData)

@app.route("/item8")
def item8():
	foundItems['08']['value'] = True
	templateData = {
	'title' : dossierItems['08']['title'],
	'image' : dossierItems['08']['image']
	}
	return render_template("item.html", **templateData)

@app.route("/item9")
def item9():
	foundItems['09']['value'] = True
	templateData = {
	'title' : dossierItems['09']['title'],
	'image' : dossierItems['09']['image']
	}
	return render_template("item.html", **templateData)

@app.route("/item10")
def item10():
	foundItems['10']['value'] = True
	dossierItems['10'] = {'image':'static/img/dossier/Dossier0110.jpg', 'index':'10','title':'CALICO', 'route':'/item10', 'chapter':'2'}
	templateData = {
	'title' : dossierItems['10']['title'],
	'image' : dossierItems['10']['image']
	}
	return render_template("item.html", **templateData)

@app.route("/item11")
def item11():
	foundItems['11']['value'] = True
	templateData = {
	'title' : dossierItems['11']['title'],
	'image' : dossierItems['11']['image']
	}
	return render_template("item.html", **templateData)

@app.route("/dc1")
def dc1():
	currentItems = []
	chapter1Items = []

	for k,v in foundItems.iteritems():
		if foundItems[k]['value'] and foundItems[k]['chapter'] == '1':
			chapter1Items.append(dossierItems[foundItems[k]['index']])

		elif foundItems[k]['value'] == False and foundItems[k]['chapter'] == '1':
			dossierItems[foundItems[k]['index']]['title'] = '?'
			dossierItems[foundItems[k]['index']]['image'] = 'static/img/dossier/Dossier_blank.jpg'
			dossierItems[foundItems[k]['index']]['route'] = '/itemblank'
			chapter1Items.append(dossierItems[foundItems[k]['index']])

		else:
			pass

	chapter1Items.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : 'These are the items found in Chapter 1',
	'chapter1Items' : chapter1Items,
	}

	return render_template("dc1.html", **templateData)	

@app.route("/dc2")
def dc2():
	currentItems = []
	chapter2Items = []
	chapter2Sorted = []

	for k,v in foundItems.iteritems():
		if foundItems[k]['value'] and foundItems[k]['chapter'] == '2':
			chapter2Items.append(dossierItems[foundItems[k]['index']])

		elif foundItems[k]['value'] == False and foundItems[k]['chapter'] == '2':
			dossierItems[foundItems[k]['index']]['title'] = '?'
			dossierItems[foundItems[k]['index']]['image'] = 'static/img/dossier/Dossier_blank.jpg'
			dossierItems[foundItems[k]['index']]['route'] = '/itemblank'
			chapter2Items.append(dossierItems[foundItems[k]['index']])

		else:
			pass

	chapter2Items.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : 'These are the items found in Chapter 2',
	'chapter2Items' : chapter2Items,
	'chapter2Sorted' : chapter2Sorted
	}

	return render_template("dc2.html", **templateData)	

@app.route("/list")
def list():
	# currentItems = []
	# chapter1Items = []
	# chapter2Items = []
	# chapter3Items = []
	# chapter4Items = []
	# chapter5Items = []
	# for k,v in foundItems.iteritems():
	# 	if foundItems[k]['value'] and foundItems[k]['chapter'] == '1':
	# 		chapter1Items.append(dossierItems[foundItems[k]['index']])

	# 	elif foundItems[k]['value'] == False and foundItems[k]['chapter'] == '1':
	# 		chapter1Items.append(dossierItems['0'])
		
	# 	elif foundItems[k]['value'] and foundItems[k]['chapter'] == '2':
	# 		chapter2Items.append(dossierItems[foundItems[k]['index']])

	# 	elif foundItems[k]['value'] == False and foundItems[k]['chapter'] == '2':
	# 		chapter2Items.append(dossierItems['0'])

	# 	else:
	# 		pass
	# 	# print foundItems

	templateData = {
	'title' : 'This is the list page'
	# 'chapter1Items' : chapter1Items,
	# 'chapter2Items' : chapter2Items
	}
	return render_template("dossier.html", **templateData)	


@app.route("/home")
def home():
	return render_template("home.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)



	