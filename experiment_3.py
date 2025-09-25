# EXPERIMENT 3 - DEMONSTRATE

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from termcolor import colored
import time
import os

password = input(colored("WHAT WILL BE YOUR PASSWORD: ", "blue", attrs=["bold"]))
nonce = os.urandom(12)
obj = AESGCM(password.encode("utf-8"))
item = input(colored("WHAT DO YOU WANT TO ENCRYPT: ", "blue", attrs=["bold"]))
enc = obj.encrypt(nonce, item.encode("utf-8"), None)
print(colored(enc.hex(), "green", attrs=["bold"]))


