import json
import requests
import urlparse


def get_teams(webserver_domain, competition_slug, auth=('arena', '123')):
    api_path = "/api/repo/tags/{}/".format("megaminerai-9-space")
    url = urlparse.urljoin(webserver_domain, api_path)
    r = requests.get(url, auth=auth)
    return [t['team']['slug'] for t in r.json()]


if __name__ == '__main__':
    teams = get_teams('http://localhost:8000', 'megaminerai-9-space')
    print json.dumps(teams, indent=2)
