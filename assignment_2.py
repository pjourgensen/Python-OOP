import abc
import datetime

class WriteFile(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self,filename):
        self.filename = filename

    def writeLine(self,line):
        myFile = open(self.filename,'a')
        myFile.write(line+'\n')
        myFile.close()

    @abc.abstractmethod
    def write(self,input):
        #writes input to a file
        return

class LogFile(WriteFile):
    def write(self,input):
        dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.writeLine('{0}    {1}'.format(dt,input))

class DelimFile(WriteFile):
    def __init__(self,filename,delim):
        super(DelimFile,self).__init__(filename)
        self.delimiter = delim

    def write(self,input):
        line = self.delimiter.join(input)
        self.writeLine(line)

log = LogFile('log.txt')                  # passes the filename to write to
mydelim = DelimFile('data.csv', ',')      # passes the filename to write to
                                          # and a delimeter

log.write('this is a log message')        # writes a message to the file
log.write('this is another log message')  # same

mydelim.write(['a', 'b', 'c', 'd'])       # writes a list of values separated
                                          # by comma to the file
mydelim.write(['1', '2', '3', '4'])       # same
