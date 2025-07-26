from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Success is not in what you have, but who you are.",
    "Your time is limited, don't waste it living someone else's life.",
    "Don't let yesterday take up too much of today.",
    "The harder you work for something, the greater you'll feel when you achieve it."
]

@app.route('/')
def index():
    quote = random.choice(quotes)
    return render_template('index2.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)