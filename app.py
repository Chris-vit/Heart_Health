from flask import Flask, request, render_template 

app = Flask(__name__) 

@app.route('/', methods=['GET']) 
def index(): 
	return render_template('index.html') 

@app.route('/read-form', methods=['POST']) 
def read_form(): 

	data = request.form 

	return { 
		'age'	 : data['age'], 
		'weight' : data['weight'], 
		'bp' : data['bp'],  
	} 

if __name__ == '__main__': 
	app.run()
