from flask import Flask, render_template, request, redirect

app = Flask(__name__)

players = []

@app.route('/')
def home():
    has_players = len(players) > 0
    return render_template('index.html', has_players=has_players)

@app.route('/register', methods=['POST'])
def register():
    player = {
        'name': request.form.get('name'),
        'age': request.form.get('age'),
        'sport': request.form.get('sport'),
        'team': request.form.get('team'),
        'email': request.form.get('email')
    }

    players.append(player)

    return redirect('/players')

@app.route('/players')
def show_players():
    return render_template('players.html', players=players)

if __name__ == '__main__':
    app.run(debug=True)