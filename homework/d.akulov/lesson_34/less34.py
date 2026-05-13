# никаких идей написать что то свое не появилось,
# куда то что то жмали как то все работает ¯\(ツ)/¯
# может дальше станет чуть яснее)
from datetime import datetime
from time import sleep
import requests

while True:
    requests.get("https://www.google.com/")
    print(datetime.now())
    sleep(2)
