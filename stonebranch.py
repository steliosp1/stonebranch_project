import csv

# Read customer codes from CUSTOMER_SAMPLE.csv and store them in a set
customer_codes_to_keep = set()
with open('CUSTOMER_SAMPLE.csv', 'r') as sample_file:
    sample_reader = csv.reader(sample_file)
    for row in sample_reader:
        customer_codes_to_keep.add(row[0])  # Assuming customer codes are in the first column

# Read CUSTOMER.csv, filter customer codes, and write to CUSTOMER_FILTERED.csv
with open('CUSTOMER.csv', 'r') as input_file, open('CUSTOMER_FILTERED.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Write header to the output file
    header = next(reader)
    writer.writerow(header)

    # Filter customer codes and write rows to the output file
    for row in reader:
        customer_code = row[0]  # Assuming customer codes are in the first column
        if customer_code in customer_codes_to_keep:
            writer.writerow(row)

# Read INVOICE.csv, filter customer codes, and write to INVOICE_FILTERED.csv
with open('INVOICE.csv', 'r') as input_file, open('INVOICE_FILTERED.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Write header to the output file
    header = next(reader)
    writer.writerow(header)

    # Filter customer codes and write rows to the output file
    for row in reader:
        customer_code = row[0]  # Assuming customer codes are in the first column
        if customer_code in customer_codes_to_keep:
            writer.writerow(row)

# Read INVOICE codes from INVOICE_FILTERED.csv and store them in a set
invoice_codes_to_keep = set()
with open('INVOICE_FILTERED.csv', 'r') as sample_file:
    sample_reader = csv.reader(sample_file)
    for row in sample_reader:
        invoice_codes_to_keep.add(row[1])  # Assuming INVOICE codes are in the sewcond column

# Read INVOICE_ITEM.csv, filter invoice codes, and write to INVOICE_ITEM_FILTERED.csv
with open('INVOICE_ITEM.csv', 'r') as input_file, open('INVOICE_ITEM_FILTERED.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Write header to the output file
    header = next(reader)
    writer.writerow(header)

    # Filter invoice codes and write rows to the output file
    for row in reader:
        invoice_code = row[0]  # Assuming invoice codes are in the first column
        if invoice_code in invoice_codes_to_keep:
            writer.writerow(row)