#!/usr/bin/python3
"""
Compile Datadog Users, Application key and API key
"""
#import sys
#from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.users_api import UsersApi
from datadog_api_client.v1.api.key_management_api import KeyManagementApi

def get_users(configuration):
    "Returns users"

    with ApiClient(configuration) as api_client:
        api_instance = UsersApi(api_client)
        response = api_instance.list_users()

    # https://datadoghq.dev/datadog-api-client-python/datadog_api_client.v1.model.html#module-datadog_api_client.v1.model.user
    # response = {
    #     'users': [
    #         {
    #             'access_role': 'adm',
    #             'disabled': False,
    #             'email': 'some.email@example.com',
    #             'handle': 'email@addresss.com',
    #             'icon': 'https://secure.gravatar.com/avatar/...',
    #             'is_admin': True,
    #             'name': 'Firstname Lastname',
    #             'role': None,
    #             'title': None,
    #             'verified': True
    #         }, {...}
    #     ]
    # }

    # Convert response.users from list of object to list of dict
    headers = ['access_role', 'disabled', 'email', 'handle', 'icon', 'is_admin', 'name', 'role',
               'title', 'verified']
    users=[]
    for user in response.users:
        to_insert= {}
        for header in headers:
            to_insert[header] = user[header]
        users.append(to_insert)
    return users

def get_api_keys(configuration):
    """Returns API keys"""

    with ApiClient(configuration) as api_client:
        api_instance = KeyManagementApi(api_client)
        response = api_instance.list_api_keys(
        )

    # response = {
    #     'api_keys': [
    #         {
    #             'created': '2022-12-27 13:57:13',
    #             'created_by': 'email@example.com',
    #             'disabled': '',
    #             'disabled_by': '',
    #             'is_active': True,
    #             'key': 'hexdigits...',
    #             'name': 'key_name'
    #         }, {...}
    #     ]
    # }
    return response.api_keys

def get_app_keys(configuration):
    """Returns APPLICATION keys"""

    with ApiClient(configuration) as api_client:
        api_instance = KeyManagementApi(api_client)
        response = api_instance.list_application_keys(
        )

     # response = {
     #     'application_keys': [
     #         {
     #             'hash': '8e3f15a79113174ef2408a06adc20d6f92f28014',
     #             'name': '20min-Dev Agent Deployment',
     #             'org_id': 1000039376,
     #             'owner': 'baptiste.blanc@tx.group',
     #             'revoked': False
     #         }, {...}
     #     ]
     # }
    return response.application_keys

DATADOG_CONFIGURATION = Configuration()

USERS=get_users(DATADOG_CONFIGURATION)
API_KEYS=get_api_keys(DATADOG_CONFIGURATION)
APP_KEYS=get_app_keys(DATADOG_CONFIGURATION)

print("{:30s},{:5s},{:40s},{:40s},{},{}".
      format('name', 'access_role', 'handle', 'email', 'disabled', 'verified'))
for USER in USERS:
    print("{:30s},{:5s},{:40s},{:40s},{},{}".
          format(USER['name'] or "", USER['access_role'].to_str(), USER['handle'],
                 USER['email'], USER['disabled'], USER['verified']))
for API in API_KEYS:
    print(f"{API.name:30s} {API.created_by:30s} {API.is_active}")

for APP in APP_KEYS:
    print(f"{APP.name:30s}, {APP.owner:30s}, {APP.revoked}")
