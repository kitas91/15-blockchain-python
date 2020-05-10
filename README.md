# 15-blockchain-python

![Blockchain with Python](newtons-coin-cradle.jpg)

Dependencies: 

PHP must be installed on your operating system (any version, 5 or 7). \
You will need to clone the hd-wallet-derive tool. \
bit Python Bitcoin library. \
web3.py Python Ethereum library. 

Libraries: 

import pandas as pd \
import numpy as np \
import subprocess \
import json \
import os \
from dotenv import load_dotenv \
from constants import * \
from web3 import Web3 \
from bit import wif_to_key, PrivateKeyTestnet \
from bit import PrivateKeyTestnet \
from bit.network import NetworkAPI \
from eth_account import Account \
from web3.middleware import geth_poa_middleware \
from web3.gas_strategies.time_based import \ 
medium_gas_price_strategy \ 

load_dotenv()

Step1:
Create a project directory called wallet and cd into it.

Create a symlink called derive for the hd-wallet-derive/hd-wallet-derive.php script into the top level project directory like so: ln -s hd-wallet-derive/hd-wallet-derive.php derive \
This will clean up the command needed to run the script in our code, as we can call ./derive instead of ./hd-wallet-derive/hd-wallet-derive.php.  \
Create a file called wallet.py -- this will be your universal wallet script.

Step2:  \
In a separate file, constants.py, set the following constants:
BTC = 'btc' \
ETH = 'eth' \
BTCTEST = 'btc-test' \

Step3:  \
Linking the transaction signing libraries

def derive_wallets (mnemonic, coin, number):
class coin:
def priv_key_to_account (coin, priv_key):
def create_tx(coin, account, to, amount):
def send_tx(coin,account, recipient, amount):

Step4: \
Send some transactions!

![terminal](terminal transaction)

![BTC Transaction](BTC transaction)

![ETH Transaction](ETH transaction)






