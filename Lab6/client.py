import json, requests
import sentry_sdk
from sentry_sdk import configure_scope
import logging

sentry_sdk.init("https://f8774516c21f40938838bfe22005ae38@o392992.ingest.sentry.io/5252335")

with configure_scope() as scope:
    scope.set_tag("Project", "IKSiS")
    scope.set_tag("Lab", "2")

try:
    #r=requests.get("https://127.0.0.1:5000/")
    r1=requests.get("https://api.nasa.gov/planetary/apod?api_key=")
    if r1.status_code != 200:
        logging.error("Connection error, logging")
        print("Connection error, logging")
except requests.exceptions.ConnectionError as e:
    sentry_sdk.capture_exception(e)
    r="The destination computer rejected the connection request"
    print(r)
