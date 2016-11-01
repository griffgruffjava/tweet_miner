DOMAIN = {
    'user': {
        'schema': {
            'firstname': {
                'type': 'string'
            },
            'lastname': {
                'type': 'string'
            },
            'username': {
                'type': 'string',
                 'unique': True
            },
            'password': {
                'type': 'string'
            },
            'phone': {
                'type': 'string'
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