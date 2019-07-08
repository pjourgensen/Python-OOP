class ConfigDict(dict):
    def __init__(self,filename):
        self._filename = filename
        super(dict,self).__init__()
        try:
            with open(self._filename,'r') as fp:
                for line in fp:
                    entry = line.split('=',1)
                    dict.__setitem__(self,entry[0],entry[1])
        except FileNotFoundError:
            with open(self._filename,'w') as fp:
                print('Created file.')

    def __setitem__(self,key,value):
        dict.__setitem__(self,key,value)
        with open(self._filename,'a') as fp:
            fp.write('\n{}={}'.format(str(key),str(value)))

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

mydict = ConfigDict('testing.txt')
mydict['a'] = 'b'
mydict['c'] = 'd'
mydict['e'] = 'f'
mydict['x']
