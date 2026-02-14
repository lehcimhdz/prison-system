import csv
from faker import Faker
import random
import os

fake = Faker('es_MX')

def generate_inmates(num_records=1000, output_file='inmates.csv'):
    """Generates fake inmate data."""
    print(f"Generating {num_records} inmate records...")
    
    headers = ['inmate_id', 'first_name', 'last_name', 'dob', 'gender', 'entry_date', 'status', 'security_level', 'cell_block']
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        
        for _ in range(num_records):
            inmate_id = fake.unique.random_number(digits=8)
            first_name = fake.first_name()
            last_name = fake.last_name()
            dob = fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat()
            gender = random.choice(['M', 'F'])
            entry_date = fake.date_between(start_date='-10y', end_date='today').isoformat()
            status = random.choice(['Active', 'Released', 'Transferred'])
            security_level = random.choice(['Low', 'Medium', 'High', 'Max'])
            cell_block = f"{random.choice(['A', 'B', 'C', 'D'])}-{random.randint(1, 50)}"
            
            writer.writerow([inmate_id, first_name, last_name, dob, gender, entry_date, status, security_level, cell_block])
            
    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    output_path = os.path.join(os.path.dirname(__file__), 'inmates.csv')
    generate_inmates(output_file=output_path)
