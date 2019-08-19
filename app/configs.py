import yaml
import os

def sanity_check(dir):
    dir = dir.split("/")
    dir = "/".join(dir[:-1])
    assert os.path.isdir(dir), "cannot find download folder @ {}".format(dir)
    return dir+"/"


#read yaml file
def get_config_file():
    path = os.path.abspath(__file__)
    for _ in range(2):
        path,_ = os.path.split(path)
    path = os.path.join(path, "config.yaml")
    return path
CONFIG_FILE = get_config_file()
print("config read form [{}]".format(CONFIG_FILE))
try:
    with open(CONFIG_FILE, 'r') as file:
        data = yaml.safe_load(file)
except:
    raise ValueError
 
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