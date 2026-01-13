#!/bin/bash
# UniBee Python SDK Generator
# This script regenerates the SDK from the latest OpenAPI spec

rm -rf *.py
rm -rf openapi_client
rm -rf docs/*.md
java -jar openapi-generator-cli.jar generate \
-i https://api.unibee.top/api.sdk.generator.json \
-g python \
-o . \
--git-repo-id unibee-python-client \
--git-user-id UniBee-Billing \
-c config.yaml \
--package-name openapi_client