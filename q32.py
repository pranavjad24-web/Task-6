import platform

if platform.system() != "Windows":
    print("Unsupported system")
    exit()

print("Environment OK")
