from threading import Thread, active_count
from subprocess import Popen, PIPE
import time,os, json
from datetime import datetime

class Backend(Thread):
    __count = active_count() + 1
    __request = {}
    def __init__(self, param):
        Thread.__init__(self)
        self.__arg = param

    def __get_extention(self, name):
        s = name.split('.')
        return s[-1]
    def __logger(self,file=None,url=None, start = True):
        def timestamp():
            date_time = datetime.fromtimestamp(time.time())
            return str(date_time.strftime("%m/%d/%Y, %H:%M:%S"))
        def append_to_json(_dict,path): 
            # borrowed form https://stackoverflow.com/questions/12994442/how-to-append-data-to-a-json-file
            with open(path, 'ab+') as f:
                f.seek(0,2)                                #Go to the end of file    
                if f.tell() == 0 :                         #Check if file is empty
                    f.write(json.dumps([_dict]).encode())  #If empty, write an array
                else :
                    f.seek(-1,2)           
                    f.truncate()                           #Remove the last character, open the array
                    f.write(' ,\n '.encode())                #Write the separator
                    f.write(json.dumps(_dict).encode())    #Dump the dictionary
                    f.write(']'.encode()) 
            

        if(start):
            self.__request['file'] =file
            self.__request['url'] = url
            self.__request['start_time'] = timestamp()
        else:
            self.__request['finish_time'] = timestamp()
            # TODO append log file 
            if(len(self.__arg["dir_log"])>0):
                file = self.__arg["dir_log"]+"/log.json"
                append_to_json(self.__request, file)
                
    def get_download_path(self):
        root = self.__arg["dir_download"]
        category = self.__arg["option"] 
        path = root + "/" +  category
        # TODO - create dir 
        if not os.path.exists(path):
            os.makedirs(path)

        return path+"/{}.{}"          


    def run(self):
        active = active_count() - self.__count
        if(active>(2+self.__arg["max_threads"])): # 2 is base num threads that are currently running, download will create extra thread
            print('process cannot be handled ', active)
            return


        # prepearation for downloading
        DOWNLOAD_DIR = self.get_download_path()
        url = self.__arg['link'].strip()
        file = DOWNLOAD_DIR.format(self.__arg['file'].strip(), self.__get_extention(url))
        self.__logger(file,url)
        exe = [self.__arg["program"]]
        args=['-o', file, '-a', '-n', self.__arg["num_connection"], url]

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
        self.__logger(start=False)
        