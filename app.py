from flask import Flask, render_template, request
 
app = Flask(__name__)      
 
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
	meal_cost = request.form['meal_cost']
	tip_percentage = request.form['tip_percentage']
	tip = float(meal_cost) * float(tip_percentage) / 100
	tip = "{0:.2f}".format(tip)
	return render_template('results.html', 
		meal_cost = meal_cost, tip_percentage = tip_percentage, tip= tip)
 
if __name__ == '__main__':
  	app.run(debug=True)