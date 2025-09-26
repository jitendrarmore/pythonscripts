import re
from collections import Counter
from http.client import responses

import requests
def logSeach(logFileName):

    Logs = []

    with open(logFileName, 'r') as file:
        for line in file:
            match =  re.search('error code', line)
            if match:
                Logs.append(match.group(1))


    count = Counter(Logs)




