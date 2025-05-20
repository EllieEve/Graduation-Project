from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/oyun')
def oyun():
    return render_template('oyun.html')

@app.route('/recycle')
def recycle():
    return render_template('recycle.html')

@app.route('/infobox')
def infobox():
    return render_template('infobox.html')

@app.route('/galeri')
def galeri():
    return render_template('galeri.html')

if __name__ == "__main__":
    app.run(debug=True)

app = Flask(__name__)
