from flask import Flask, render_template, request, jsonify,flash


app = Flask(__name__)


@app.route('/main')
def main():
    return render_template("home.html")
@app.route('/team')
def teams():
    return render_template("team.html")

@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")
##

##
@app.route('/parent2/bm/leaning')
def leaning_bmp2():
    return render_template('parent2/bm/leaning.html')
@app.route('/parent2/bm/fullbend')
def fullbend_bmp2():
    return render_template('parent2/bm/fullbend.html')
@app.route('/parent2/bm/bend40')
def bend40_bmp2():
    return render_template('parent2/bm/bend40.html')
@app.route('/parent2/bm/bend70')
def bend70_bmp2():
    return render_template('parent2/bm/bend70.html')
@app.route('/parent2/bm/sq')
def sq_bmp2():
    return render_template('parent2/bm/sq.html')

## 


## Parent page 1 
@app.route('/parent1/bm/leaning')
def main95():
    return render_template('parent1/bm/leaning.html')

##
@app.route('/parent1/bm/leaning')
def leaning_bmp1():
    return render_template('parent1/bm/leaning.html')
@app.route('/parent1/bm/fullbend')
def fullbend_bmp1():
    return render_template('parent1/bm/fullbend.html')
@app.route('/parent1/bm/bend40')
def bend40_bmp1():
    return render_template('parent1/bm/bend40.html')
@app.route('/parent1/bm/bend70')
def bend70_bmp1():
    return render_template('parent1/bm/bend70.html')
@app.route('/parent1/bm/sq')
def sq_bmp1():
    return render_template('parent1/bm/sq.html')

## 



if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=False)
    app.run(host='10.0.0.57', port=8900, debug=True)