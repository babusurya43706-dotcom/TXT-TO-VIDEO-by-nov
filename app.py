from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'https://t.me/free_for_All_User'


if __name__ == "__main__":
    app.run()
