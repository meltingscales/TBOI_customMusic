import sys
import os
import time

try:
    import settings
except ImportError as e:
    print(e)
    input("Couldn't import settings module.")


def wait(t=60 * 10, m="Waiting 'cuz debug mode is on."):
    print(m)
    time.sleep(t)


try:
    import requests
except:
    wait(m="'requests' library not found.\nTry 'pip install requests'?")

if isinstance(sys.argv, list) and len(sys.argv) > 1:

    args = ""
    settings.message = {}

    for i in range(1, len(sys.argv)):
        args += sys.argv[i].replace(' ', '')

    print("Args: ")
    print(args)

    argsList = args.split(',')

    for arg in argsList:
        argDict = arg.split('=')
        settings.message[argDict[0]] = argDict[1]

print(f'sys.argv: {repr(sys.argv)}')
print(f'Script directory: {settings.script_path}')


def sendMessage(message, host=settings.host, port=settings.port):
    r = requests.post(f'http://{host}:{str(port)}/post/', data=message)

    print(f"Sent '{message}' to '{host}:{str(port)}'")

    print(r.status_code)

    r.close()


if __name__ == '__main__':
    sendMessage(settings.message)

    sys.exit(1)
