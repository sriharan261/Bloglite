from  flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "Hello World"

@app.route("/about")
def about():
    return 'about'

if __name__ == "__main__":
    app.debug = True
    app.run()
