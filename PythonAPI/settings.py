import os
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
# MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'user')
# MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'user')
# MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'cooldb')

DOMAIN = {
    'cooltweets': {
        'schema': {
            'text': {
                'type': 'string',
                'maxlength': 140,
            },
            'id': {
                'type': 'number',
                'unique': True
            },
            'screen_name': {
                'type': 'string',
                'unique': True
            }
        }
    }
}

# MONGO_USERNAME = 'username'
#
# MONGO_PASSWORD = 'password'
#
# MONGO_DBNAME = 'cooldb'

RESOURCE_METHODS = ['GET', 'POST']