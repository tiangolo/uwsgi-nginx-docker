from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print "test"
    return "Hello World!"

if __name__ == "__main__":
    app.run()
