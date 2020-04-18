# Script for python 3

import os
from hwmon.utils import is_vm, print_dict

class Hwmon():

    def __init__(self):
        is_vm()

    class HW():

        def __init__(self):
            self.master_path = '/sys/class/hwmon'

        def extract_data(self, sub_folder_path, file_):

            if os.path.exists(os.path.join(sub_folder_path, file_.split('_')[0] + '_label')):

                label_name = file_.split('_')[0] + '_label'

                file = open(os.path.join(sub_folder_path, label_name), 'r')
                label_name = file.read().strip()
                file.close()
                file = open(os.path.join(sub_folder_path, file_), 'r')
                value = file.read().strip()
                file.close()

            else:

                label_name = file_.split('_')[0]
                file = open(os.path.join(sub_folder_path, file_), 'r')
                value = file.read().strip()
                file.close()

            # See https://www.kernel.org/doc/Documentation/hwmon/sysfs-interface
            if file_.lower().startswith('in'):
                return label_name, str(int(value) / 1000) + ' v'
            elif file_.lower().startswith('fan'):
                return label_name, value + ' RPM'
            elif file_.lower().startswith('pwm'):
                return label_name, str(int(value) / 255) + ' PWM (%)'
            elif file_.lower().startswith('temp'):
                return label_name, str(int(value) / 1000) + ' C'
            elif file_.lower().startswith('curr'):
                return label_name, str(int(value) / 1000) + ' a'
            elif file_.lower().startswith('power'):
                return label_name, str(int(value) / 1000000) + ' w'

        def data(self):

            data = dict()

            folders = os.listdir(self.master_path)

            for folder in folders:

                sub_folder_path = os.path.join(self.master_path, folder)

                files = os.listdir(sub_folder_path)

                name = open(os.path.join(sub_folder_path, 'name'), 'r')
                name_key = name.read().strip()
                name.close()

                data[name_key] = dict()

                for file_ in files:

                    try:

                        if '_input' in file_:
                            label_name, value = self.extract_data(sub_folder_path, file_)
                            data[name_key][label_name] = value

                        if '_average' in file_:
                            label_name, value = self.extract_data(sub_folder_path, file_)
                            data[name_key][label_name] = value

                    except Exception:
                        pass

            return data

        def print_data(self):
            print_dict(self.data(), indent=0)

    class CPU():

        def __init__(self):

            self.path = '/proc/cpuinfo'

        def raw_data(self):

            data_file = open(self.path, 'r')
            data = data_file.readlines()
            data_file.close()

            manipulate_data = lambda data: data.strip().replace('\t', '').split(': ')
            data = list(map(manipulate_data, data))

            return data

        # See https://rosettacode.org/wiki/Linux_CPU_utilization#Python
        def cpu_usage(self):

            last_idle = last_total = 0

            with open('/proc/stat') as f:
                fields = [float(column) for column in f.readline().strip().split()[1:]]

            idle, total = fields[3], sum(fields)
            idle_delta, total_delta = idle - last_idle, total - last_total
            last_idle, last_total = idle, total
            utilisation = 100.0 * (1.0 - idle_delta / total_delta)

            return utilisation

        def data(self):

            data = self.raw_data()
            mhz_sum, cont = 0, 0

            info = {'Name': '', 'CPU_usage': round(self.cpu_usage(), 2),
                    'cores': '', 'threads': ''
                    }

            for line in data:

                if len(line) > 1:
                    if line[0] == 'model name' and info['Name'] == '':
                        info['Name'] = line[1]
                    elif line[0] == 'cpu MHz':
                        mhz_sum = mhz_sum + float(line[1])
                        cont = cont + 1
                    elif line[0] == 'siblings' and info['threads'] == '':
                        info['threads'] = line[1]
                    elif line[0] == 'cpu cores' and info['cores'] == '':
                        info['cores'] = line[1]
                    else:
                        pass

            info['Average_MHz'] = round(mhz_sum / cont, 2)

            return info

        def print_data(self):
            print_dict(self.data(), indent=0)

    class MEM():

        def __init__(self):

            self.path = '/proc/meminfo'

        def data(self):

            data_file = open(self.path, 'r')
            data = data_file.readlines()
            data_file.close()

            manipulate_data = lambda data: data.strip().replace('\t', '').replace(' ', '').replace('kB', '').split(':')
            data = list(map(manipulate_data, data))

            for i in range(len(data)):
                data[i][1] = self.convert_to_mb(float(data[i][1]))

            return dict(data)

        def print_data(self):
            print_dict(self.data(), indent=0)

        def convert_to_mb(self, byte_size):
            """
                ref: https://gist.github.com/Pobux/0c474672b3acd4473d459d3219675ad8
                A bit is the smallest unit, it's either 0 or 1
                1 byte = 1 octet = 8 bits
                1 kB = 1 kilobyte = 1000 bytes = 10^3 bytes
                1 KiB = 1 kibibyte = 1024 bytes = 2^10 bytes
                1 KB = 1 kibibyte OR kilobyte ~= 1024 bytes ~= 2^10 bytes (it usually means 1024 bytes but sometimes it's 1000... ask the sysadmin ;) )
                1 kb = 1 kilobits = 1000 bits (this notation should not be used, as it is very confusing)
                1 ko = 1 kilooctet = 1000 octets = 1000 bytes = 1 kB
                Also Kb seems to be a mix of KB and kb, again it depends on context.
                In linux, a byte (B) is composed by a sequence of bits (b). One byte has 256 possible values.
                More info : http://www.linfo.org/byte.html
                """
            BASE_SIZE = 1024.00
            MEASURE = ["B", "KB", "MB", "GB", "TB", "PB"]

            def _fix_size(size, size_index):
                if not size:
                    return "0"
                elif size_index == 0:
                    return str(size)
                else:
                    return "{:.3f}".format(size)

            current_size = byte_size
            size_index = 0

            while current_size >= BASE_SIZE and len(MEASURE) != size_index:
                current_size = current_size / BASE_SIZE
                size_index = size_index + 1

            size_to_return = _fix_size(current_size, size_index)
            measure = MEASURE[size_index]
            return size_to_return + measure

    class NET():

        def __init__(self):

            self.path = '/proc/net/dev'

        def data(self):

            def remove_spaces(list_data):

                while '' in list_data:
                    list_data.remove('')

                return list_data

            data_file = open(self.path, 'r')
            data = data_file.readlines()[1:]
            data_file.close()

            info = dict()
            receive, transmit = remove_spaces(data[0].split('|')[1].split(' ')), remove_spaces(
                data[0].split('|')[2].strip().split(' '))

            for value in data[1:]:
                aux = value.split(':')
                name, stats = aux[0], list(map(int, remove_spaces(aux[1].strip().split(' '))))

                info[name] = dict()
                info[name]['receive'] = dict(zip(receive, stats[:8]))
                info[name]['transmit'] = dict(zip(transmit, stats[9:]))

            return info

        def print_data(self):
            print_dict(self.data(), indent=0)

    class USB():

        def __init__(self):
            self.path = '/dev/input/by-id'

        def data(self):
            devices = list(map(lambda data: data.split('-event')[0], os.listdir(self.path)))
            return list(set(devices))

        def print_data(self):
            for device in self.data():
                print(device)

    class DISK():

        def __init__(self):
            self.path = '/dev/disk/by-id'

        def data(self):
            devices = list(map(lambda data: data.split('-part')[0], os.listdir(self.path)))
            return list(set(devices))

        def print_data(self):
            for device in self.data():
                print(device)
