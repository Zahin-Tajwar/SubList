import requests
import time
import urllib3
import sys
import colorama
from colorama import*
colorama.init()

def banner():
    print(Fore.YELLOW + r'''

  _________    ___.   .____    .__          __               ____  _______   
 /   _____/__ _\_ |__ |    |   |__| _______/  |_            /_   | \   _  \  
 \_____  \|  |  \ __ \|    |   |  |/  ___/\   __\   ______   |   | /  /_\  \ 
 /        \  |  / \_\ \    |___|  |\___ \  |  |    /_____/   |   | \  \_/   \
/_______  /____/|___  /_______ \__/____  > |__|              |___| /\_____  /
        \/          \/        \/       \/                          \/     \/ 

  ''')
    print(Fore.YELLOW+"Find out and List all the Subdomains of a domain.")
    time.sleep(1)

def parse_url(url):
    try:
        host = urllib3.util.url.parse_url(url).host
    except Exception as e:
        print(Fore.RED+'[*] Invalid domain, try again..')
        sys.exit(1)
    return host

def write_subs_to_file(subdomain, output_file):
    with open(output_file, 'a') as fp:
        fp.write(subdomain + '\n')
        fp.close()

def main():
    banner()
    subdomains = []

    target = parse_url(input("Target Domain:"))
    output = "SubList.txt"

    req = requests.get(f'https://crt.sh/?q=%.{target}&output=json')

    if req.status_code != 200:
        print('[*] Information not available!')
        sys.exit(1)

    for (key,value) in enumerate(req.json()):
        subdomains.append(value['name_value'])

    print(f"\n****** TARGET: {target} ******\n")


    subs = sorted(set(subdomains))

    for s in subs:
        print(f'[*] {s}\n')
        if output is not None:
            write_subs_to_file(s, output)

    print("\n\n SubListing is complete, ALMOST all subdomains have been found.")


if __name__=='__main__':
    main()