import requests
#a = input("what do you want to spam:")
payload = {
    'content': '<@282467417722978304> where are you'
}

header = {
    'authorization':'NjIyODU5NDAyMDI1NjMxNzQ1.GIASo3.zwutNY89Zmi_40BcTLRWVk4N6JjGaUPN8gnLa4'
}
for i in range(5):
    r = requests.post('https://discord.com/api/v9/channels/907644352979927041/messages', data=payload, headers=header)

