import requests
import sentry_sdk
from sentry_sdk import configure_scope

sentry_sdk.init("https://dbf98bd7df8941848dc689f45176b3d3@o778448.ingest.sentry.io/5797914")

with configure_scope() as scope:
    scope.set_tag("Project", "IKSiS")
    scope.set_tag("Lab", "2")

try:
    #r=requests.get("https://127.0.0.1:5000/")
    r1=requests.get("https://api.nasa.gov/planetary/apod?api_key=")
    if r1.status_code != 200:
        print("Connection error, logging")
        raise requests.exceptions.ConnectionError("Connection error, logging")
except requests.exceptions.ConnectionError as e:
    sentry_sdk.capture_exception(e)
    print(str(e))
