#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def welcome_module():

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True)
        )
    )

    name = module.params['name']
    message = f"Welcome, {name}!"

    module.exit_json(changed=False, msg=message)

if __name__ == '__main__':
    welcome_module()