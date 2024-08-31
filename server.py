from flask import Flask, request, jsonify
import asyncio

from chatGptParse import ParsGPT
from requestQuotes import RequestQuotes

app = Flask(__name__)


@app.route("/translate", methods=["POST"])
def translateGpt():
  text = request.json["text"]
  translate = ParsGPT().translate(text)
  return jsonify({"translate": translate})


@app.route("/get_random_quote",methods=["POST"])
def get_random_quote():
  tag = request.json["tag"]
  quote = asyncio.run(RequestQuotes(tag).random_quote())
  return jsonify({"quote":quote})


@app.route("/teach_me",methods=["POST"])
def teach_me():
  orginal = request.json["orginal"]
  user_translate = request.json["user_translate"]

  teach = ParsGPT().teach(user_translate,orginal)
  return jsonify({"teach":teach})

@app.route("/")
def test():
  return ("Hello")

app.run(debug=True)