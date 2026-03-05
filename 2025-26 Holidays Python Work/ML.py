# Example training data (sentences and labels)
import datetime
import pyttsx3
import random

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

training_sentences = [
    "hi", "hello", "hey there",
    "how are you", "what's up",
    "tell me a joke", "make me laugh",
    "what's the time", "tell me the time"
]

training_labels = [
    "greeting", "greeting", "greeting",
    "feeling", "feeling",
    "joke", "joke",
    "time", "time"
]
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(training_sentences)
model = MultinomialNB()
model.fit(X, training_labels)

while True:
    user = input("You: ")
    if "bye" in user:
        speak("Goodbye!")
        break
    if user.strip() == "":
        continue

    # clean the speech text
    user = user.lower().strip().replace("!", "").replace(".", "").replace("?", "")
    X_test = vectorizer.transform([user])
    intent = model.predict(X_test)[0]

    if intent == "greeting":
        speak(random.choice["Hey there! How are you?", "Wassup Man!", "Hey! How can I help you?"])
    elif intent == "feeling":
        speak(random.choice["I'm doing great, thanks for asking!", "How are you?"])
    elif intent == "joke":
        speak("Why was 6 afraid of 7? Because 7 8 9!")
    elif intent == "time":
        from datetime import datetime
        speak(f"It's {datetime.now().strftime('%I:%M %p')}")
    else:
        speak("Hmm, I don't understand that yet. Could you please repeat?")
