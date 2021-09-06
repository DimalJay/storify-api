from flask import Flask, jsonify
from storify import getArticles

app = Flask(__name__)

@app.route('/bot')
def bot():
    return jsonify(getArticles())


if __name__ == '__main__':
    app.run()
