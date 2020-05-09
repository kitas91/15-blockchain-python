# 15-blockchain-python

Dependencies: \
PHP must be installed on your operating system (any version, 5 or 7). \
You will need to clone the hd-wallet-derive tool. \
bit Python Bitcoin library. \
web3.py Python Ethereum library. \

Libraries: \
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

