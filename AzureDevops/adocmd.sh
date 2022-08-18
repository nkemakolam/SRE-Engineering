#!/bin/bash
set -xe

az devops user  list --org https://unicef.visualstudio.com/ --output table
az devops security permission namespace list --org https://unicef.visualstudio.com/ --output table