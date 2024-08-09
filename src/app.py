from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)
print('Model loaded. Check http://127.0.0.1:5000/')


@app.route('/')
def index():
    return render_template('index.html')
if __name__=="__main__":
    app.run(debug="True")