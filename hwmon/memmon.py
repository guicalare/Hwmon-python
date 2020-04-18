from utils import print_dict

class MEMmon():

    '''
    Class that reads /proc/meminfo and return 
    the actual values of the memory info

    To obtain the data, execute the following sentence: 

        MEMmon().data()

    To print the data, execute the following sentence:

        MEMmon().print_data()
    '''

    def __init__(self):

        self.path = '/proc/meminfo'

    def data(self):

        data_file = open(self.path, 'r')
        data = data_file.readlines()
        data_file.close()

        manipulate_data = lambda data: data.strip().replace('\t','').replace(' ','').replace('kB','').split(':')
        data = list(map(manipulate_data,data))
        
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
