#!/bin/bash
export DD_HOST={DD_HOST:-api.datadoghq.eu}
curl -X GET "https://api.datadoghq.eu/api/v1/org" \
     -H "Accept: application/json" \
     -H "DD-API-KEY: ${DD_API_KEY}" \
     -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
