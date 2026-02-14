import csv
from faker import Faker
import random
import os
from datetime import datetime, timedelta

fake = Faker('es_MX')

def generate_movements(num_records=5000, output_file='movements.csv'):
    """Generates fake movement/transaction data (visits, transfers, commissary)."""
    print(f"Generating {num_records} movement records...")
    
    headers = ['movement_id', 'inmate_id', 'type', 'timestamp', 'details', 'amount']
    
    types = ['Visit', 'Commissary', 'Medical', 'Transfer', 'Court']
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        
        for _ in range(num_records):
            movement_id = fake.uuid4()
            inmate_id = fake.random_number(digits=8) # Potentially non-existent inmates, simulating dirty data
            movement_type = random.choice(types)
            timestamp = fake.date_time_between(start_date='-1y', end_date='now').isoformat()
            
            details = ""
            amount = 0.0
            
            if movement_type == 'Visit':
                details = f"Visitor: {fake.name()}"
            elif movement_type == 'Commissary':
                details = f"Item: {fake.word()}"
                amount = round(random.uniform(5, 500), 2)
            elif movement_type == 'Medical':
                details = f"Reason: {fake.sentence()}"
            elif movement_type == 'Transfer':
                details = f"To: {fake.city()}"
            
            writer.writerow([movement_id, inmate_id, movement_type, timestamp, details, amount])
            
    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    output_path = os.path.join(os.path.dirname(__file__), 'movements.csv')
    generate_movements(output_file=output_path)
