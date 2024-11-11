#!/bin/bash

# Define the endpoints
endpoints=(
    "saucelabs.com"
    "api.us-west-1.saucelabs.com/rest/v1"
    "maki1932.miso.saucelabs.com"
)

# Loop through each endpoint and check connectivity
for endpoint in "${endpoints[@]}"; do
    response=$(curl --head --silent --write-out "%{http_code}" --output /dev/null "https://$endpoint")
    if [ "$response" -eq 200 ]; then
        echo -e "SUCCESS: $endpoint"
    else
        echo -e "FAILED: $endpoint"
    fi
done
