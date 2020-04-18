import subprocess
import warnings

# Inspiration: https://stackoverflow.com/a/45953420
# Adapted to python3
def print_dict(dictionary, previous='', indent=0):
    '''
    Function that prints a beautifully formatted dictionary on the screen 
    '''

    if isinstance(dictionary,dict):
        for key in dictionary.keys():
            if isinstance(dictionary[key],dict):
                print('\t'*indent, key)
            print_dict(dictionary[key], previous=key, indent=indent+1)
    else:
        print('\t'*(indent-1), previous, dictionary)


def is_vm():
    """
    Function that check if Host is a VM
    """
    try:
        subprocess.check_output('dmesg |grep -i hypervisor', shell=True)
        warnings.warn("Running under VM environment")
        warnings.warn("""Information displayed by Hwmon when running
         the code in a virtual machine may be incomplete""")
        return True
    except:
        return False