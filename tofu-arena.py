from bottle import route, run, request

from schema import schema, game_schema
from game import make_game_maker
from webserver import get_teams


TOTAL_GAMES = 50
TEAMS = get_teams('http://localhost:8000', 'megaminerai-9-space')

make_game = make_game_maker(TEAMS, TOTAL_GAMES)


@route('/api/v1/')
def get_schema():
    return schema


#@route('/api/v1/game/schema/')
def get_game_schema():
    return game_schema


@route('/api/v1/game/')
def game_list():
    limit = request.query.limit or '20'
    offset = request.query.offset or '0'
    return make_game(int(limit), int(offset))



run(host='localhost', port=8080, debug=True, reloader=True)
