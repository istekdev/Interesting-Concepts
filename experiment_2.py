# EXPERIMENT 2 - USING TRUE ENTROPY FOR KEYGEN

from bip32utils import BIP32Key
from termcolor import colored
from mnemonic import Mnemonic
import time
import os

mn = Mnemonic("english")

def menu():
  print(colored("WELCOME TO EXPERIMENT 2", "blue", attrs=["bold"]))
  time.sleep(1)
  entropy = os.urandom(32)
  seedphrase = mn.to_mnemonic(entropy)
  seed = mn.to_seed(seedphrase, passphrase="")
  master = BIP32Key.fromEntropy(seed)
  private = master.PrivateKey()
  public = master.PublicKey()
  print(colored(f"YOUR PRIVATE KEY: {private.hex()}", "green", attrs=["bold"]))
  print(colored(f"YOUR PUBLIC KEY: {public.hex()}", "green", attrs=["bold"]))

menu()
