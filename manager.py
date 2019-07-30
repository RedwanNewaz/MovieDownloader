import json
import logging
import threading
import time
import os
from subprocess import Popen, PIPE
import subprocess


logging.basicConfig(filename='debug.log', level=logging.DEBUG)

class FileManager(object):
    log = 'log.json'

    def read_json(self):
        with open(self.log, 'r') as file:
            self.data = json.load(file)[0]
            logging.debug(self.data)
    def write_json(self, data):
        with open(self.log, 'w') as outfile:
            outfile.write(json.dumps([data], indent=4))

    def get_pid(self):
        self.read_json()
        return self.data['status']
    def update_pid(self, pid):
        self.data['status'] = pid
        self.write_json(self.data)

class ProcessMonitor(object):

    def is_alive(self, pid):
        result = pid > 1
        logging.debug('process is {}'.format(result))
        return result

    def sanity_check(self, pid):
        return not self.is_alive(pid)


def thread_function(program):
    logging.debug('downloading  attempted')
    try:
        logging.debug('downloading from  {} ....'.format(program.url))   
        file = program.file
        url = program.url.strip()
        exe = ["C:/ProgramData/chocolatey/bin/axel"]
        args=['-o', file, '-a', '-n', '8', url]

        # stdout = Popen(exe+args)

        process = Popen(exe+args, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        logging.debug(stderr)
        logging.debug("download succeed")
        logging.debug(stdout)
        program.update_pid(-1)
    except:
        logging.debug("download failed")
        program.update_pid(-1)




class ProgramManager(FileManager,ProcessMonitor):
    def __init__(self):
        self.storage_dir = 'C:\Users\Redwan Newaz\Videos\current\{}.mp4'

    def execute(self):
        old_pid = self.get_pid()
        self.file = self.storage_dir.format(self.data['file'])
        self.url = self.data['url']
        if self.sanity_check(old_pid):
            danggle_thread = threading.Thread(target=thread_function,args=(self,))
            danggle_thread.start()
            pid = os.getpid()
            self.update_pid(pid)
            # danggle_thread.join()
        else:
            print "sanity check failed <br>"
        print "request has been processed <br>"



    def download(self):
       logging.debug('downloading from  {} ....'.format(download.url))   
       file = download.file
       url = download.url.strip()
       exe = ["C:/ProgramData/chocolatey/bin/axel"]
       args=['-o', file, '-a', '-n', '8', url]
       process = Popen(exe+args, stdout=PIPE, stderr=PIPE)
       stdout, stderr = process.communicate()
       logging.debug(stderr)
       logging.debug(stdout)



if __name__ == '__main__':
    program = ProgramManager()
    program.execute()
