from random import sample
from datetime import datetime


def make_meta(limit, offset, total):
    link = "/api/v1/game/?offset={}&limit={}&format=json"

    next_link = None
    if offset + limit <= total:
        next_link = link.format(offset+limit, limit)

    prev_link = None
    if offset - limit >= 0:
        prev_link = link.format(offset-limit, limit)

    meta = {
        "meta": {
            "limit": limit,
            "next": next_link,
            "offset": offset,
            "previous": prev_link,
            "total_count": total
            }
        }

    return meta


def game_object_generator(team_list, total):

    def make_client(team):
        team_id, name = team
        client = {"name": name,
                  "resource_url": "/api/v1/clientname/{}/".format(team_id)}
        return client

    def make_time(_index):
        return datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')

    def make_game_data(team, game_id):
        team_id, name = team
        return {
            "game": "/api/v1/game/{}/".format(game_id),
            "id": "{}".format(game_id),
            "name": {
                "name": name,
                "resource_uri": "/api/v1/clientname/{}/".format(team_id)
                },
            "output_url": "http://placekitten.com/g/200/300",
            "resource_uri": "/api/v1/game_data/669384/",
            "version": "ShellAI",
            "won": None
            }

    for i in range(1, total + 1):
        game_id = i
        teams = sample(list(enumerate(team_list)), 2)
        clients = [make_client(t) for t in teams]
        games = [make_game_data(t, game_id) for t in teams]
        games[0]['won'] = True

        yield {
            "clients": clients,
            "completed": make_time(i),
            "game_data": games,
            "gamelog_url": "http://placekitten.com/g/200/300",
            "id": str(game_id),
            "loser": clients[1],
            "resource_uri": "/api/v1/game/{}/".format(game_id),
            "status": "Complete",
            "winner": clients[0]
            }


def make_game_maker(team_list, total):
    games = list(game_object_generator(team_list, total))
    games.reverse()

    def make_game(limit, offset):
        results = {
            "meta": make_meta(limit, offset, total),
            "objects": games[offset:limit+offset],
            }
        return results

    return make_game
