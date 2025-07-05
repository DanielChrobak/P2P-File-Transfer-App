from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/app')
def app_page():
    return render_template('app.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
