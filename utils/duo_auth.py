import requests

class DuoAuth:
    def __init__(self):
        s = requests.Session()
        response = s.get("")
        print("hi")