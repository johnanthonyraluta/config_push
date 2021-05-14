from netmiko import ConnectHandler
from data_input.validation_commands import show_command_list
from jinja2 import Environment, FileSystemLoader
import sys

#show_command_list = ["show int desc","show version","show ip int br","show clo","show log | in Nov"]
#host_list=["10.205.142.67","10.205.142.79","10.205.138.64","10.205.138.65"]
file_path = "/home/users/jraluta/tnt_script/config_push/"

def hostname():
    host_list = []
    input_df = None
    try:
        input_df = pd.read_csv(file_path + "data_input\\Sample_Nodes.csv")
        host_c1 = input_df['HOSTNAME']
        for _ in host_c1:
            if _ in host_list:
                continue
            else:
                host_list.append(_)
        return [host_list,input_df] # in list format
    except:
        return [host_list,input_df]

def read_csv():
    csv_details = []
    tnt_nodes = hostname()
    df = tnt_nodes[1]
    if tnt_nodes[0] is None:
        return('No CSV File Found!')
    else:
        for device_name in tnt_nodes[0]:
            # foca_site = foca_df.loc[foca_df['SOURCE_IPV4_ADDRESS'] == ip, 'SITE NAME'].iloc[0]
            interface = df.loc[df['HOSTNAME']==device_name, 'INTERFACE'].iloc[0]
            interface_desc = df.loc[df['HOSTNAME']==device_name, 'INT_DESC'].iloc[0]
            snmp = df.loc[df['HOSTNAME']==device_name, 'SNMP_LOC'].iloc[0]
            csv_details.append({device_name:[interface,interface_desc,snmp]})
    return csv_details

def generate_config(data):
    file_loader = FileSystemLoader('templates/')
    env = Environment(loader=file_loader)
    template = env.get_template("panel.j2")
    output = template.render(data=data)
    return output

def tnt_connect(host):
    try:
        tnt_session = ConnectHandler(
          device_type = "cisco_xr",
          host=host,
          username= "cisco",
          password= "T&T!@bd!@n-C!sc0",
        )
        tnt_session.logfile = open("tnt_connect.log", "w+b")
        return tnt_session
    except:
        return None
def tnt_disconnect(tnt_session):
    tnt_session.disconnect()

def show_command(tnt_session,sh_command):
    command_out = tnt_session.send_command(sh_command,expect_string=r'#',delay_factor=5)
    return command_out

def push_config(tnt_session,cfg_list):
    cfg_out = tnt_session.send_config_set(cfg_list)
    return cfg_out

def save_to_file(command_out,host,command,activity):
    with open('/home/users/jraluta/tnt_script/UPGRADE/data_output/' + host + '_' + activity, 'a') as parse_results:
              parse_results.write(command + '\n')
              parse_results.write("="*25 + '\n')
              parse_results.write(command_out + '\n')

def main():
    try:
       sys.argv[1]
    except:
       print('Specify if precheck,postcheck or adhoc: ')
       sys.exit(1)

    activity = sys.argv[1]

    for host in host_list:
        tnt_sess = tnt_connect(host)
        for command in show_command_list:
            try:
                command_out = show_command(tnt_sess,command)
                save_to_file(command_out,host,command,activity)
                print('Success ' + command + ' ' + host)
            except:
                print('Failed ' + command + ' of ' + host) 
        tnt_disconnect(tnt_sess)
    print("Done!")
if __name__ == '__main__':
    main()
