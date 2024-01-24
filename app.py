# app.py

import nltk
nltk.download('stopwords')
nltk.download('punkt')

from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import json
import random




app = Flask(__name__)

#app.py

# Step 3: Preprocess user messages and intents
def preprocess_text(text):
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))

    words = nltk.word_tokenize(text.lower())
    words = [ps.stem(word) for word in words if word.isalnum() and word not in stop_words]

    return ' '.join(words)



# Step 4: Train a classifier
with open('intents.json') as file:
    data = json.load(file)

intents = data['intents']
X = []  # Features
y = []  # Labels

for intent in intents:
    for pattern in intent['patterns']:
        X.append(preprocess_text(pattern))
        y.append(intent['tag'])

vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

classifier = MultinomialNB()
classifier.fit(X_vectorized, y)

# Step 5: Define a function to generate a response
def generate_response(user_message):
    user_message = preprocess_text(user_message)
    user_vectorized = vectorizer.transform([user_message])
    intent = classifier.predict(user_vectorized)[0]

    for intent_data in intents:
        if intent_data['tag'] == intent:
            return random.choice(intent_data['responses'])

# Step 6: Create a web interface with Flask
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    response = generate_response(user_message)
    return {'response': response}

if __name__ == '__main__':
    app.run(debug=True)
