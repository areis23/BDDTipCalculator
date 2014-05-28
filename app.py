from flask import Flask, render_template
 
app = Flask(__name__)      
 
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/results', methods=['POST'])
def results(meal_cost= 10):
	return render_template('results.html', meal_cost = meal_cost)
 
if __name__ == '__main__':
  	app.run(debug=True)