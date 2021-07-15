from configparser import  ConfigParser

class IniFileReader:
    def __init__(self, filename):
        self.data = None

        with open(filename, 'r') as config_file:
            self.data = ConfigParser()
            self.data.read_file(config_file)

    def get_browser(self, section_name):
        value = self.data.get(section_name, 'browser', fallback=None)
        if value is None:
            raise Exception("Browser option is not present in the config file")
        return value

    def get_wait_time(self, section_name):
        value = self.data.get(section_name, 'wait', fallback=None)
        if value is None:
            raise Exception("Wait_time option is not present in the config file")
        return int(value)

    def get_email(self, section_name):
        value = self.data.get(section_name, "email", fallback=None)
        if value is None:
            raise Exception("email option is not found in section ", section_name)
        return value

    def get_password(self, section_name):
        value = self.data.get(section_name, "password", fallback=None)
        if value is None:
            raise Exception("password option is not found in section ", section_name)
        return value