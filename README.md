# Spam Detection Web Application

## 📌 Description
A simple Machine Learning-based web application that detects whether an email is Spam or Not Spam using a trained model.

The model is trained on a spam dataset and deployed using a Flask web interface.

---

## 🚀 Tech Stack
- Python
- Flask
- Scikit-learn
- HTML/CSS
- Pickle (Model Serialization)

---

## 📁 Project Structure

spam_detection/
│
├── static/css/ # CSS styling files
├── templates/ # HTML templates
├── app.py # Flask application
├── email_spam.ipynb # Model training notebook
├── model.pkl # Trained ML model
├── vectorizer.pkl # Text vectorizer
├── spam_dataset.csv # Dataset used for training



---

## 📊 How It Works

1. User enters a Email.
2. Text is transformed using the saved vectorizer.
3. The trained model predicts:
   - Spam
   - Not Spam
4. Result is displayed on the web page.


---

## ⚙️ Installation

1. Clone the repository
2. Install required packages:
   pip install flask scikit-learn pandas numpy
3. Run the Application
   python app.py
   


## Author
Sanjaykanth M
