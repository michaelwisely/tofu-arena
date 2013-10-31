schema = {
    "client": {
        "list_endpoint": "/mies/thunderdome/api/v1/client/",
        "schema": "/mies/thunderdome/api/v1/client/schema/"
        },
    "clientname": {
        "list_endpoint": "/mies/thunderdome/api/v1/clientname/",
        "schema": "/mies/thunderdome/api/v1/clientname/schema/"
        },
    "game": {
        "list_endpoint": "/mies/thunderdome/api/v1/game/",
        "schema": "/mies/thunderdome/api/v1/game/schema/"
        },
    "game_data": {
        "list_endpoint": "/mies/thunderdome/api/v1/game_data/",
        "schema": "/mies/thunderdome/api/v1/game_data/schema/"
        },
    "match": {
        "list_endpoint": "/mies/thunderdome/api/v1/match/",
        "schema": "/mies/thunderdome/api/v1/match/schema/"
        }
    }

game_schema = {
    "allowed_detail_http_methods": [
        "get"
        ],
    "allowed_list_http_methods": [
        "get"
        ],
    "default_format": "application/json",
    "default_limit": 20,
    "fields": {
        "clients": {
            "blank": False,
            "default": "No default provided.",
            "help_text": "Many related resources. Can be either a list of URIs or list of individually nested resource data.",
            "nullable": False,
            "readonly": False,
            "type": "related",
            "unique": False
            },
        "completed": {
            "blank": False,
            "default": "No default provided.",
            "help_text": "A date & time as a string. Ex: \"2010-11-10T03:07:43\"",
            "nullable": True,
            "readonly": False,
            "type": "datetime",
            "unique": False
            },
        "game_data": {
            "blank": False,
            "default": "No default provided.",
            "help_text": "Many related resources. Can be either a list of URIs or list of individually nested resource data.",
            "nullable": True,
            "readonly": False,
            "type": "related",
            "unique": False
            },
        "gamelog_url": {
            "blank": False,
            "default": "",
            "help_text": "Unicode string data. Ex: \"Hello World\"",
            "nullable": False,
            "readonly": False,
            "type": "string",
            "unique": False
            },
        "id": {
            "blank": False,
            "default": "",
            "help_text": "Unicode string data. Ex: \"Hello World\"",
            "nullable": False,
            "readonly": False,
            "type": "string",
            "unique": True
            },
        "loser": {
            "blank": False,
            "default": "No default provided.",
            "help_text": "A single related resource. Can be either a URI or set of nested resource data.",
            "nullable": True,
            "readonly": False,
            "type": "related",
            "unique": False
            },
        "resource_uri": {
            "blank": False,
            "default": "No default provided.",
            "help_text": "Unicode string data. Ex: \"Hello World\"",
            "nullable": False,
            "readonly": True,
            "type": "string",
            "unique": False
            },
        "status": {
            "blank": False,
            "default": "New",
            "help_text": "Unicode string data. Ex: \"Hello World\"",
            "nullable": False,
            "readonly": False,
            "type": "string",
            "unique": False
            },
        "winner": {
            "blank": False,
            "default": "No default provided.",
            "help_text": "A single related resource. Can be either a URI or set of nested resource data.",
            "nullable": True,
            "readonly": False,
            "type": "related",
            "unique": False
            }
        },
    "filtering": {
        "id": [
            "exact"
            ],
        "loser": 2,
        "winner": 2
        },
    "ordering": [
        "completed"
        ]
    }
