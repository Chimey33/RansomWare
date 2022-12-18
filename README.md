# RansomWare

Basic ransomware software that encrypts some user data and propagates. Each step undertaken will produce some output in the same directory as the folder the repo is contained in (encrypted files, key files etc) that can be observed by the user 
## Package requirements
- Requires pyton 3.9.2
- pycryptodome
- glob
- base64
- os

## Instructions for running


Run the following commands in order

- `python3 ransomware.py`
- `python3 key_recovery.py`
- `python3 file_recovery.py`

## To restart

- `rm key.bin key.txt ransomprvkey.pem ransomware.py`
- `mv ransomware_propagation.py ransomware.py`


