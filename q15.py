import sys

print("Python Version:", sys.version)

if sys.version_info < (3, 8):
    print("Unsupported version")
    exit()
