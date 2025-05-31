import numpy as np

def load_csv(filename):
    try:
        return np.genfromtxt(filename, delimiter=',', dtype=None, skip_header=1, encoding='utf-8')
    except FileNotFoundError:
        print(f'파일을 찾을 수 없습니다: {filename}')
        raise
    except Exception as e:
        print(f'파일 읽기 중 오류가 발생했습니다: {e}')
        raise

def save_csv(filename, data):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('parts,strength\n')
            for row in data:
                f.write(f'{row[0]},{row[1]}\n')
    except Exception as e:
        print(f'파일 저장 중 오류가 발생했습니다: {e}')
        raise

def main():
    try:
        arr1 = load_csv('mars_base_main_parts-001.csv')
        arr2 = load_csv('mars_base_main_parts-002.csv')
        arr3 = load_csv('mars_base_main_parts-003.csv')

        parts = np.concatenate((arr1, arr2, arr3))

        parts_to_work_on = [row for row in parts if float(row[1]) < 50]

        save_csv('parts_to_work_on.csv', parts_to_work_on)

        print('전체 부품 개수:', len(parts))
        print('강도 < 50 부품 수:', len(parts_to_work_on))
    except Exception as e:
        print(f'프로그램 실행 중 오류가 발생했습니다: {e}')

if __name__ == '__main__':
    main()
