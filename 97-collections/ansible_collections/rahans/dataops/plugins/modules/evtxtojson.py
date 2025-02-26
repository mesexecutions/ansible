from ansible.module_utils.basic import AnsibleModule
import json
from evtx import PyEvtxParser


'''
Python Module Required:

    pip install evtx

Reference: https://pypi.org/project/evtx/
'''

def main():
    module = AnsibleModule(
        argument_spec=dict(
            evtx_filepath=dict(type='str', required=True)
        )
    )

    # The Ansible playbook must provide the filepath to the Event Log Viewer (.evtx) file as a module argument.

    evtx_filepath = module.params['evtx_filepath']

    # Initialize Empty List to Store all Records from Event (.evtx) File
    event_records = []

    # Parse the EVTX file 
    evtx_parser = PyEvtxParser(evtx_filepath)

    # Iterate thorugh Each Record in the evtx_parser and Apped to the List event_records
    for record in evtx_parser.records_json():
        record['data'] = json.loads(record['data'])
        event_records.append(record)

    # Combine all Records into a Single Dictionary
    event_records_dict = { 'records': event_records }

    # Return the JSON Formatted Events as the Result of the Ansible Module Execution
    module.exit_json(changed=True, events=event_records_dict)

if __name__ == '__main__':
    main()

