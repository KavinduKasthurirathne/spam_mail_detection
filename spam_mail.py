import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

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

# Streamlit App UI
st.title("Spam Email Classifier")
st.write("Enter an email content to classify it as Spam or Ham.")

# Input field for the email content
email_content = st.text_area("Email Content")

# Classify when button is pressed
if st.button("Classify"):
    if email_content:
        result = classify_email(email_content)
        st.write(f"The email is classified as: {result}")
    else:
        st.write("Please enter some email content.")
