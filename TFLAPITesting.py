import requests
import urllib.parse

headers = {
# Request headers
'Cache-Control': 'no-cache',
}

params = urllib.parse.urlencode({
})

try:
    print(requests.get("https://api.tfl.gov.uk/Place/Meta/Categories", params=params, headers=headers).json())
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))