from json import dumps
from urllib.request import Request
from urllib.request import urlopen

request = Request(
    url="http://127.0.0.1:21313/api/push",
    method="POST",
    headers={
        "Content-Type": "application/json",
    },
    data=dumps({
        "name": input("name="),
        "score": int(input("score="))
    }).encode("utf-8")
)

resp = urlopen(request)
print(resp)
