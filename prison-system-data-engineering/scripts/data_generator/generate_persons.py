import csv
import os
import random
from faker import Faker

fake = Faker('es_MX')

def generate_persons(output_dir, num_inmates=1000, num_staff=200, num_visitors=500):
    """Generates the Master Person Registry and specific role tables."""
    print("Generating Person Registry...")
    
    # 1. Master Person Table
    persons = []
    inmates = []
    staff = []
    visitors = []
    
    # Helper to create person
    def create_person(role):
        pid = fake.uuid4()
        bio_hash = fake.sha256()
        fname = fake.first_name()
        lname = fake.last_name()
        dob = fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat()
        gender = random.choice(['M', 'F'])
        persons.append([pid, fname, lname, dob, gender, bio_hash, role])
        return pid

    # Generate Inmates
    print(f"  - Generating {num_inmates} inmates...")
    blocks = ['A', 'B', 'C', 'D']
    for _ in range(num_inmates):
        pid = create_person('Inmate')
        # Inmate Specifics
        sentence_start = fake.date_between(start_date='-10y', end_date='today')
        sentence_end = fake.date_between(start_date='today', end_date='+20y')
        crime = random.choice(['Robbery', 'Fraud', 'Assault', 'Homicide', 'Drug Trafficking'])
        block = random.choice(blocks)
        cell = f"{block}-{random.randint(1, 50):03d}"
        inmates.append([pid, sentence_start, sentence_end, crime, cell, 'Active'])

    # Generate Staff
    print(f"  - Generating {num_staff} staff...")
    roles = ['Guard', 'Doctor', 'Nurse', 'Cleaner', 'Cook', 'Admin', 'Social Worker']
    for _ in range(num_staff):
        pid = create_person('Staff')
        job = random.choice(roles)
        shift = random.choice(['Morning', 'Evening', 'Night'])
        salary = round(random.uniform(8000, 45000), 2)
        staff.append([pid, job, shift, salary])

    # Generate Visitors
    print(f"  - Generating {num_visitors} visitors...")
    for _ in range(num_visitors):
        pid = create_person('Visitor')
        # Link to random inmate
        inmate_pid = random.choice(inmates)[0]
        relation = random.choice(['Mother', 'Father', 'Wife', 'Husband', 'Brother', 'Sister', 'Lawyer'])
        visitors.append([pid, inmate_pid, relation, 'Approved'])

    # Write Files
    with open(os.path.join(output_dir, 'dim_persons.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(['person_id', 'first_name', 'last_name', 'dob', 'gender', 'biometric_hash', 'type'])
        w.writerows(persons)

    with open(os.path.join(output_dir, 'dim_inmates_details.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(['person_id', 'sentence_start', 'sentence_end', 'crime', 'cell_id', 'status'])
        w.writerows(inmates)
        
    with open(os.path.join(output_dir, 'dim_staff_details.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(['person_id', 'role', 'shift', 'salary'])
        w.writerows(staff)

    with open(os.path.join(output_dir, 'dim_visitors_details.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(['person_id', 'inmate_id', 'relationship', 'status'])
        w.writerows(visitors)

    print("Person Registry Generated.")

if __name__ == "__main__":
    output_dir = os.path.dirname(__file__)
    generate_persons(output_dir)
