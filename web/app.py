from flask import Flask, request, render_template
app=Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello'

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/hpcapture.html')
def hpcapture():
    return render_template("hpcapture.html")

@app.route('/hpcrime.html')
def hpcrime():
    return render_template("hpcrime.html")

if __name__=='__main__':
    app.run()