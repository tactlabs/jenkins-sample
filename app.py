from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'nalla work akuthu super !!!!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
