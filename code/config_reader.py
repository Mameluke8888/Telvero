from code.json_file_reader import JsonFileReader
from code.ini_file_reader import IniFileReader


class ConfigReader:
    def __init__(self, filename):
        self.reader = None

        if filename.endswith(".json"):
            self.reader = JsonFileReader(filename)
        elif filename.endswith(".ini"):
            self.reader = IniFileReader(filename)
        else:
            raise Exception("File format is not supported")

    def get_browser(self, section_name):
        return self.reader.get_browser(section_name)

    def get_wait_time(self, section_name):
        return self.reader.get_wait_time(section_name)

    def get_email(self, section_name):
        return self.reader.get_email(section_name)

    def get_password(self, section_name):
        return self.reader.get_password(section_name)

    def get_first_name(self, section_name):
        return self.reader.get_first_name(section_name)

    def get_last_name(self, section_name):
        return self.reader.get_last_name(section_name)

    def get_phone(self, section_name):
        return self.reader.get_phone(section_name)

    def get_order_id(self, section_name):
        return self.reader.get_order_id(section_name)

    def get_product_name(self, section_name):
        return self.reader.get_product_name(section_name)

    def get_product_code(self, section_name):
        return self.reader.get_product_code(section_name)

    def get_quantity(self, section_name):
        return self.reader.get_quantity(section_name)

    def get_order_date(self, section_name):
        return self.reader.get_order_date(section_name)

    def get_return_reason(self, section_name):
        return self.reader.get_return_reason(section_name)

    def get_product_opened(self, section_name):
        return self.reader.get_product_opened(section_name)

    def get_address(self, section_name):
        return self.reader.get_address(section_name)

    def get_city(self, section_name):
        return self.reader.get_city(section_name)