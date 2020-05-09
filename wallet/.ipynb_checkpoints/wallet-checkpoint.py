import pandas as pd
import numpy as np
import subprocess
import json
import os
from dotenv import load_dotenv
from constants import *
from web3 import Web3
from bit import wif_to_key, PrivateKeyTestnet
from bit.network import NetworkAPI
from eth_account import Account
from web3.middleware import geth_poa_middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy



load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer =0)
w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

mnemonic = os.getenv('MNEMONIC')

def derive_wallets (mnemonic, coin, number):
    command = f"./derive -g --mnemonic ='{mnemonic}' --coin='{coin}' --numderive='{number}' --cols=index,path,address,privkey,pubkey,pubkeyhash,xprv,xpub --format=json"
    #suprocess.PIPE redirects the command output so that we can use it. 
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) =p.communicate()
    p_status = p.wait()
    keys = json.loads(output)
    return keys


class coin:
    BTC = 'btc'
    ETH = 'eth'
    BTCTEST = 'btc-test'
    

def priv_key_to_account (coin, privkey):
    if coin == ETH:
        return Account.privateKeyToAccount(privkey)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(privkey)
    
    
def create_tx(coin, account, to, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to": to, "value": amount}
        )
        return {
            "from": account.address,
            "to": to,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address),
        }
    elif coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])



def send_tx(coin,account, recipient, amount):
    tx = create_tx(coin,account,recipient,amount)
    signed_tx = account.sign_transaction(tx)
    if coin == ETH:
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return result.hex()
    elif coin == BTCTEST:
        return NetworkAPI.broadcast_tx_testnet(signed_tx)
