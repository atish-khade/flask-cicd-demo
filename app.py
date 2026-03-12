from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from CI/CD Pipeline! This line is added on 2nd edit. Webhook was tested on 12-Mar-26. This line was added after"

app.run(host="0.0.0.0", port=5000)
