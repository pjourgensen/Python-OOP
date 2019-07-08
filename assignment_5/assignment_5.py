"""
This adjusts the object serialization of the prior solution, now using pickle files as opposed to text
files. User functionality remains unchanged.
"""
class ConfigDict(dict):

    config_directory = '/home/petejourgensen/Desktop/OOP/Assignments/'

    def __init__(self,filename):
        self._filename = config_directory + filename
        super(dict,self).__init__()
        try:
            with open(self._filename,'r') as fp:
                self = pickle.load(fp)
        except FileNotFoundError:
            with open(self._filename,'w') as fp:
                print("File Created")

    def __setitem__(self,key,value):
        dict.__setitem__(self,key,value)
        with open(self._filename,'w') as fp:
            pickle.dump(self,fp)

    def __getitem__(self,key):
        if not key in self:
            raise ConfigKeyError(self,key)
        return dict.__getitem__(self,key)

class ConfigKeyError(Exception):
    def __init__(self,config_dict,key):
        self.key = key
        self.key_tuple = tuple(config_dict.keys())

    def __str__(self):
        return 'key "{}" not found. Available keys: {}'.format(self.key,self.key_tuple)
