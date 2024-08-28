from flask import Flask, request

from chatGptParse import ParsGPT
from requestQuotes import ReauestQuotes

app = Flask(__name__)


@app.route("/translate", methods=["POST"])
def translateGpt():
  tag = request.json["tag"]
  quote = ReauestQuotes(tag).randomQuote()
  answer = ParsGPT().translate(quote)
  return {"answer": answer}


@app.route("/")
def test():

  return ("Hello")


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
