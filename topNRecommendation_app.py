import numpy as np
from flask import Flask,request,jsonify,render_template
from collections import defaultdict
from surprise.dump import load
app=Flask(__name__)
modele=load("foodRecommender.pkl")

@app.route('/')
def home():
    return render_template('indexTopN.html')

def get_top_n(predictions, n=3):

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

@app.route('/predict',methods=['POST'])
def predict():
    features=[x for x in request.form.values()]
    predictions=[]
    
    for iid in list(features[1].split(',')):
        predictions.append(modele[1].predict(features[0],iid))
    foods=get_top_n(predictions,int(features[2]))
    
    for uid, user_ratings in foods.items():
        continue
    prediction_text='Le top{} des produits recommandables pour l\'utilisateur {} est {}'.format(int(features[2]),features[0],[iid for (iid, _) in user_ratings])
    return render_template('indexTopN.html',prediction_text=prediction_text)



if __name__ =="__main__":
    app.run(debug=True)