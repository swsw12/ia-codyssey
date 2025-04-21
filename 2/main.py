print("Hello Mars")  

a = []  
try:
    with open("mission_computer_main.log", "r", encoding="utf-8") as log_file:
        for line in log_file:
            a.append(line) 
            print(line.strip()) 
        
        print(a)  
        a.sort(reverse=True)  
        print(a) 

except FileNotFoundError:
    print('Error: 파일이 없습니다.')

except PermissionError:
    print('Error: 파일에 접근할 권한이 없습니다.')

except MemoryError:
    print('Error: 로그 파일의 용량이 큽니다다.')

except UnicodeDecodeError:
    print('Error: 파일 인코딩 오류. 다른 인코딩을 시도하세요.')
    with open('mission_computer_main.log', 'r', encoding='utf-8', errors='replace') as file:
        log_data = file.readlines()

logs = [] 

try:
    with open("mission_computer_main.log", "r", encoding="utf-8") as log_file:
        for line in log_file:
            line = line.strip() 
            parts = line.split(",") 

            if len(parts) < 3:  
                continue

            log_entry = {
                "timestamp": parts[0], 
                "event": parts[1],     
                "message": parts[2]    
            }

            logs.append(log_entry) 

    print("🔹 변환된 데이터 (딕셔너리화):")
    for log in logs:
        print(log)

except FileNotFoundError:
    print('Error: 파일이 없습니다.')

except PermissionError:
    print('Error: 파일에 접근할 권한이 없습니다.')

except MemoryError:
    print('Error: 로그 파일의 용량이 큽니다.')

except UnicodeDecodeError:
    print('Error: 파일 인코딩 오류. 다른 인코딩을 시도하세요.')

try:
    with open("mission_computer_main.json", "w", encoding="utf-8") as file:
        file.write("[\n")

        for i, log in enumerate(logs):
            json_string = f'  {{"timestamp": "{log["timestamp"]}", "event": "{log["event"]}", "message": "{log["message"]}"}}'
            
            if i < len(logs) - 1:
                json_string += "," 
            
            file.write(json_string + "\n")

        file.write("]\n") 

    print(" JSON 파일 저장 완료")

except Exception as e:
    print(f" Error: {e}")
