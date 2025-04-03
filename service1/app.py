from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/service1')
def service1():
    return render_template('service1.html')

@app.route('/service2')
def service2():
    return redirect("http://<service2-loadbalancer-ip>")

@app.route('/service3')
def service3():
    return redirect("http://<service3-loadbalancer-ip>")

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)), host='0.0.0.0', debug=True)
