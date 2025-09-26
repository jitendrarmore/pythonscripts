
import re
from datetime import datetime

def parseLogginf(logfile, logLevel, startDate=None, endDate=None):

    logs = []
    startDate = datetime.strptime(startDate, "%Y-%m-%d")
    endDate = datetime.strptime(endDate, "%Y-%m-%d")

    with open(logfile, 'r') as f:
        for line in f:
            try:
                logDate = line[:10]
                logDateParse = datetime.strptime(logDate, "%Y-%m-%d")
                if startDate <= logDateParse <= endDate and logLevel in line:
                    logs.append(line)
            except:
                print(f"Skipping line due to date parsing error: {line.strip()}")
                continue

    for log in logs:
        print(log.strip())

parseLogginf('application_log', 'INFO', '2025-07-11', '2025-07-13')