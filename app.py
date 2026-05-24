from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Temporary in-memory storage
players = []


@app.route('/')
def home():

    # Check if any players exist
    has_players = len(players) > 0

    return render_template(
        'index.html',
        has_players=has_players
    )


@app.route('/register', methods=['POST'])
def register():

    # Collect form data
    player = {
        'name': request.form.get('name'),
        'age': request.form.get('age'),
        'sport': request.form.get('sport'),
        'team': request.form.get('team'),
        'email': request.form.get('email')
    }

    # Store in memory
    players.append(player)

    return redirect('/players')


@app.route('/players')
def show_players():

    return render_template(
        'players.html',
        players=players
    )


@app.route('/health')
def health():

    return {
        "status": "healthy"
    }, 200


if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        port=8000
    )