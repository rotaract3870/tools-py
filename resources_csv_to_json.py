import csv
import json

def execute():
    file_name = input('Resources file (resources.csv): ')
    if not file_name:
        file_name = 'resources.csv'

    print("Converting to JSON data...")

    data = []
    category_idx = 1
    category_data = {}
    
    with open(file_name, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            category = row.pop('category')
            if category not in category_data:
                category_data[category] = category_idx
                category_idx = category_idx + 1
            if not row.get('link'):
                row['link'] = '#'
            category_id = category_data[category]
            data.append({**row, 'category_id': category_id})

    output_file_name = input('Output resources file (resources.json): ')
    if not output_file_name:
        output_file_name = 'resources.json'
    
    json_data = {
        'category_data': [{'id': v, 'name': k} for k, v in category_data.items()],
        'data': data,
    }

    with open(output_file_name, 'w') as json_file:
        json_file.write(json.dumps(json_data, indent=4))

    print(f"Saved to {output_file_name}...")

if __name__ == '__main__':
    execute()
