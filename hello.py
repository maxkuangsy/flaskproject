from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello World! I love python'

@app.route('/book')
def book():
    return 'Books!'

@app.route('/book/<int:id>/price')
def price(id):
    return  str(id)

if __name__ == '__main__':
    app.run(debug=True)