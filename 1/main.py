print("Hello Mars")
try:
    with open("mission_computer_main.log", "r", encoding="utf-8") as log_file:
        for line in log_file:
            print(line.strip())  

except FileNotFoundError:
    print('Error: 파일이 없습니다.')


except PermissionError:
    print('Error: 파일에 접근권한이 없습니다.')

except MemoryError:
    print('Error: 로그 파일의 용량이 큽니다.')


except UnicodeDecodeError:
    print('Error: 파일 인코딩 오류. 다른 인코딩을 사용해보세요.')
    with open('mission_computer_main.log', 'r', encoding='utf-8', errors='replace') as file:
        log_data = file.readlines()
