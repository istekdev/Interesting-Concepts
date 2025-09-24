# EXPERIMENT 1: THIS IS TO TEST WHETHER KEYGEN IS SAFE WHEN DERIVED FROM A PASSWORD AND USERNAME

from temrcolor import colored
from eth_utils import keccak
import ecdsa
import time

def menu():
  print(colored("WELCOME TO EXPERIMENT NUMBER 1!", "green", attrs=["bold"]))
  time.sleep(1)
  user = input(colored("WHAT IS YOUR SELECTED USERNAME: ", "blue", attrs=["bold"]))
  psw = input(colored("WHAT IS YOUR SELECTED PASSWORD: ", "blue", attrs=["bold"]))
  timestamp = str(time.time())
  private = keccak(keccak(user.encode("utf-8") + psw.encode("utf-8") + timestamp.encode("utf-8")))
  sk = ecdsa.SigningKey.from_string(private)
  public = sk.verifying_key
  print(colored(f"YOUR PRIVATE KEY: {private.hex()}", "green", attrs=["bold"]))
  print(colored(f"YOUR PUBLIC KEY: {public.hex()}", "green", attrs=["bold"]))

menu()
  
                   
  
