# import all the libraries
from flask import Flask, render_template, request
import joblib

# Loading saved model
model = joblib.load('model.joblib')

# initilizing the flask app
app = Flask(__name__)

#Create all the routes
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    sepal_length = float(request.form.get("sl"))
    sepal_width = float(request.form.get("sw"))
    petal_length = float(request.form.get("pl"))
    petal_width = float(request.form.get("pw"))
    
    # pridict from Loaded Model
    pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    
    return render_template("predict.html", pred=pred[0])


#call the main driver function
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)