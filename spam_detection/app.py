from flask import Flask, render_template, request,url_for
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)
  

with open("model.pkl", "rb") as file:
    model = pickle.load(file)
    
with open("vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)    



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["GET","POST"])
def predict():
    prediction = None
    user_text = request.form.get("user_text")

    if user_text:
       
        text_vectorized = vectorizer.transform([user_text]).toarray()

        
        prediction = model.predict(text_vectorized)[0]

        
        result = "Spam" if prediction == 1 else "Not Spam"
    else:
        result = "No input provided."

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
