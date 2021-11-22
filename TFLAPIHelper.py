import requests
import urllib.parse


class TFLAPIHelper:

    # TFL API
    ## AccidentStats

    def getAccidentStatsWithYear(self, year: str):
        headers = {
            # Request headers
            'Cache-Control': 'no-cache',
        }
        if self.valid_year(year):
            return self.getJsonFromCustomUrl("https://api.tfl.gov.uk/AccidentStats/" + year, headers=headers)
        else:
            print("Invalid year entered: %s" % year)

    ## AirQuality

    def getAirQuality(self):
        headers = {
            # Request headers
            'Cache-Control': 'no-cache',
        }
        return self.getJsonFromCustomUrl("https://api.tfl.gov.uk/AirQuality/", headers=headers)

    # Post Utilities

    def printBasicPost(self, url, data):
        print(self.postBasicJson(url, data))

    def postBasicJson(self, url, data):
        return self.postJsonFromCustomUrl(url, data)

    def postJsonFromCustomUrl(self, url, data, params=None, headers=None):
        return self.postRequestFromCustomUrl(url,data, params, headers).json()

    def postRequestFromCustomUrl(self, url: str, data, params=None, headers=None):
        if headers is None:
            headers = {}
        if params is None:
            params = {}
        return requests.post(url, data, params=params, headers=headers)

    # Get Utilities

    def printBasicGet(self, url):
        print(self.getBasicJson(url))

    def getBasicJson(self, url):
        return self.getJsonFromCustomUrl(url)

    def getJsonFromCustomUrl(self, url, params=None, headers=None):
        return self.getRequestFromCustomUrl(url, params, headers).json()

    def getRequestFromCustomUrl(self, url: str, params=None, headers=None):
        if headers is None:
            headers = {}
        if params is None:
            params = {}
        return requests.get(url, params=params, headers=headers)

    # Request Validation Utilities
    def valid_year(self, year: str):
        if year and year.isdigit():
            return 1900 <= int(year) <= 2021


helper = TFLAPIHelper()
print(helper.getAccidentStatsWithYear("2012"))

