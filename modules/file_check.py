#!/usr/bin/python

import os
from ansible.module_utils.basic import AnsibleModule

def file_check(path):
   if os.access(path, os.F_OK):
      return True
   else:
      return False

def main():
   
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(required=True)
        ),
    supports_check_mode=True
    )

    params = module.params
    path = params['path']

    if file_check(path):
        module.exit_json(changed=False, status=True)
    else:
        module.exit_json(changed=False, status=False)

if __name__ == '__main__':
    main()
    

        
