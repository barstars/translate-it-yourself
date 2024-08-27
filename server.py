from flask import Flask, request, jsonify
from chatGptParse  import *
from requestQuotes import ReauestQuotes

app = Flask(__name__)

@app.route("/translate",methods=["POST"])
def translateGpt():
	tag = request.json["tag"]
	quote = ReauestQuotes(tag).randomQuote()
	print(quote)
	return translate(quote)

if __name__ == '__main__':
	app.run(debug="True")