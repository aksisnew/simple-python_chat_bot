from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# We will ad some training data over here
training_Sentences = [
    "hello", "hi", "hey",
    "bye", "thank you", "appreciate it",
    "what is your name", "who are you"
]
training_labels = [
       "greeting", "greeting", "greeting",
    "farewell", "farewell", "farewell",
    "thanks", "thanks", "thanks",
    "identity", "identity"
]

vectorizer = TfidfVectorizer(tokenizer=preprocess)
X = vectorizer.fit_transform(training_sentences)
clf = LogisticRegression()
clf.fit(X, training_labels)
