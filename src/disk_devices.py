from os import listdir

class Devices():

    def __init__(self):

        self.path = '/dev/disk/by-id'

    def data(self):

        devices = list(map(lambda data: data.split('-part')[0], listdir(self.path)))
        return list(set(devices))
    
    def print_data(self):

        for device in self.data():
            print(device)

# Uncomment the following sentence to get a json from the data 
#print(Devices().data())
# Uncomment the following sentence to print the data 
#Devices().print_data()