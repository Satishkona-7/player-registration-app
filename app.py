from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import os

app = Flask(__name__)

# Read MongoDB connection string from environment variable
mongo_uri = os.environ.get("MONGO_URI")

# Create MongoDB client
client = MongoClient(mongo_uri)

# Database and collection
db = client.playerdb
players_collection = db.players


@app.route('/')
def home():

    # Check if any players exist
    has_players = players_collection.count_documents({}) > 0

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

    # Insert into MongoDB
    players_collection.insert_one(player)

    return redirect('/players')


@app.route('/players')
def show_players():

    # Fetch all players from MongoDB
    players = list(players_collection.find())

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