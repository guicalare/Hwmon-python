import subprocess
import warnings

def print_dict(dictionary, previous='', indent=0):

    """
    Description:
        Function that prints out a dictionary beautifully.
    
    Inspiration:
        https://stackoverflow.com/a/45953420

    Args:
        dictionary (dict): Simple or composite Python dictionary to be printed on screen
        previous (str, optional): Support variable used by the function when working in a recursive way.
                                  To avoid performance problems, it is recommended to leave the variable
                                  at its default value.. Defaults to ''.
        indent (int, optional): Total tabs used by the function to print a dictionary on the screen.
                                Defaults to 0.
    
    Return:
        None
    """    

    if isinstance(dictionary,dict):
        for key in dictionary.keys():
            if isinstance(dictionary[key],dict):
                print('\t'*indent, key)
            print_dict(dictionary[key], previous=key, indent=indent+1)
    else:
        print('\t'*(indent-1), previous, dictionary)


def is_vm():

    """
    Description:
        Function that check if Host is a VM
    
    Args:
        None

    Returns:
        [bool]: True if the Host is a VM and False if not
    """    

    try:
        subprocess.check_output('dmesg |grep -i hypervisor', shell=True)
        warnings.warn("Running under VM environment")
        warnings.warn("Information displayed by Hwmon when running the code in a virtual machine may be incomplete")
        return True
    except:
        return False