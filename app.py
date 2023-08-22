from flask import Flask, render_template

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
