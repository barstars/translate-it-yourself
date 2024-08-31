from flask import Flask, request, jsonify
import asyncio

from chatGptParse import ParsGPT
from requestQuotes import RequestQuotes

app = Flask(__name__)


@app.route("/translate", methods=["POST"])
def translateGpt():
  text = request.json["text"]
  answer = ParsGPT().translate(text)
  return jsonify({"answer": answer})


@app.route("/get_random_quote",methods=["POST"])
def get_random_quote():
  tag = request.json["tag"]
  quote = asyncio.run(RequestQuotes(tag).random_quote())
  return jsonify({"quote":quote})

@app.route("/")
def test():
  return ("Hello")


