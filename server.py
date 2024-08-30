from flask import Flask, request
import asyncio

from chatGptParse import ParsGPT
from requestQuotes import RequestQuotes

app = Flask(__name__)


@app.route("/translate", methods=["POST"])
def translateGpt():
  tag = request.json["tag"]
  quote = asyncio.run(RequestQuotes(tag).random_quote())
  print(quote)
  answer = ParsGPT().translate(quote)
  return {"answer": answer}


@app.route("/")
def test():

  return ("Hello")


