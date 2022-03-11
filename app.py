from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

PORT = os.getenv('PORT_NO')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world jenkins deployment work paniruchu !!!!'

if __name__ == '__main__':
    app.run(debug=True,host=PORT)
