import threading
import sys
import random
import string
import requests
import subprocess
import time
from proxy_requests import ProxyRequests

token = ""

def id_generator(size, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

def gen():
        try:
                while True:
                        code = id_generator(16)
                        codechecker(code)
                if gend > amount:
                        return
        except Exception as e:
                return

def codechecker(code):
        try:
                r = ProxyRequests("https://discordapp.com/api/v6/entitlements/gift-codes/$%s?with_application=false&with_subscription_plan=true" % (code))
                r.get()
                JsonResponse = r.get_json()
                Response = JsonResponse["message"]
                if Response == "Unknown Gift Code":
                        print(f"\x1b[31;1mInvaild Code {code}\n")
                        return
                if Response == "You are being rate limited.":
                        return
                        print("\x1b[31;1mYou Are Being Rate Limited.")
                else:
                        print(f"\x1b[31;1mFound Working Code {code} Site Response:{Response}\n")
                        response = ProxyRequests("https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem", json={"channel_id":str(message.channel.id)}, headers={'authorization':token})
                        redeemedcode = (response.text)
                        return
        except Exception as e:
                print(e)
                return

try:
        threads = int(sys.argv[1])
        for x in range(threads):
                threading.Thread(target=gen).start()
except Exception as e:
        print(f"{sys.argv[0]} [threads]")
