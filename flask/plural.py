
from flask import Flask, request
from textblob import Word

app = Flask(__name__)

@app.route('/plural')
def define():
  word_str = request.args['word']
  word_obj = Word(word_str)
  return word_obj.pluralize() + "\n"
  
if __name__ == '__main__':
  app.run()
