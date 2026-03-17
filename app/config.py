import os

class Config:
    def __init__(self):
        self.API_TITLE = os.environ.get('API_TITLE', 'sms-test1 Template')
        self.API_PORT = int(os.environ.get('API_PORT', 8000))

    @property
    def POSTGRES_HOST(self):
        return os.environ.get('POSTGRES_HOST', '')

    @property
    def POSTGRES_PORT(self):
        return int(os.environ.get('POSTGRES_PORT', 5432))

    @property
    def POSTGRES_DB(self):
        return os.environ.get('POSTGRES_DB', 'postgres')

    @property
    def POSTGRES_USER(self):
        return os.environ.get('POSTGRES_USER', 'postgres')

    @property
    def POSTGRES_PASSWORD(self):
        return os.environ.get('POSTGRES_PASSWORD', '')

    @property
    def POSTGRES_CONNECT_TIMEOUT(self):
        return int(os.environ.get('POSTGRES_CONNECT_TIMEOUT', 3))

    @property
    def REDIS_HOST(self):
        return os.environ.get('REDIS_HOST', '')

    @property
    def REDIS_PORT(self):
        return int(os.environ.get('REDIS_PORT', 6379))

    @property
    def REDIS_PASSWORD(self):
        return os.environ.get('REDIS_PASSWORD', '')

    @property
    def REDIS_CONNECT_TIMEOUT(self):
        return int(os.environ.get('REDIS_CONNECT_TIMEOUT', 3))
        
config = Config()
