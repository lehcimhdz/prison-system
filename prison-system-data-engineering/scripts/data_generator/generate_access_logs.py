import csv
import os
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('es_MX')

def load_ids(filepath, col_index=0):
    """Helper to load IDs from existing CSVs to ensure referential integrity."""
    ids = []
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader) # toggle header
            for row in reader:
                ids.append(row[col_index])
    return ids

def generate_access_logs(output_dir, num_logs=10000):
    """Generates access logs (Who, Where, When, Why)."""
    print(f"Generating {num_logs} Access Logs...")
    
    # Load IDs
    persons = load_ids(os.path.join(output_dir, 'dim_persons.csv'))
    locations = load_ids(os.path.join(output_dir, 'dim_locations.csv'), 0)
    cells = load_ids(os.path.join(output_dir, 'dim_cells.csv'), 0)
    all_locations = locations + cells
    
    if not persons or not all_locations:
        print("Error: Missing master data. Run generate_persons.py and generate_master_data.py first.")
        return

    logs = []
    directions = ['ENTRY', 'EXIT']
    
    for _ in range(num_logs):
        log_id = fake.uuid4()
        person_id = random.choice(persons)
        location_id = random.choice(all_locations)
        timestamp = fake.date_time_between(start_date='-1mo', end_date='now').isoformat()
        direction = random.choice(directions)
        reason = fake.sentence(nb_words=4)
        
        logs.append([log_id, person_id, location_id, timestamp, direction, reason])
        
    with open(os.path.join(output_dir, 'fact_access_logs.csv'), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['log_id', 'person_id', 'location_id', 'timestamp', 'direction', 'reason'])
        writer.writerows(logs)
        
    print("Access Logs Generated.")

if __name__ == "__main__":
    output_dir = os.path.dirname(__file__)
    generate_access_logs(output_dir)
