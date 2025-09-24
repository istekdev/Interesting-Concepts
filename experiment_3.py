# EXPERIMENT 3 - DEMONSTRATE ENCRYPTION

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from termcolor import colored
import time
import os

entropy = os.urandom(32)
nonce = os.urandom(12)
obj = AESGCM(entropy)

inp = input(colored("YOUR RAWTEXT: ", "blue", attrs=["bold"]))
enc = obj.encrypt(nonce, inp.encode("utf-8"), None)
print(colored(f"YOUR HEX CIPHERTEXT: {enc.hex()}", "green", attrs=["bold"]))
