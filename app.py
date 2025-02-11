from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return send_from_directory('src', 'index.html')

@app.route('/login')
def login():
    return send_from_directory('src', 'login.html')

@app.route('/signup')
def signup():
    return send_from_directory('src', 'signup.html')

@app.route('/terms-of-use')
def termsOfUse():
    return send_from_directory('src', 'TermsOfUse.html')

@app.route('/about-us')
def aboutUs():
    return send_from_directory('src', 'aboutUs.html')

@app.route('/contact-us')
def contactUs():
    return send_from_directory('src', 'contactUs.html')

@app.route('/movies')
def movies():
    return send_from_directory('src', 'movies.html')

@app.errorhandler(404)
def notFound(e):
    return send_from_directory('src', '404.html'),404

if __name__ == '__main__':
    app.run(debug=True)
