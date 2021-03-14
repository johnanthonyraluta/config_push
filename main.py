from data_input.nodes_inventory import host_list
from modules.spof_checks import tnt_connect,tnt_disconnect,show_command,push_config,file_path
import os.path
from os import path
import time,datetime

def parse_to_list(file):
    new_list = []
    with open(file,'r') as reader:
        for content in reader:
            new_list.append(content.strip().split('\n')[0])
    return new_list

def connect_device(device_ip):
    tnt_session = tnt_connect(device_ip)
    return tnt_session

def check_host(tnt_session,device_name):
    prompt = tnt_session.find_prompt()
    if device_name in prompt:
        return True
    return False

def disco_device(tnt_session):
    tnt_disconnect(tnt_session)

def deploy_config(tnt_session,cfg_list):
    deploy_output = push_config(tnt_session,cfg_list)
    return deploy_output

def main():
    target_nodes = parse_to_list(file_path+"data_input/nodes_for_config.txt")
    for host in host_list:
        for nodes in target_nodes:
            if path.exists(file_path + "data_input/" + nodes + ".cfg") == True:
                if nodes == host.split()[0]:
                    tnt_session = connect_device(host.split()[1])
                    status = check_host(tnt_session,nodes)
                    if status == True:
                        cfg_list = parse_to_list(file_path+"data_input/"+nodes+".cfg")
                        print('Deploying configuration on ' + nodes)
                        config_session= deploy_config(tnt_session,cfg_list)
                        print(config_session)
                        with open(file_path+"data_output/"+nodes+".log","w") as writer:
                           #for lines in config_session:
                            writer.writelines(config_session + '\n')
                        print('Config done on '+ nodes)
                    else:
                        print('Discrepancy with inventory file found! Task aborted!')
                        disco_device(tnt_session)
                    disco_device(tnt_session)
            else:
                print('No config file found for ' + nodes)

if __name__ == '__main__':
    main()




