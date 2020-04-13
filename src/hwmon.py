# Script for python 3

import os
import timeit

class Hwmon():

    '''
    Class that reads Hwmon data (sys/class/hwmon) and only return
    the actual values of the sensors.

    To obtain the data, execute the following sentence: 

        Hwmon().data()

    To print the data, execute the following sentence:

        Hwmon().print_data()
    '''

    def __init__(self):

        self.master_path = '/sys/class/hwmon'

    def extract_data(self, sub_folder_path, file_):

        if os.path.exists(os.path.join(sub_folder_path,file_.split('_')[0]+'_label')):

            label_name = file_.split('_')[0]+'_label'

            file = open(os.path.join(sub_folder_path,label_name), 'r')
            label_name = file.read().strip()
            file.close()
            file = open(os.path.join(sub_folder_path,file_), 'r')
            value = file.read().strip()
            file.close()   

        else:

            label_name = file_.split('_')[0]
            file = open(os.path.join(sub_folder_path,file_), 'r')
            value = file.read().strip()
            file.close()
        
        # See https://www.kernel.org/doc/Documentation/hwmon/sysfs-interface
        if file_.lower().startswith('in'):
            return label_name, str(int(value)/1000) + ' v'
        elif file_.lower().startswith('fan'):
            return label_name, value + ' RPM'
        elif file_.lower().startswith('pwm'):
            return label_name, str(int(value)/255) + ' PWM (%)'
        elif file_.lower().startswith('temp'):
            return label_name, str(int(value)/1000) + ' ºC'
        elif file_.lower().startswith('curr'):
            return label_name, str(int(value)/1000) + ' a'
        elif file_.lower().startswith('power'):
            return label_name, str(int(value)/1000000) + ' w'

    def data(self):

        data = dict()

        folders = os.listdir(self.master_path)

        for folder in folders:
                
            
            sub_folder_path = os.path.join(self.master_path,folder)

            files = os.listdir(sub_folder_path)

            name = open(os.path.join(sub_folder_path,'name'), 'r')
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

        data = self.data()

        for key in data.keys():
            print(key)
            for sub_key in data[key].keys():
                print('\t',' ',sub_key,' ', data[key][sub_key])

# Uncomment the following sentence to get a json from the data 
#print(Hwmon().data())
# Uncomment the following sentence to print the data 
#Hwmon().print_data()
