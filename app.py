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

@app.route('/series')
def series():
    return send_from_directory('src', 'series.html')

# Movies Pages

@app.route('/Julie-Keeps-Quiet')
def JulieKeepsQuiet():
    return send_from_directory('src/movies', 'Julie-Keeps-Quiet.html')

@app.route('/Once')
def Once():
    return send_from_directory('src/movies', 'Once.html')

@app.route('/Perdida')
def Perdida():
    return send_from_directory('src/movies', 'Perdida.html')

@app.route('/Planes')
def Planes():
    return send_from_directory('src/movies', 'Planes.html')

@app.route('/Nickel-Boys')
def NickelBoys():
    return send_from_directory('src/movies', 'Nickel-Boys.html')

@app.route('/Distant')
def Distant():
    return send_from_directory('src/movies', 'Distant.html')

@app.route('/Kinda-Pregnant')
def KindaPregnant():
    return send_from_directory('src/movies', 'Kinda-Pregnant.html')

@app.route('/Spread')
def Spread():
    return send_from_directory('src/movies', 'Spread.html')

@app.route('/Princess-Protection-Program')
def PrincessProtectionProgram():
    return send_from_directory('src/movies', 'Princess-Protection-Program.html')

@app.route('/The-Intruder')
def TheIntruder():
    return send_from_directory('src/movies', 'The-Intruder.html')

# banner movie
@app.route('/The-Dark-Knight')
def TheDarkKnight():
    return send_from_directory('src/movies', 'The-Dark-Knight.html')

@app.errorhandler(404)
def notFound(e):
    return send_from_directory('src', '404.html'),404

if __name__ == '__main__':
    app.run(debug=True)
