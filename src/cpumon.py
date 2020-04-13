class CPUmon():

    '''
    Class that reads /proc/cpuinfo and /proc/stat files, and return 
    the actual values of the cpu info such us: cpu usge, cpu MHz and
    cpu name

    To obtain the data, execute the following sentence: 

        Hwmon().data()

    To print the data, execute the following sentence:

        CPUmon().print_data()
    '''

    def __init__(self):

        self.path = '/proc/cpuinfo'
    
    def raw_data(self):

        data_file = open(self.path, 'r')
        data = data_file.readlines()
        data_file.close()

        manipulate_data = lambda data: data.strip().replace('\t','').split(': ')
        data = list(map(manipulate_data,data))

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

        info = {'Name':'', 'CPU_usage':round(self.cpu_usage(),2),
                'cores':'', 'threads':''
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

        info['Average_MHz'] = round(mhz_sum/cont, 2)

        return info

    def print_data(self):
    
        data = self.data()
        for key in data.keys():
            print(key)
            if type(data[key])==list:
                for i in data[key]:
                    print('\t',i)
            else:
                print('\t',data[key])

# Uncomment the following sentence to get a json from the data 
#print(CPUmon().data())
# Uncomment the following sentence to print the data 
#CPUmon().print_data()
