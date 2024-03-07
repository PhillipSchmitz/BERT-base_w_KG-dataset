import csv

csv_filename = 'extracted_data/extracted_entities.csv'
csv_data = {}
with open(csv_filename, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        entity_id, label = row[0], row[1]
        csv_data[entity_id] = label

csv_filename2 = 'extracted_data/extracted_relations.csv'
csv_data2 = {}
with open(csv_filename2, 'r', encoding='utf-8') as csv_file2:
    csv_reader2 = csv.reader(csv_file2)
    next(csv_reader2)  # Skip the header row
    for row in csv_reader2:
        entity_id, label = row[0], row[1]
        csv_data2[entity_id] = label

txt_filename = 'train.txt'
resulting_labels = []  # Store resulting labels here

with open(txt_filename, 'r', encoding='utf-8') as txt_file:
    for line in txt_file:
        words = line.strip().split()
        for word in words:
            if word in csv_data:
                resulting_labels.append(csv_data[word])
            if word in csv_data2:
                resulting_labels.append(csv_data2[word])

# Create a new CSV file for resulting labels
new_csv_file = 'train_dir/train.csv'
with open(new_csv_file, 'w', newline='', encoding='utf-8') as new_csv_file:
    csv_writer = csv.writer(new_csv_file)
    csv_writer.writerow(['Subject', 'Predicate', 'Object'])

    for i in range(0, len(resulting_labels), 3):
        row_labels = resulting_labels[i:i + 3]
        csv_writer.writerow(row_labels)

print(f"Resulting labels written to {new_csv_file}")