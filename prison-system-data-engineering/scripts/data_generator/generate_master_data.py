import csv
import os
import random
from faker import Faker

fake = Faker('es_MX')

def generate_facilities(output_dir):
    """Generates facility data (Blocks, Cells, Common Areas)."""
    print("Generating Facility Master Data...")
    
    facilities = []
    blocks = ['A', 'B', 'C', 'D'] # A=Max Security, B=Medium, C=Low, D=Women
    
    # 1. Generate Cells
    cell_data = []
    for block in blocks:
        security_level = 'Max' if block == 'A' else 'Medium' if block == 'B' else 'Low'
        for cell_num in range(1, 51): # 50 cells per block
            cell_id = f"{block}-{cell_num:03d}"
            capacity = 2 if block == 'A' else 4
            cell_data.append([cell_id, block, cell_num, capacity, security_level])

    with open(os.path.join(output_dir, 'dim_cells.csv'), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['cell_id', 'block_name', 'cell_number', 'capacity', 'security_level'])
        writer.writerows(cell_data)

    # 2. Generate Common Areas
    areas = ['Cafeteria', 'Workshop', 'Library', 'Gym', 'Infirmary', 'Visitation Area', 'Admin Office', 'Kitchen']
    area_data = []
    for area in areas:
        area_id = f"AREA-{area[:3].upper()}"
        area_data.append([area_id, area, 'Common'])

    with open(os.path.join(output_dir, 'dim_locations.csv'), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['location_id', 'name', 'type'])
        writer.writerows(area_data)
        
    print(f"Facilities generated in {output_dir}")

def generate_suppliers(output_dir, num_suppliers=50):
    """Generates supplier data (Food, Maintenance, Services)."""
    print("Generating Supplier Master Data...")
    
    headers = ['supplier_id', 'company_name', 'service_type', 'contract_id', 'contract_start', 'contract_end']
    services = ['Food', 'Cleaning', 'Maintenance', 'Medical Supplies', 'Security Equipment', 'Transport']
    
    data = []
    for _ in range(num_suppliers):
        supplier_id = fake.uuid4()
        company = fake.company()
        service = random.choice(services)
        contract_id = f"CTR-{fake.random_number(digits=6)}"
        start = fake.date_between(start_date='-5y', end_date='today')
        end = fake.date_between(start_date='today', end_date='+2y')
        
        data.append([supplier_id, company, service, contract_id, start, end])
        
    with open(os.path.join(output_dir, 'dim_suppliers.csv'), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)
        
    print(f"Suppliers generated in {output_dir}")

if __name__ == "__main__":
    output_dir = os.path.dirname(__file__)
    generate_facilities(output_dir)
    generate_suppliers(output_dir)
