from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "hello tensorflow"

if __name__ == '__main__':
    app.run()