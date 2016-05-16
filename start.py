import requests
import json
from config import *


req = requests.post('https://www.googleapis.com/qpxExpress/v1/trips/search', json = payload, headers= {"Content-type": "application/json"}, params = {"key": "AIzaSyDD3kocm1L62YyxEWZNwvjPMdyHefIQQnc"});
print req.json()