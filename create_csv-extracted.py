import json
import csv

with open('entities.json', 'r') as f:
    data = json.load(f)
csv_filename = 'extracted_data/extracted_entities.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Entity ID', 'Label', 'Description', 'Wiki link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i, (entity_id, entity_info) in enumerate(data.items()):
        label = entity_info.get('label', '')
        description = entity_info.get('description', '')
        wiki = entity_info.get('wiki', '')

        writer.writerow({
            'Entity ID': entity_id,
            'Label': label,
            'Description': description,
            'Wiki link': wiki
        })
print(f"Data has been saved to {csv_filename}")


with open('relations.json', 'r') as f2:
    data_rel = json.load(f2)
csv_rel_filename = 'extracted_data/extracted_relations.csv'
with open(csv_rel_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Relation ID', 'Label', 'Description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i, (entity_id, entity_info) in enumerate(data_rel.items()):
        label = entity_info.get('label', '')
        description = entity_info.get('description', '')

        writer.writerow({
            'Relation ID': entity_id,
            'Label': label,
            'Description': description,
        })
print(f"Data has been saved to {csv_rel_filename}")