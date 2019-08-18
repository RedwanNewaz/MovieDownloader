from threading import Thread, active_count
from app.configs import AXEL, DOWNLOAD_DIR,CONNECTION
from subprocess import Popen, PIPE
import time,os
from datetime import datetime

class Backend(Thread):
    __count = active_count() + 1
    __request = {'file':None, 'url':None, 'time':None}
    def __init__(self, param):
        Thread.__init__(self)
        self.__arg = param

    def __get_extention(self, name):
        s = name.split('.')
        return s[-1]
    def __logger(self,file,url):
        self.__request['file'] =file
        self.__request['url'] = url
        self.__request['time'] = time.time()
        print('requested time ', datetime.fromtimestamp(self.__request['time']))


    def run(self):
        active = active_count() - self.__count
        if(active>3):
            print('process cannot be handled ', active)
            return


        # prepearation for downloading
        url = self.__arg['link'].strip()
        file = DOWNLOAD_DIR.format(self.__arg['file'].strip(), self.__get_extention(url))
        self.__logger(file,url)
        exe = [AXEL]
        args=['-o', file, '-a', '-n', CONNECTION, url]

        print('downloading file:={} \n from: {}'.format(file, url))
        print("axel cmd ", exe+args)

        # start downloading
        process = Popen(exe+args, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        print(stdout)
        ret = process.wait()

        # if downloaded file exist then save log otherwise show download failed
        if(os.path.exists(self.__request['file'])):
            print('download finished with {}'.format(ret))
        else:
            print("[ERROR] Download Failed !!!!")
  
        
