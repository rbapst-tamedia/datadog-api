#!/bin/bash
export DD_HOST=https://api.datadoghq.eu/
curl -s -X GET $DD_HOST/api/v1/monitor \
     -H "Accept: application/json" \
     -H "DD-API-KEY: ${DD_API_KEY}" \
     -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" -o - | jq ''
