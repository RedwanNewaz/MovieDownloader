from threading import Thread, active_count
from time import sleep
import os
from subprocess import Popen, PIPE

class Backend(Thread):
    count = active_count() + 1
    def __init__(self, param):
        Thread.__init__(self)
        self.__arg = param

    def run(self):
        active = active_count() - self.count
        if(active>3):
            print('process cannot be handled ', active)
            return
        
        # modify here
        storage_dir = 'C:/Users/Redwan Newaz/Videos/current\{}.mp4'
        file = storage_dir.format(self.__arg['file'])
        url = self.__arg['link'].strip()
        exe = ["C:/ProgramData/chocolatey/bin/axel"]
        args=['-o', file, '-a', '-n', '8', url]

        print('downloading file:={} \n from: {}'.format(file, url))
        

        # stdout = Popen(exe+args)

        process = Popen(exe+args, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        print(stdout)
        ret = process.wait()
        print('download finished with {}'.format(ret))
  
        
