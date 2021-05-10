import requests

url='https://api.pwnedpasswords.com/range/'+'mypass123'

res = requests.get(url)

print(res)