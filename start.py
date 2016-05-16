import requests
import json
from testFile import *
from pprintpp import pprint
from config import *


'''req = requests.post(
						'https://www.googleapis.com/qpxExpress/v1/trips/search',
						json = payload,
						headers = {"Content-type": "application/json"},
						params = {"key": "AIzaSyDD3kocm1L62YyxEWZNwvjPMdyHefIQQnc"}
					)'''

dataFlights = p;
#dataFlights = req.json()

#for option in dataFlights['trips']['tripOption']:
print pprint(dataFlights['trips']['tripOption'][0], width=1)

