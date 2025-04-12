from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)
sentiment_analyzer = pipeline("sentiment-analysis")

response_dict = {
    "POSITIVE": [
        "That's wonderful to hear! Keep up the positive vibes 😊.",
        "Glad you're feeling good! Remember to share your smile with others."
    ],
    "NEGATIVE": [
        "I'm sorry you're feeling this way. Take a deep breath. You're not alone 💙.",
        "That sounds tough. Maybe a short walk or some music might help a bit?",
        "It’s okay to have hard days. Don’t hesitate to talk to someone you trust."
    ],
    "NEUTRAL": [
        "Thanks for sharing. Would you like to talk more about it?",
        "I'm here to listen. Tell me more if you'd like."
    ]
}

@app.route('/', methods=["GET", "POST"])
def home():
    user_input = ""
    response = ""
    sentiment = ""

    if request.method == "POST":
        user_input = request.form['message']
        result = sentiment_analyzer(user_input)[0]
        sentiment = result['label']
        response = response_dict.get(sentiment, response_dict["NEUTRAL"])[0]

    return render_template("chat.html", user_input=user_input, response=response, sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
