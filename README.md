# Chatty 🤖

## Overview
This repository contains a simple Natural Language Processing (NLP) chatbot implemented in Python using Flask, NLTK, and scikit-learn. The chatbot is trained to understand user intents and generate appropriate responses.

## Features
- **Preprocessing**: User messages and intents are preprocessed to ensure consistency and better understanding.
- **Multinomial Naive Bayes Classifier**: A classifier is trained using the Multinomial Naive Bayes algorithm to predict user intents based on their messages.
- **Web Interface**: The chatbot is integrated into a web interface using Flask, allowing users to interact with it through a simple web application.

## Requirements
- Python 3.x
- Flask
- NLTK
- scikit-learn

## Installation
1. Install the required dependencies:
    ```bash
    pip install flask nltk scikit-learn
    ```

2. Download NLTK data:
    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    ```

## Usage
1. Run the `app.py` file:
    ```bash
    python app.py
    ```
2. Open a web browser and navigate to `http://localhost:5000` to interact with the chatbot.

## Training Data
The chatbot is trained using a dataset stored in `intents.json`. Customize this file to add more intents and patterns for a richer user experience.

## How It Works
1. **Preprocessing**: User messages are preprocessed to tokenize, stem, and remove stopwords, ensuring consistent input for the classifier.
2. **Training**: The Multinomial Naive Bayes classifier is trained on the preprocessed data from `intents.json`.
3. **Response Generation**: User messages are preprocessed and passed through the trained classifier to predict the intent. A random response associated with the predicted intent is then provided.

## Web Interface
- The home route (`/`) renders the `index.html` template.
- The `/get_response` route handles user messages via POST requests and returns a JSON response containing the chatbot's reply.

Feel free to explore and enhance this chatbot by customizing the training data and improving the response generation logic. Enjoy chatting!
