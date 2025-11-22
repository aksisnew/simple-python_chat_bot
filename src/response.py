responses = {
    "greeting": "Hello! How can I help you today?",
    "farewell": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "identity": "I’m your friendly Python NLP bot."
}

def get_response(user_input):
    X_test = vectorizer.transform([user_input])
    intent = clf.predict(X_test)[0]
    return response.get(intent, "Sorry, I didn’t understand that.")
    