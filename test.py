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
        print(f"Player {player} career stats: PASSED")
        passed += 1
    else:
        print(f"Player {player} career stats: FAILED")

print(f"Player career test: {passed}/{len(players)} passed")
print("------END TESTING PLAYER CAREER------")

