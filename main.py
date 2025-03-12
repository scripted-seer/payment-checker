import json
import os
from termcolor import colored
from tronpy import Tron
from tronpy.exceptions import AddressNotFound
from tronpy.providers import HTTPProvider

# --config
wal_dir = "wallets"
wal_file = os.path.join(wal_dir, "wallets.json")
tron_api = HTTPProvider("https://api.trongrid.io")

# --creat wallet addres
def create_wallet(param):
    wallets = load_wallets()
    chat_id_str = str(param)

    if chat_id_str in wallets:
        return colored("you wallet before created ... " \
               f"wallet addr: {wallets[chat_id_str]['address']}",'light_yellow')

    client = Tron(tron_api)
    wallet = client.generate_address()

    wallets[chat_id_str] = {
        'address': wallet['base58check_address'],
        'private_key': wallet['private_key']
    }
    save_wallets(wallets)

    return colored(f"created !\n" \
           f"addr: {wallet['base58check_address']}\n" \
           "send this addr just tron !!", 'black')

# --check balance and handel not found wallet
def check_balance(param):
    wallets = load_wallets()
    chat_id_str = str(param)
    
    if chat_id_str not in wallets:
        return colored("not found wallet please creat new", 'red')
    
    client = Tron(tron_api)
    address = wallets[chat_id_str]['address']

    try:
        account_info = client.get_account(address)
    except AddressNotFound:
        return colored("No transactions have been made yet. At least 1 TRON must be deposited to register the wallet on the network.", 'yellow')
    
    balance = client.get_account_balance(address)
    return colored(f"balance :\n" \
           f"trx: {balance} \n" \
           f"addr: {address}", 'green')

# --creat wallets(json) directory )
def wallets_dir():
    os.makedirs(wal_dir, exist_ok=True)

# -- load params in json wallet
def load_wallets():
    try:
        with open(wal_file, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {} 

# --save data wallet in json
def save_wallets(wallets):
    wallets_dir()
    with open(wal_file, "w") as f:
        json.dump(wallets, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    p = "your_parametr"
    print(create_wallet(p))
    print("\n" + check_balance(p))