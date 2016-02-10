from __future__ import print_function

from statuscake_customresource.create import create_status_cake
from statuscake_customresource.delete import delete_status_cake
from statuscake_customresource.update import update_status_cake


def handler(event, context):
    request_type = event['RequestType']

    if request_type == 'Create':
        return create_status_cake(event)
    elif request_type == 'Delete':
        return delete_status_cake(event)
    elif request_type == 'Update':
        return update_status_cake(event)
    else:
        raise 'Unknown request type {}'.format(request_type)


