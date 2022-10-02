## ETHstorageDump


A simple python tool to help dump memory slots from targeted solidity contracts.
![Demo Screenshot](https://raw.githubusercontent.com/HackingWeb3/ETHstorageDump/main/demo.png)



## EVM storage primer

EVM points at a total of 2^256 * 32 bytes of total storage.
EVM storage maps the location of a value ```key``` by computing
```sha3(key, p)```
(p being the storage slot that acts as pointer in the mapping)

Total indexes available:
2**256
115792089237316195423570985008687907853269984665640564039457584007913129639936



By default unused slots are stored as 0. This all happens at the interface level and it is not actually storing 32 bytes of 0s on the blockchain. (Internally storage is a merkle tree and any 0 values are truncated)



This tool only pulls the first 256 slots by default. You can always add more but dumping all addresses from a
