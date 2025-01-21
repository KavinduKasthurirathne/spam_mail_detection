from flask import Flask, request, render_template
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and vectorizer
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

def classify_email(email_content):
    """Classify an email as Spam or Ham."""
    email_features = vectorizer.transform([email_content])
    prediction = model.predict(email_features)
    return "Ham" if prediction[0] == 1 else "Spam"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email_content = request.form['email_content']
        result = classify_email(email_content)
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)

if __name__ == "__main__":
    app.run(debug=True)