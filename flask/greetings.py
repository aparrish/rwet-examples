
from flask import Flask
import random

app = Flask(__name__)

greets = ["Hello", "Hi", "Salutations", "Greetings", "Hey", "Sup"]
places = ["region", "continent", "world", "solar system",
  "galaxy"]

@app.route('/hello')
def hello():
  greeting = random.choice(greets) + ", " + random.choice(places)
  return greeting + "\n"

if __name__ == '__main__':
  app.run()
