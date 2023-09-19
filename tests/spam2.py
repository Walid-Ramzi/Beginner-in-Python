import requests
import json

def retrive(channelid):

    header = {
        'authorization':'NjIyODU5NDAyMDI1NjMxNzQ1.GIASo3.zwutNY89Zmi_40BcTLRWVk4N6JjGaUPN8gnLa4'
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=header)
    s = json.loads(r.text)
    for i in s:
        print(i['content'], '\n')
retrive('907644352979927041')