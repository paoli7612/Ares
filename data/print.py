import json
from termcolor import colored

with open('data/config.json') as json_file:
    data = json.load(json_file)

def print_colored(text, color):
    print(colored(text, color), end="")

print_colored("Piattaforme:\n", "blue")
for platform in data['platforms']:
    print_colored("Nome:", "yellow"), print(platform['name'])
    print_colored("Descrizione:", "yellow"), print(platform['description'])
    print_colored("Immagine:", "yellow"), print(platform['image'])

print_colored("Stanze:\n", "blue")
for room in data['rooms']:
    print_colored("Nome:", "yellow"), print(room['name'])
    print_colored("Descrizione:", "yellow"), print(room['description'])
    print_colored("Immagine:", "yellow"), print(room['image'])
    print_colored("Dispositivi montati:", "cyan"), print()
    mounts = room['mounts']
    for mount in mounts:
        print_colored("<-> Piattaforma:", "magenta"), print(mount['platform'])
        print_colored("    Nome:", "magenta"), print(mount['name'])
        print_colored("    IP:", "magenta"), print(mount['ip'])