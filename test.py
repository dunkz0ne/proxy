from requests import request
import json

# player career

print("------TESTING PLAYER CAREER------")

players = ['1629029', '2544', '203507', '201142', '203999']
passed = 0
for player in players:
    url = f'http://localhost:5000/api/players/{player}/career'
    response = request('GET', url)
    data = json.loads(response.text)
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
    if int(data['parameters']['TeamID']) == int(team):
        print(f"Team {team} career stats: \033[92mPASSED\033[0m")
        passed += 1
    else:
        print(f"Team {team} career stats: \033[91mFAILED\033[0m")

print(f"Player career test: {passed}/{len(players)} passed")
print("------END TESTING PLAYER CAREER------")