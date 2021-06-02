import sentry_sdk
import random
from sentry_sdk import configure_scope

sentry_sdk.init("https://dbf98bd7df8941848dc689f45176b3d3@o778448.ingest.sentry.io/5797914")

with configure_scope() as scope:
    scope.set_tag("Project", "IKSiS")
    scope.set_tag("Lab", "2")

try:
    while True:
        print(1/random.randint(-5,5))
except Exception as e:
    sentry_sdk.capture_exception(e)
    print(str(e))
