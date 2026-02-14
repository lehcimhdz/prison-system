import csv
from faker import Faker
import random
import os

fake = Faker('es_MX')

def generate_staff(num_records=200, output_file='staff.csv'):
    """Generates fake staff data."""
    print(f"Generating {num_records} staff records...")
    
    headers = ['staff_id', 'first_name', 'last_name', 'role', 'shift', 'hire_date', 'salary']
    
    roles = ['Guard', 'Warden', 'Nurse', 'Doctor', 'Janitor', 'Cook', 'Admin']
    shifts = ['Morning', 'Evening', 'Night']
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        
        for _ in range(num_records):
            staff_id = fake.unique.random_number(digits=6)
            first_name = fake.first_name()
            last_name = fake.last_name()
            role = random.choice(roles)
            shift = random.choice(shifts)
            hire_date = fake.date_between(start_date='-20y', end_date='today').isoformat()
            salary = round(random.uniform(10000, 50000), 2)
            
            writer.writerow([staff_id, first_name, last_name, role, shift, hire_date, salary])
            
    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    output_path = os.path.join(os.path.dirname(__file__), 'staff.csv')
    generate_staff(output_file=output_path)
