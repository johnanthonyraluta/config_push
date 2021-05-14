from jinja2 import Environment, FileSystemLoader
import csv
#file_path = "C:\\Users\\jraluta\\nrfu\\config_push\\"
file_path="/home/users/jraluta/tnt_script/config_push/"
def read_input():
    site_list = []
    with open(file_path+"data_input/Sample_Nodes2.csv", encoding='utf-8-sig') as file:
        read = csv.reader(file)
        for r in read:
            site_dict = {}
            int_dict = {}
            int_dict[r[1]] = r[2]
            snmp_dict = {}
            snmp_dict['snmp'] = r[3]
            site_dict[r[0]] = [int_dict,snmp_dict]
            site_list.append(site_dict)
    return site_list

def render_int_desc(site_list,snmp_site_list,snmp_list):
    for k in site_list:
        for key, value in k.items():
            v1 = list(value[0].keys())[0]
            v2 = list(value[0].values())[0]
            v3 = list(value[1].values())[0]
            if key in snmp_site_list:
                continue
            else:
                snmp_site_list.append(key)
            # if v3 in snmp_list:
            #     continue
            # else:
            snmp_list.append(v3)
        if v2 != "":
            print(key,v2)
            file_loader = FileSystemLoader(file_path + "template")
            env = Environment(loader=file_loader)
            template = env.get_template("desc_template.j2")
            output = template.render({'v1': v1, 'v2': v2})
            with open(file_path + "data_output/" + key + ".cfg", 'a+') as write_file:
                write_file.write(output)

def render_snmp(snmp_site_list,snmp_list):
    snmp_dic = {snmp_site_list[i]: snmp_list[i] for i in range(len(snmp_site_list))}
    for key, value in snmp_dic.items():
        if value != "":
            v3 = value
            print(key,v3)
            file_loader = FileSystemLoader(file_path + "template")
            env = Environment(loader=file_loader)
            template = env.get_template("snmp_template.j2")
            output = template.render({'v3': v3})
            with open(file_path + "data_output/" + key + ".cfg", 'a+') as write_file:
                write_file.write(output+"\n")
                write_file.write("commit\n")
                write_file.write("exit\n")
                write_file.write("terminal length 0\n")
                write_file.write("show interface desc\n")
                write_file.write("show run snmp-server | i location\n")
                write_file.write("show config commit changes last 1\n")
                write_file.write("show clock\n")

def main():
    snmp_site_list = []
    snmp_list = []
    render_int_desc(read_input(),snmp_site_list,snmp_list)
    render_snmp(snmp_site_list,snmp_list)
    with open(file_path+"data_input/nodes_for_config_isat.txt", 'w') as writer:
        for sites in snmp_site_list:
            writer.write(sites+"\n")
    print('Config rendered!')


if __name__ == '__main__':
    main()
