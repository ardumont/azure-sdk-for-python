# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ErrorDetails(Model):
    """Generic resource error details information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: the HTTP status code or error code associated with this error
    :vartype code: str
    :ivar message: the error message localized based on Accept-Language
    :vartype message: str
    :ivar target: the target of the particular error (for example, the name
     of the property in error).
    :vartype target: str
    """ 

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(self):
        self.code = None
        self.message = None
        self.target = None