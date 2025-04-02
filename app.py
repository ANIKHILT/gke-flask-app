from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/service1')
def service1():
    return render_template('service1.html')

@app.route('/service2')
def service2():
    return redirect("https://www.programiz.com/sql/online-compiler")

@app.route('/service3')
def service3():
    return redirect("https://www.programiz.com/python-programming/online-compiler")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000
