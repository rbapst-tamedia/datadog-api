#!/bin/bash
export DD_HOST=${DD_HOST:-api.datadoghq.eu}

curl -s -X GET https://$DD_HOST/api/v1/integration/aws/filtering \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
