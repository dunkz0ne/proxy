import nba_api.stats.endpoints as nba

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Player
@app.route('/api/players/<player_id>/career', methods=['GET'])
def player_career(player_id):
    career = nba.PlayerCareerStats(player_id=player_id)
    return career.get_json()

# Team
@app.route('/api/teams/<team_id>', methods=['GET'])
def team_details(team_id):
    team = nba.TeamDetails(team_id=team_id)
    return team.get_json()

@app.route('/api/teams/<team_id>/roster', methods=['GET'])
def team_roster(team_id):
    team = nba.CommonTeamRoster(team_id=team_id)
    return team.get_json()

@app.route('/api/teams/<team_id>/schedule', methods=['GET'])
def team_schedule(team_id):
    team = nba.TeamGameLog(team_id=team_id)
    return team.get_json()

# Match
@app.route('/api/matches/<match_id>', methods=['GET'])
def match_details(match_id):
    match = nba.BoxScoreMatchupsV3(game_id=match_id)
    return match.get_json()

# League
@app.route('/api/league/standings', methods=['GET'])
def league_standings():
    standings = nba.LeagueStandings()
    return standings.get_json()

@app.route('/api/league/leaders', methods=['GET'])
def league_leaders():
    leaders = nba.LeagueLeaders()
    return leaders.get_json()


if __name__ == '__main__':
    app.run("localhost", 5000, debug=True)