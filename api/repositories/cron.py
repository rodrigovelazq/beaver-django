import requests
import time
from rest_framework import status
from rest_framework.response import Response
from .models import Owners

MAX_RETRIES = 5  # Arbitrary number of times we want to try

def job_retrieve_repositories_from_github():
    owner = Owners.objects.create(login='Apple')
    owner.save()
    f = open("/home/rodrigo/Desktop/demofile.txt", "w+")
    f.write("> job_retrieve_repositories_from_github is running...")
    f.close()
    #self.external_api_view()


# def github_api_request(self):
#     attempt_num = 0  # keep track of how many times we've retried
#     while attempt_num < MAX_RETRIES:
#         r = requests.get("http://api.github.com/repos/facebook/react", timeout=10)
#         if r.status_code == 200:
#             data = r.json()
#
#
#                 return
#             else:
#                 attempt_num += 1
#                 # You can probably use a logger to log the error here
#                 time.sleep(5)  # Wait for 5 seconds before re-trying
#         raise Exception("Request failed, too many retries attempted")