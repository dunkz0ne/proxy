import nba_api.stats.endpoints as nba

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/api/players/<player_id>/career', methods=['GET'])
def player_career(player_id):
    career = nba.PlayerCareerStats(player_id=player_id)
    return career.get_json()


if __name__ == '__main__':
    app.run("localhost", 5000, debug=True)