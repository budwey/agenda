# LIST OF CONSTANTS FOR SERVER CONFIGURATION

# FLASK_ENV
flask_env = 'FLASK_ENV'
# ENVIRONMENTS
envs = {
    'dev': {
        'name': 'development',
        'path': '.env_dev'
    },
    'prod': {
        'name': 'production',
        'path': '.env_prod'
    },
}
# ENVIRONMENT PARAMS
env_params = {
    'debug': 'FLASK_DEBUG',
    'database_url': 'SQLALCHEMY_DATABASE_URI',
    'database_tracking': 'SQLALCHEMY_TRACK_MODIFICATIONS'
}
# MESSAGES
messages = {
    'db': {
        'success': "Success: Database connected.",
        'error': "Error: An error has occurred while connecting to database."
    },
    'api': {
        'success': "Success: API Service mounted.",
        'error': "Error: An error has occurred while mounting API Service."
    },
    'schema': {
        'success': "Success: Schemas Service mounted.",
        'error': "Error: An error has occurred while mounting Schemas Service."
    }
}
