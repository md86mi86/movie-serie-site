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

# series Pages

@app.route('/Asura')
def Asura():
    return send_from_directory('src/series', 'Asura.html')

@app.route('/Miss-austen')
def MissAusten():
    return send_from_directory('src/series', 'Miss-austen.html')

@app.route('/Mo')
def Mo():
    return send_from_directory('src/series', 'Mo.html')

@app.route('/Namibeu')
def Namibeu():
    return send_from_directory('src/series', 'Namibeu.html')

@app.route('/Out-there')
def OutThere():
    return send_from_directory('src/series', 'Out-there.html')

@app.route('/Prison-cell-211')
def PrisonCell211():
    return send_from_directory('src/series', 'Prison-cell-211.html')

@app.route('/Protection')
def Protection():
    return send_from_directory('src/series', 'Protection.html')

@app.route('/The-hooligan')
def TheHooligan():
    return send_from_directory('src/series', 'The-hooligan.html')

@app.route('/The-penguin')
def ThePenguin():
    return send_from_directory('src/series', 'The-penguin.html')

@app.route('/Until-i-kill-you')
def UntilIKillYou():
    return send_from_directory('src/series', 'Until-i-kill-you.html')

# banner movie
@app.route('/The-Dark-Knight')
def TheDarkKnight():
    return send_from_directory('src/movies', 'The-Dark-Knight.html')

# 404 error
@app.errorhandler(404)
def notFound(e):
    return send_from_directory('src', '404.html'),404

if __name__ == '__main__':
    app.run(debug=True)
