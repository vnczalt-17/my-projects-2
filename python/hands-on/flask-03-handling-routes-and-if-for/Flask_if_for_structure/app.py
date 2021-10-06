from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    first = 'This is my first conditions experience'
    return render_template('index.html', message = first)

@app.route('/vincenzo')
def mylist():
    names = ["Ahmet Arif", "Salih", "Tarkan", "Sergio", "Halil"]
    return render_template('body.html', object = names)


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)