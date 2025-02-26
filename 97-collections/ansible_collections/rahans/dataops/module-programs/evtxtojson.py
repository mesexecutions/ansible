import json
from evtx import PyEvtxParser

# Initialize an Empty List to Store Event Records
event_records = []

evtxfilepath = 'artifacts/Security_Trim.evtx'

# Parse the .evtx File 
evtxparser = PyEvtxParser(evtxfilepath)

# Iterate through Each record in the evtx File and Append to the List

for record in evtxparser.records_json():
    record['data'] = json.loads(record['data'])
    event_records.append(record)

# Combine all Records into Single Dictionary
events_dict = { 'records': event_records }

# Convert events_dict to a JSON-Formatted String with Indentation
json_formated_events = json.dumps(events_dict, indent=4)
print(json_formated_events)