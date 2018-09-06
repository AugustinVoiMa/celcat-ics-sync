import json

class Conf:
    def __init__(self, configfile="/etc/celcat_ics_sync.conf.json"):
        self.conf = None
        with open(configfile, "r") as file:
            self.conf = json.loads(file.read())
        if(self.conf == None):
            print("Error loading config file "+configfile)
            exit(1)

    @property
    def sites(self):
        return self.conf["sites"].keys()

    def getsite(self, site):
        return self.conf["sites"][site]
