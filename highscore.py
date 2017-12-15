#WORK IN PROGRESS, DON'T USE IT UNTILL YOU ARE CERTIFIED TO USE IT
def post(user, score, game_id):
    import requests
    import json
    print(user)
    print(score)
    print(game_id)
    url = "https://ghosting.nl/pygame/"
    data = {'user': user, 'score': score, 'game_id': game_id}
    print(data)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)

    print(r)