#!/bin/bash

locust_script='./anyscript.py';
python -m locust -f $locust_script;

if [[ $? -eq 0 ]];
then
    echo "This script succeeded & now closes web interface at http://localhost:8089 (accepting connections from all network interfaces)";
    echo "";
else
    echo "Failed to start web interface at http://localhost:8089 (accepting connections from all network interfaces)";
    echo "Exiting with 1...";
    exit 1;
fi