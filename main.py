import requests, time


tokenlist = open("tokens.txt").read().splitlines()
exceptions = open("exceptions.txt").read().splitlines()

ratelimit = 0

for token in tokenlist:
    try:
        print(f"\n[+] Leave all available guilds")
        guildsIds = requests.get("https://discord.com/api/v7/users/@me/guilds", headers={'Authorization': token}).json()
        for guild in guildsIds:
            if ratelimit > 10:
                print(f"\n[+] Preventing ratelimit. Waiting for 65 seconds.")
                ratelimit = 0
                time.sleep(65)
            if guild["id"] not in exceptions:
                try:
                    requests.delete(
                        f'https://discord.com/api/v7/users/@me/guilds/'+guild['id'],
                        headers={'Authorization': token})
                    print(f"\t[!] Left this server: "+guild['name'])
                    ratelimit += 1
                except Exception as e:
                    print(f"\t[!] the following error occurred : {e}")
            else:
                print(f"[!] Did not leave {guild['name']} as it appeared in exceptions")
        print(f"\n[+] Deleted all available guilds for this token : {token}")
    except Exception as e:
        print(f"\t[!] Token : {token} | the following error occurred :{e}")
