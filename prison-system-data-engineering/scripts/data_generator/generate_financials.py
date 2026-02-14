import csv
import os
import random
from faker import Faker

fake = Faker('es_MX')

def load_ids(filepath, col_index=0):
    ids = []
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                ids.append(row[col_index])
    return ids

def generate_financials(output_dir, num_txns=5000):
    """Generates Wallets and Transactions."""
    print("Generating Financial Data...")
    
    # Load Inmate IDs
    inmates = load_ids(os.path.join(output_dir, 'dim_inmates_details.csv'), 0)
    
    if not inmates:
        print("Error: Missing inmate data.")
        return

    # 1. Create Wallets
    wallets = []
    wallet_map = {} # inmate_id -> wallet_id
    
    for inmate_id in inmates:
        wallet_id = f"W-{fake.uuid4()[:8]}"
        initial_balance = round(random.uniform(0, 2000), 2)
        status = 'Active'
        wallets.append([wallet_id, inmate_id, initial_balance, status])
        wallet_map[inmate_id] = wallet_id

    with open(os.path.join(output_dir, 'dim_wallets.csv'), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['wallet_id', 'inmate_id', 'current_balance', 'status'])
        writer.writerows(wallets)

    # 2. Generate Transactions
    txns = []
    types = ['DEPOSIT', 'PURCHASE', 'SALARY', 'TRANSFER']
    
    for _ in range(num_txns):
        txn_id = fake.uuid4()
        # Pick random inmate/wallet
        inmate_id = random.choice(inmates)
        wallet_id = wallet_map[inmate_id]
        
        txn_type = random.choice(types)
        amount = 0.0
        desc = ""
        
        if txn_type == 'DEPOSIT':
            amount = round(random.uniform(100, 1000), 2)
            desc = "Family Deposit"
        elif txn_type == 'PURCHASE':
            amount = round(random.uniform(-200, -5), 2) # Negative
            desc = f"Commissary: {fake.word()}"
        elif txn_type == 'SALARY':
            amount = round(random.uniform(50, 200), 2)
            desc = "Work Payment"
        elif txn_type == 'TRANSFER':
            amount = round(random.uniform(-500, -50), 2)
            desc = "Transfer to external account"

        timestamp = fake.date_time_between(start_date='-3mo', end_date='now').isoformat()
        
        txns.append([txn_id, wallet_id, amount, txn_type, timestamp, desc])
        
    with open(os.path.join(output_dir, 'fact_wallet_transactions.csv'), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['transaction_id', 'wallet_id', 'amount', 'type', 'timestamp', 'description'])
        writer.writerows(txns)

    print("Financial Data Generated.")

if __name__ == "__main__":
    output_dir = os.path.dirname(__file__)
    generate_financials(output_dir)
