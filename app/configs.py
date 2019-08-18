import yaml
import os

def sanity_check(dir):
    dir = dir.split("/")
    dir = "/".join(dir[:-1])
    assert os.path.isdir(dir), "cannot find download folder @ {}".format(dir)
    return dir+"/"


#read yaml file
print("config read form [{}]".format(os.getcwd()))
try:
    with open("config.yaml", 'r') as file:
        data = yaml.safe_load(file)
except:
    with open("../config.yaml", 'r') as file:
        data = yaml.safe_load(file)

IP_ADDRESS = data['server']['ip']
PORT = data['server']['port']
DOWNLOAD_DIR = data['server']['download_folder']
AXEL = data['axel']['exe']
CONNECTION = data['axel']['connection']

UPLOAD_DIR = sanity_check(DOWNLOAD_DIR)

if __name__ == '__main__':
    print(IP_ADDRESS)
    print(DOWNLOAD_DIR)
    print(AXEL)
    print(CONNECTION)