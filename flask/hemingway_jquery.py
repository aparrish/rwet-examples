
from flask import Flask, request, render_template
from textblob import TextBlob
import random

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("hemingway_jquery.html")

@app.route('/transformed', methods=["POST"])
def transformed():
  text = request.form['text']
  blob = TextBlob(text)
  output = list()
  for sentence in blob.sentences:
    if len(sentence.words) <= 5:
      output.append(unicode(sentence))
  return ' '.join(output)

if __name__ == '__main__':
  app.run()
