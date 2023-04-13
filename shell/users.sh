#!/bin/bash
# Get all users, api_keys, application_keys and org info from Datadog
# NOTICE: creates users-PTS.json, users-ADM.json, api_keys-PTS.json, ... on local dir
# Prerequists:
# export DD_API_KEY_ADM=an_api_key_on_Datadog_ADM_account
# export DD_APP_KEY_ADM=an_app_key_on_Datadog_ADM_account
# export DD_API_KEY_PTS=an_api_key_on_Datadog_PTS_account
# export DD_APP_KEY_PTS=an_app_key_on_Datadog_PTS_account

export DD_HOST=https://api.datadoghq.eu/
for account in PTS ADM; do
    DD_API_KEY=$(eval echo '$'DD_API_KEY_$account)
    DD_APP_KEY=$(eval echo '$'DD_APP_KEY_$account)
    # Get users
    curl -s -X GET $DD_HOST/api/v1/users \
         -H "Accept: application/json" \
         -H "DD-API-KEY: ${DD_API_KEY}" \
         -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" -o - | jq '' > users-$account.json

    # Get API keys
    curl -s -X GET $DD_HOST/api/v2/api_keys \
         -H "Accept: application/json" \
         -H "DD-API-KEY: ${DD_API_KEY}" \
         -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" -o - | jq '' > api_keys-$account.json

    # Get APP keys
    curl -s -X GET $DD_HOST/api/v2/application_keys \
         -H "Accept: application/json" \
         -H "DD-API-KEY: ${DD_API_KEY}" \
         -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" -o - | jq '' > application_keys-$account.json

    # Get Organization info
    curl -s -X GET $DD_HOST/api/v1/org \
         -H "Accept: application/json" \
         -H "DD-API-KEY: ${DD_API_KEY}" \
         -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" -o - | jq '' > orgs-$account.json
done
