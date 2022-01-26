import os
with open("hosts.txt") as file:
    dump = file.read()
    dump = dump.splitlines()
    for ip in dump:
        print(ip) # print(ip, end="") também é uma possibilidade
        os.system(f"ping {ip}")