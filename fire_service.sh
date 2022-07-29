#! /bin/sh

echo "** Running the Java Services **\n"

# Sample Service Running, Change it with yours
cd sample_java_services/
/bin/bash ./start.sh

# Service has been Fired, Let Display & Check & Run the Python Script Forever
echo "** Checking If Pixopa Service is running ... **\n"
ps aux | grep java

# Change Directory to Parent where Python Script is Present
cd ..
python processChecker.py