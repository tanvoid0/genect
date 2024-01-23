from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
import pandas as pd

# ML Packages
from sklearn.feature_extraction.text import CountVectorizer
import joblib

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html', name='')


@app.route('/predict', methods=['POST'])
def predict():
    df = pd.read_csv("data/gender.csv")
    # Features and Labels
    df_X = df.name
    df_Y = df.sex

    # Vectorization
    corpus = df_X
    cv = CountVectorizer()
    X = cv.fit_transform(corpus)

    # Loading our ML Model
    naivebayes_model = open("models/naivebayesgendermodel.pkl", "rb")
    clf = joblib.load(naivebayes_model)
    my_prediction = None
    namequery = None

    # Receives the input query from form
    if request.method == 'POST':
        namequery = request.form['namequery']
        data = [namequery]
        vect = cv.transform(data).toarray()
        my_prediction = clf.predict(vect)
    return render_template('results.html', prediction=my_prediction, name=namequery.upper())


if __name__ == '__main__':
    app.run(debug=True, port=33507)
