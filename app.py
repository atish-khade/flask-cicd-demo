from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from CI/CD Pipeline! This line is added on 2nd edit."

app.run(host="0.0.0.0", port=5000)
