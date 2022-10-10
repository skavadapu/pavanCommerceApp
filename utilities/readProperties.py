import configparser

# in order to read the config.ini file we need to use the configparser package
config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')


class ReadConfig:
    # staticmethod tag allows to use the method directly in child class without creating object
    @staticmethod
    def getApplicationUrl():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'userEmail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
