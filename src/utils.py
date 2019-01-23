import random
import re
from ipaddress import IPv4Network
from json import load, dump


class SecretFile:
    def __init__(self, path):
        self.path = path
        try:
            with open(path) as f:
                self.json = load(f)
        except FileNotFoundError:
            self.json = {}

    def __setitem__(self, key, value):
        self.json[key] = value
        with open(self.path, "w+") as f:
            dump(self.json, f)

    @staticmethod
    def _generate_secret():
        return ''.join(
            [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for _ in range(50)])

    def __getitem__(self, item):
        if item not in self.json:
            self[item] = self._generate_secret()
        return self.json[item]
