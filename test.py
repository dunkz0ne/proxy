from requests import request
import json

print("------TESTING PLAYER CAREER------")

players = ['1629029', '2544', '203507', '201142', '203999']
passed = 0
for player in players:
    url = f'http://localhost:5000/api/players/{player}/career'
    response = request('GET', url)
    data = json.loads(response.text)
    open('json/player-career.json', 'w').write(json.dumps(data, indent=4))
    if int(data['parameters']['PlayerID']) == int(player):
        print(f"Player {player} career stats: \033[92mPASSED\033[0m")
        passed += 1
    else:
        print(f"Player {player} career stats: \033[91mFAILED\033[0m")

print(f"Player career test: {passed}/{len(players)} passed")
print("------END TESTING PLAYER CAREER------")

print("------TESTING TEAM DETAILS------")

teams = ['1610612737', '1610612738', '1610612747', '1610612744', '1610612745']
passed = 0
for team in teams:
    url = f'http://localhost:5000/api/teams/{team}'
    response = request('GET', url)
    data = json.loads(response.text)
    open('json/team-details.json', 'w').write(json.dumps(data, indent=4))
    if int(data['parameters']['TeamID']) == int(team):
        print(f"Team {team} career stats: \033[92mPASSED\033[0m")
        passed += 1
    else:
        print(f"Team {team} career stats: \033[91mFAILED\033[0m")

print(f"Team details test: {passed}/{len(players)} passed")
print("------END TESTING TEAM DETAILS------")

print("------TESTING TEAM ROSTER------")

teams = ['1610612737', '1610612738', '1610612747', '1610612744', '1610612745']
passed = 0
for team in teams:
    url = f'http://localhost:5000/api/teams/{team}/roster'
    response = request('GET', url)
    data = json.loads(response.text)
    open('json/team-roster.json', 'w').write(json.dumps(data, indent=4))
    if int(data['parameters']['TeamID']) == int(team):
        print(f"Team {team} roster: \033[92mPASSED\033[0m")
        passed += 1
    else:
        print(f"Team {team} roster: \033[91mFAILED\033[0m")

print(f"Team roster test: {passed}/{len(players)} passed")
print("------END TESTING TEAM ROSTER------")

print("------TESTING TEAM SCHEDULE------")

teams = ['1610612737', '1610612738', '1610612747', '1610612744', '1610612745']
passed = 0
for team in teams:
    url = f'http://localhost:5000/api/teams/{team}/schedule'
    response = request('GET', url)
    data = json.loads(response.text)
    open('json/team-schedule.json', 'w').write(json.dumps(data, indent=4))
    if int(data['parameters']['TeamID']) == int(team):
        print(f"Team {team} schedule: \033[92mPASSED\033[0m")
        passed += 1
    else:
        print(f"Team {team} schedule: \033[91mFAILED\033[0m")

print(f"Team schedule test: {passed}/{len(players)} passed")
print("------END TESTING TEAM SCHDULE------")

print("------TESTING MATCH DETAILS------")

matches = ['0022000001', '0022000002', '0022000003', '0022000004', '0022000005']
passed = 0
for match in matches:
    url = f'http://localhost:5000/api/matches/{match}'
    response = request('GET', url)
    data = json.loads(response.text)
    open('json/match-details.json', 'w').write(json.dumps(data, indent=4))
    if int(data['boxScoreMatchups']['gameId']) == int(match):
        print(f"Match {match} details: \033[92mPASSED\033[0m")
        passed += 1
    else:
        print(f"Match {match} details: \033[91mFAILED\033[0m")

print(f"Match details test: {passed}/{len(players)} passed")
print("------END TESTING MATCH DETAILS------")
