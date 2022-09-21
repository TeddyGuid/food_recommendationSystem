import numpy as np
from flask import Flask,request,jsonify,render_template
from surprise.dump import load
app=Flask(__name__)
modele=load("foodRecommender.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    features=[x for x in request.form.values()]
    prediction=modele[1].predict(features[0],features[1])
    estimation_2decimale=np.round(prediction.est,1)
    prediction_text='la valeur du rating est de {}'.format(estimation_2decimale)
    return render_template('index.html',prediction_text=prediction_text)

if __name__ =="__main__":
    app.run(debug=True)