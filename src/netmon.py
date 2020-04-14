from utils import print_dict

class NETmon():

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
        receive, transmit = remove_spaces(data[0].split('|')[1].split(' ')), remove_spaces(data[0].split('|')[2].strip().split(' '))
        
        for value in data[1:]:

            aux = value.split(':')
            name, stats = aux[0], list(map(int,remove_spaces(aux[1].strip().split(' '))))

            info[name] = dict()
            info[name]['receive'] = dict(zip(receive,stats[:8]))
            info[name]['transmit'] = dict(zip(transmit,stats[9:]))
        
        return info
    
    def print_data(self):
        print('Ctrl + C to exit the watch mode\n')
        print_dict(self.data(), indent=0)


# Uncomment the following sentence to get a json from the data 
#print(NETmon().data())
# Uncomment the following sentence to print the data 
#NETmon().print_data()