from flask import Flask, jsonify
from storify import getArticles

app = Flask(__name__)

@app.route('/bot')
def bot():
    return jsonify(getArticles())


app.run( port=8000, debug=True)
