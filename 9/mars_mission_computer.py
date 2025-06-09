import threading
import multiprocessing
import time
import os
import platform

class MissionComputer:
    def __init__(self, name='Computer'):
        self.name = name
        self.env_values = {
            'mars_base_internal_temperature': 22.5,
            'mars_base_external_temperature': -60.2,
            'mars_base_internal_humidity': 55.0,
            'mars_base_external_illuminance': 600.0,
            'mars_base_internal_co2': 0.04,
            'mars_base_internal_oxygen': 5.5
        }

    def get_mission_computer_info(self):
        for _ in range(3):  # 3번 출력
            print(f"[{self.name}] System Info:")
            print(f"  OS: {platform.system()}")
            print(f"  Version: {platform.version()}")
            print(f"  CPU Type: {platform.processor()}")
            print(f"  CPU Core Count: {os.cpu_count()}")
            print('-' * 40)
            time.sleep(20)

    def get_mission_computer_load(self):
        for _ in range(3):
            try:
                load = os.getloadavg()  # Unix 전용
                print(f"[{self.name}] Load Average (1, 5, 15min): {load}")
            except AttributeError:
                print(f"[{self.name}] Load Average: Not available on this OS")
            print('-' * 40)
            time.sleep(20)

    def get_sensor_data(self):
        for _ in range(3):
            print(f"[{self.name}] Sensor Values:")
            for key, value in self.env_values.items():
                print(f"  {key}: {value}")
            print('-' * 40)
            time.sleep(20)



def run_threads():
    runComputer = MissionComputer('Threaded')

    t1 = threading.Thread(target=runComputer.get_mission_computer_info)
    t2 = threading.Thread(target=runComputer.get_mission_computer_load)
    t3 = threading.Thread(target=runComputer.get_sensor_data)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


def run_instance(name):
    computer = MissionComputer(name)
    computer.get_mission_computer_info()
    computer.get_mission_computer_load()
    computer.get_sensor_data()

def run_processes():
    p1 = multiprocessing.Process(target=run_instance, args=('Process1',))
    p2 = multiprocessing.Process(target=run_instance, args=('Process2',))
    p3 = multiprocessing.Process(target=run_instance, args=('Process3',))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

# -----------------------------------------------
if __name__ == '__main__':
    print('1단계 멀티 쓰레드 실행 중\n')
    run_threads()

    print('2단계 멀티 프로세스 실행 중\n')
    run_processes()
