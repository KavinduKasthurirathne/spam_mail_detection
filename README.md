# Email Spam/Ham Classifier

This is a simple email classification application that uses a trained machine learning model to classify emails as either **Spam** or **Ham**. The model is based on **Logistic Regression** and uses **TF-IDF Vectorization** for text feature extraction.

You can use this application via a web interface built with **Streamlit** or **Flask** to classify your email content.

## Features
- Classifies email content as either **Spam** or **Ham** (non-spam).
- Uses **Logistic Regression** for classification.
- **TF-IDF Vectorizer** is used to preprocess and vectorize email content.
- Easily deployable using **Streamlit** or **Flask**.

## Requirements
- Python 3.x
- Required Python libraries:
  - `pickle`
  - `sklearn`
  - `streamlit` (for Streamlit version)
  - `flask` (for Flask version)

## Installation

### 1. Clone the Repository
First, clone the repository to your local machine.

```bash
git clone https://github.com/KavinduKasthurirathne/spam_mail_detection.git
```

### 2. Install Dependancies
Install the required dependencies.

```bash
pip install pickle sklearn streamlit flask
```

### 3. Run the Application
Run the streamlit application. Open the terminal and run the following command.

```bash
streamlit run app.py
```
Run the flask application. Open the terminal and run the following command.

```bash
python app.py
```
