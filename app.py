from flask import Flask, render_template
from scrape.cse_scrape import *
from utils.duo_auth import DuoAuth as duo
from scrape.cse_scrape import CSEScrape
app = Flask(__name__)

@app.route('/')
def index():
    test_data = {
        "data1" : "hi",
        "data2" : 2,
        "data3" : "testing"
    }
    return render_template('index.html', **test_data)

if __name__ == '__main__':
    app.run(debug=True, port = 8080)
    cse_scrape = CSEScrape()

