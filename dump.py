from web3 import Web3
import binascii

#RPC provider (using a free one from cloudflare)
#appending a testnet url
network = "/v1/rinkeby"
ethRpc = f"https://cloudflare-eth.com{network}"
# new free rpc I found
ethRpc = "https://rinkeby.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161"

#how many slots to get
DEPTH = 256
DEPTH = 10

#target contract. This is based off a testnet
#ethernaut contract
target = "0xb729CE0154a3Ce365df6FC721e0765159672eAa1"
# target = "0xA1CAbc7553Ca39EfFb96F4438A866470157Ad6b6"
# target = "0x331ce9F4558eb20A15Ab781A69447B8e0FE76c94"

#http provider
w3 = Web3(Web3.HTTPProvider(ethRpc))


CONNECTED  = w3.isConnected()

def HR():
    print("_" * 80)

def newLines():
    print()
    HR()
    HR()


def toString(_val):
    return binascii.hexlify(_val).decode("ascii")

def toBytes(_val):
    return str(_val)

def toInt(_val):
    return int.from_bytes(_val, byteorder='big')

def toAddress(_val):
    return binascii.hexlify(_val[12:32])

def runAll():
    for x in range(0,DEPTH):
        slot = w3.eth.getStorageAt(target,x)
        print(f"Working on slot #{x}")
        print(f"[{x}] - [bytes] {toBytes(slot)}")
        HR()
        print(f"[{x}] - [int] {toInt(slot)}")
        HR()
        print(f"[{x}] - [address] {toAddress(slot)}")
        HR()
        print(f"[{x}] - [string] {toString(slot)}")
        newLines()



if CONNECTED:
    # key = w3.eth.getStorageAt(target,1)
    # print(key)
    runAll()
