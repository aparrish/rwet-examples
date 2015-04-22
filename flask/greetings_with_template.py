
from flask import Flask, render_template
import random

app = Flask(__name__)

greets = ["Hello", "Hi", "Salutations", "Greetings", "Hey", "Sup"]
places = ["region", "continent", "world", "solar system",
  "galaxy"]

@app.route('/hello')
def hello():
  return render_template("greeting.html",
    greet=random.choice(greets), place=random.choice(places))

if __name__ == '__main__':
  app.run()
