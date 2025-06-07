import platform
import os
import json
import ctypes


class MissionComputer:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': 0,
            'mars_base_external_temperature': 0,
            'mars_base_internal_humidity': 0,
            'mars_base_external_illuminance': 0,
            'mars_base_internal_co2': 0,
            'mars_base_internal_oxygen': 0
        }

    def get_sensor_data(self, sensor):
        sensor.set_env()
        self.env_values = sensor.get_env()

    def get_mission_computer_info(self):
        try:
            info = {
                'operating_system': platform.system(),
                'os_version': platform.version(),
                'cpu_type': platform.processor(),
                'cpu_core_count': os.cpu_count(),
                'memory_total_kb': self._get_total_memory_kb()
            }
            print(json.dumps(info, indent=2))
        except Exception as e:
            print('시스템 정보를 가져오는 중 오류 발생:', str(e))

    def get_mission_computer_load(self):
        try:
            load = {
                'cpu_load_average': 'not available on Windows',
                'memory_usage_percent': self._get_memory_usage_percent()
            }
            print(json.dumps(load, indent=2))
        except Exception as e:
            print('시스템 부하 정보를 가져오는 중 오류 발생:', str(e))

    def _get_total_memory_kb(self):
        try:
            mem_info = self._get_windows_memory_status()
            return int(mem_info['total_physical'] / 1024)
        except:
            return -1

    def _get_memory_usage_percent(self):
        try:
            mem_info = self._get_windows_memory_status()
            used = mem_info['total_physical'] - mem_info['avail_physical']
            percent = (used / mem_info['total_physical']) * 100
            return round(percent, 2)
        except:
            return -1

    def _get_windows_memory_status(self):
        class MEMORYSTATUSEX(ctypes.Structure):
            _fields_ = [
                ('dwLength', ctypes.c_ulong),
                ('dwMemoryLoad', ctypes.c_ulong),
                ('ullTotalPhys', ctypes.c_ulonglong),
                ('ullAvailPhys', ctypes.c_ulonglong),
                ('ullTotalPageFile', ctypes.c_ulonglong),
                ('ullAvailPageFile', ctypes.c_ulonglong),
                ('ullTotalVirtual', ctypes.c_ulonglong),
                ('ullAvailVirtual', ctypes.c_ulonglong),
                ('ullAvailExtendedVirtual', ctypes.c_ulonglong),
            ]

        stat = MEMORYSTATUSEX()
        stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
        ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat))

        return {
            'total_physical': stat.ullTotalPhys,
            'avail_physical': stat.ullAvailPhys
        }


class DummySensor:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': 0,
            'mars_base_external_temperature': 0,
            'mars_base_internal_humidity': 0,
            'mars_base_external_illuminance': 0,
            'mars_base_internal_co2': 0,
            'mars_base_internal_oxygen': 0
        }

    def set_env(self):
        import random
        self.env_values['mars_base_internal_temperature'] = random.uniform(18, 30)
        self.env_values['mars_base_external_temperature'] = random.uniform(0, 21)
        self.env_values['mars_base_internal_humidity'] = random.uniform(50, 60)
        self.env_values['mars_base_external_illuminance'] = random.uniform(500, 715)
        self.env_values['mars_base_internal_co2'] = random.uniform(0.02, 0.1)
        self.env_values['mars_base_internal_oxygen'] = random.uniform(4, 7)

    def get_env(self):
        return self.env_values


if __name__ == '__main__':
    runComputer = MissionComputer()
    runComputer.get_mission_computer_info()
    runComputer.get_mission_computer_load()
