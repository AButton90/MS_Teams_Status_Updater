import json


class MSTeams():
    def __init__(self):
        pass

    def connect_to_ms_teams(self):
        """Function that connects to the user's Micorsoft Teams account"""
        pass

    def update_status(self, status: str, message: str, debug: bool = False):
        """Function that updates the user's MS Teams Status and Status Message"""
        pass

    def check_status(self):
        """Function that checks the current Status and Status Message on the user's MS Teams account"""
        pass


class HTMLGenerator():
    def __init__(self):
        self.set_config_json()

    def set_config_json(self):
        """Function that imports the config file containing all the project data the user is working on.
        This file is used to generate the HTML template"""

        with open("config.json", "r") as file:
            self.config_json = json.load(file)

    def generate_html(self):
        """Function that creates the HTML template for the MS Teams Updater App"""
        pass
