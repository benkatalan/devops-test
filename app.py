from flask import Flask
app = Flask(__name__)
@app.get('/')
def home():
    return "hello from docker"
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)

