# 1. Mars_Base_Inventory_List.csv 내용을 읽어 출력
def read_and_print_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print("파일 내용:")
    for line in lines:
        print(line.strip())
    return lines

# 2. 파일 내용을 리스트로 변환
def parse_to_list(lines):
    inventory = []
    header = lines[0].strip().split(",")
    for line in lines[1:]:
        parts = line.strip().split(",")
        if len(parts) == 5:  
            name, weight, gravity, strength, flammability = parts
            try:
                flammability = float(flammability) 
            except ValueError:
                continue 
            inventory.append([name, weight, gravity, strength, flammability])
    return inventory

# 3. 인화성이 높은 순으로 정렬
def sort_by_flammability(inventory):
    return sorted(inventory, key=lambda x: x[4], reverse=True)

# 4. 인화성 지수 0.7 이상 필터링
def filter_dangerous_items(inventory):
    dangerous_items = [item for item in inventory if item[4] >= 0.7]
    print("\n인화성 지수 0.7 이상 목록:")
    for item in dangerous_items:
        print(item)
    return dangerous_items

# 5. 위험 목록 CSV 저장
def save_to_csv(filename, header, data):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(",".join(header) + "\n") 
        for item in data:
            f.write(",".join(map(str, item)) + "\n")
    print(f"{filename} 파일로 저장 완료!")

filename = "Mars_Base_Inventory_List.csv"
lines = read_and_print_file(filename) 
print("@")
inventory = parse_to_list(lines) 
sorted_inventory = sort_by_flammability(inventory)  
dangerous_items = filter_dangerous_items(sorted_inventory) 
print("@")
# 5. 위험 목록 저장
output_filename = "Mars_Base_Inventory_danger.csv"
save_to_csv(output_filename, lines[0].strip().split(","), dangerous_items)
