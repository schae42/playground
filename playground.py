
from flask import Flask, render_template
app = Flask(__name__)                     

@app.route('/play')                           
def index():
    return render_template('index.html', times=3)

@app.route('/play/<times>')                           
def index_play_boxes(times):
    return render_template('index.html', times=int(times))

@app.route('/play/<times>/<color>')                           
def index_play_color(times, color):
    return render_template('index.html', times=int(times), color=color)

if __name__=="__main__":
    app.run(debug=True)                   
