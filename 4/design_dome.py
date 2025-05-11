import math


densities = {
    '유리': 2.4,
    '알루미늄': 2.7,
    '탄소강': 7.85
}


mars_gravity_ratio = 0.38


global_area = 0
global_weight = 0

def sphere_area(diameter, material='유리', thickness=1):
    radius = diameter / 2
    area = 2 * math.pi * (radius ** 2)
    density = densities.get(material, 2.4)
    volume = area * thickness
    weight = density * volume
    weight_kg = (weight / 1000) * mars_gravity_ratio

    global global_area
    global global_weight
    global_area = area
    global_weight = weight_kg

    return area, weight_kg

def print_result(diameter, material, thickness, area, weight):
    print(f'재질 =⇒ {material}, 지름 =⇒ {diameter:03}, 두께 =⇒ {thickness:03}, 면적 =⇒ {area:.3f}, 무게 =⇒ {weight:.3f} kg')

def main():
    while True:
        try:
            diameter = float(input('지름을 입력하세요 (0을 입력하면 종료): '))
            if diameter == 0:
                print('프로그램을 종료합니다.')
                break
            material = input('재질을 입력하세요 (유리, 알루미늄, 탄소강): ')
            thickness = float(input('두께를 입력하세요 (단위: cm): '))

            if diameter <= 0 or thickness <= 0:
                print('지름과 두께는 0보다 커야 합니다. 다시 입력하세요요')
                continue

            area, weight = sphere_area(diameter * 100, material, thickness)
            print_result(diameter, material, thickness, area, weight)
        except ValueError:
            print('잘못된 입력입니다. 다시 시도해주세요.')

if __name__ == '__main__':
    main()
