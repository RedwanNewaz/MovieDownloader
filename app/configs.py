import yaml
import os

#read yaml file
print("config read form [{}]".format(os.getcwd()))
try:
    with open("config.yaml", 'r') as file:
        data = yaml.safe_load(file)
except:
    with open("../config.yaml", 'r') as file:
        data = yaml.safe_load(file)

IP_ADDRESS = data['server']['ip']
DOWNLOAD_DIR = data['server']['download_folder']
AXEL = data['axel']['exe']
CONNECTION = data['axel']['connection']

if __name__ == '__main__':
    print(IP_ADDRESS)
    print(DOWNLOAD_DIR)
    print(AXEL)
    print(CONNECTION)