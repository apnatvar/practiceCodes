import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
print(len(res.text))
print(res.text[:100])
# print(res.raise_for_status()) # to handle error cases
file = open('test.txt','wb')
for chunk in res.iter_content(10000):
    file.write(chunk)
file.close()
