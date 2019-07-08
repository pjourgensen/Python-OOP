"""
This is practice with both inheritance and polymorphism. ConfigDict inherits from the python built-in
dict class to allow users to build config files with the ease of using dictionaries.
"""

class ConfigDict(dict):
    def __init__(self,filename):
        self._filename = filename
        super(dict,self).__init__()
        with open(self._filename,'r') as fp:
            for line in fp:
                entry = line.split('=',1)
                dict.__setitem__(self,entry[0],entry[1])

    def __setitem__(self,key,value):
        dict.__setitem__(self,key,value)
        with open(self._filename,'a') as fp:
            fp.write('\n{}={}'.format(str(key),str(value)))

"""
#Testing Code

cc = ConfigDict('config_dict.txt')         # Assumes 'config_dict.txt' already exists
print(cc['sql_query'])                     # SELECT this FROM that WHERE condition
print(cc['email_to'])                      # me@mydomain.com
cc['database'] = 'mysql_managed'           # [ this writes to the config file ]

"""
