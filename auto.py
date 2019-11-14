#!/usr/bin/python
import readline, rlcompleter
CMD = ["status", "start", "stop", "restart", "reload" ,"exit"]

def completer(text, state):
    options = [cmd for cmd in CMD if cmd.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

readline.parse_and_bind("bind ^I rl_complete")
readline.set_completer(completer)

while True:
    cmd = input("Please select one from the list above: ")
    if cmd == 'exit':
        break
    print(cmd)