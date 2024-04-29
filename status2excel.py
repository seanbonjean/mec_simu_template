import openpyxl

def read_records_from_file(file_path):
    records = []
    with open(file_path, 'r') as file:
        record_lines = file.readlines()
        for line in record_lines:
            line = line.strip()
            if line.startswith("Record"):
                records.append(line)
            if line.startswith("Container") and not line.startswith("Container ID:"):
                records.append(line)
    return records

def create_excel(records, excel_path):
    wb = openpyxl.Workbook()
    ws = wb.active

    ws.append(["ID", "CPU", "Memory"])

    for record in records:
        if record.startswith("Record"):
            ws.append(["Record", record])
        if record.startswith("Container"):
            container_id = record.split()[1][:-1]
            total_cpu = record.split()[4][:-1]
            total_memory = record.split()[7]

            ws.append([container_id, total_cpu, total_memory])

    wb.save(excel_path)

if __name__ == "__main__":
    file_path = "C:/Users/sean-/Desktop/out/process_stats.txt"
    excel_path = "C:/Users/sean-/Desktop/out/process_stats.xlsx"
    records = read_records_from_file(file_path)
    create_excel(records, excel_path)
