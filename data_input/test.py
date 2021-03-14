csv_detail = []
for nodes in host_list:
    for i,y in enumerate(input_df['HOSTNAME']):
        if nodes == y:
            interface = input_df.loc[input_df['HOSTNAME']==nodes, 'INTERFACE'].iloc[i]
            interface_desc = input_df.loc[input_df['HOSTNAME']==nodes, 'INT_DESC'].iloc[i]
            snmp = input_df.loc[input_df['HOSTNAME']==nodes, 'SNMP_LOC'].iloc[i]
            csv_details.append({nodes:[interface,interface_desc,snmp]})

csv_detail = []
for nodes in host_list:
    node_dict = {nodes:[]}
    for x in input_df['HOSTNAME']:
        if x == nodes:
            interface = input_df.loc[input_df['HOSTNAME']==x, 'INTERFACE']
            tmp_list = []
            for _ in range(len(interface)):
                tmp_list = []
                interface = input_df.loc[input_df['HOSTNAME'] == x, 'INTERFACE'].iloc[_]
                interface_desc = input_df.loc[input_df['HOSTNAME']==x, 'INT_DESC'].iloc[_]
                snmp = input_df.loc[input_df['HOSTNAME']==x, 'SNMP_LOC'].iloc[_]
                tmp_list.append(interface)
                tmp_list.append(interface_desc)
                tmp_list.append(snmp)
                node_dict[x].append(tmp_list)
    csv_detail.append(node_dict)


csv_detail = []
for nodes in host_list:
    node_dict = {nodes:[]}
    for x in input_df['HOSTNAME']:
        tmp_list = []
        interface = input_df.loc[input_df['HOSTNAME'] == x, 'INTERFACE'].values[0]
        interface_desc = input_df.loc[input_df['HOSTNAME']==x, 'INT_DESC'].iloc[_]
        snmp = input_df.loc[input_df['HOSTNAME']==x, 'SNMP_LOC'].iloc[_]
        tmp_list.append(interface)
        tmp_list.append(interface_desc)
        tmp_list.append(snmp)
        node_dict[x].append(tmp_list)
    csv_detail.append(node_dict)

[{'MYGTSTBDCIBE002': [[list1],[list2]]},{'MYGTSTBDCIBE003': [[list1]]}]

import csv
file_path = "C:\\Users\\jraluta\\nrfu\\config_push\\"
with open(file_path + "data_input\\Sample_Nodes.csv", 'r') as csv_file:
    reader = csv.reader(csv_file)
    tnt = {}
    for row in reader:
        if tnt == {}:
            tnt[row[0]] = {'attributes':{['interface':row[1],'desc':row[2],'snmp':row[3]]}]}
        elif tnt != {} and



site_list = [{'site1':[{'a':1,'b':2,'c':3},{'snmp':7}]},{'site2':[{'a':4,'c':5},{'snmp1':6}]}]

file_path = "/home/users/jraluta/tnt_script/config_push/"
for k in site_list:
    for key, value in k.items(): \
    print(list(value[0].keys()), list(value[1].keys()))
---------------------------------------------
    ['a', 'b', 'c']['snmp']
    ['a', 'c']['snmp1']

from jinja2 import Environment, FileSystemLoader
file_path = "C:\\Users\\jraluta\\nrfu\\config_push\\"
import csv
with open(file_path+"data_input\\Sample_Nodes.csv", encoding='utf-8-sig') as file:
    read = csv.reader(file)
    row = ""
    site_list = []
    for r in read:
        if r[0] != row:
            site_dict = {}
            int_dict = {}
            int_dict[r[1]] = r[2]
            snmp_dict = {}
            snmp_dict['snmp'] = r[3]
            site_dict[r[0]] = [int_dict,snmp_dict]
            site_list.append(site_dict)

snmp_site_list = []
snmp_list = []
for k in site_list:
        for key, value in k.items():
            v1 = list(value[0].keys())[0]
            v2 = list(value[0].values())[0]
            v3 = list(value[1].values())[0]
            if key in snmp_site_list:
                continue
            else:
                snmp_site_list.append(key)
            if v3 in snmp_list:
                continue
            else:
                snmp_list.append(v3)
        file_loader = FileSystemLoader(file_path+"template")
        env = Environment(loader=file_loader)
        template = env.get_template("desc_template.j2")
        output = template.render({'v1':v1, 'v2':v2})
        with open(file_path+"data_output\\"+key+".txt", 'a+') as write_file:
            write_file.write(output)





