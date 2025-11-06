from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'https://t.me/selectionway_free_course'


if __name__ == "__main__":
    app.run()
