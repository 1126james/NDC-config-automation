import os
import shutil
import pandas as pd
import set_host_and_IP as sh
import dfs 
import default_vlan as dv
import get_vlan_trunk as gvt


def create(replace_host):
    newname = replace_host+".txt"
    old = "C:/Users/James/Desktop/python/NDC/creation/creation4.txt"
    new = "C:/Users/James/Desktop/python/NDC/creation/test/"+newname
    shutil.copy2(old,new)
    
def print_dfs(dfs_grp):
    Variables = "dfs_R"
    read_1st_creation = open('creation/creation.txt', 'r')
    f = open('creation/creation2.txt', 'w')
    conf = ''
    if dfs_grp == 1:
        conf += 'priority 150\nsource ip 192.168.101.1 vpn-instance mgmt peer 192.168.101.2'
    elif dfs_grp == 2:
        conf += 'priority 120\nsource ip 192.168.101.2 vpn-instance mgmt peer 192.168.101.1'
    for sentences in read_1st_creation.readlines():
        words = sentences.split()
        for word in words:
            if word != Variables and word == words[-1]: # Not replace but at last place
                f.write(word)
            elif word !=  Variables: # Not replace but at beginning/middle
                f.write(word+ " ")
            elif word == Variables and word == words[-1]:
                f.write(conf)
            elif word == Variables and word != words[-1]:
                f.write(conf + " ")
        f.write("\n")
    read_1st_creation.close()
    f.close()
    os.remove('creation/creation.txt')
    return

def replace_dv(default_vlan_dict):
    port_name = "interface 10GE1/0/"
    replacement = "port default vlan "

    with open('creation/creation2.txt', 'r') as file:
        lines = file.readlines()

    with open('creation/creation3.txt', 'w') as file:
        found = False
        for line in lines:
            if found:
                found = False
                continue
            for port in default_vlan_dict:
                if line.strip() == port_name+port:
                    file.write(line)
                    replacement_line = replacement + default_vlan_dict[port]
                    file.write(replacement_line + "\n")
                    found = True
                    break
            if not found:
                file.write(line)

        file.close()
    os.remove('creation/creation2.txt')
    return

def add_vlan_trunk(vlan_list):
    vlan_list.sort()
    with open('creation/creation3.txt', 'r') as file:
        lines = file.readlines()

    with open('creation/creation4.txt', 'w') as file:
        for line in lines:
            file.write(line)
            if line.strip() == "port link-type trunk":
                content = "port trunk allow-pass vlan " + " ".join(str(num) for num in vlan_list) + "\n"
                file.write(content)
    file.close()
    os.remove('creation/creation3.txt')
    return




def main():
    row = 0
    while row != 156:
        try:
            error_dict = {}
            error_count = 0
            df = pd.read_excel('edit_conf/read_this.xlsx')
            read_template = open('template/swt01klngc-bm08.txt', 'r') # Read Only
            f = open('creation/creation.txt', 'w') # Append file
            error_file = open("creation/error/error_container_1.txt","w")
            error_file2 = open("creation/error/error_container_2.txt","w")
    ##############
            replace_host = sh.set_host(row, df, read_template, f)
    ##############
            dfs_grp = dfs.set_dfs(replace_host, error_dict, error_file, error_file2, error_count)
    ##############
            print_dfs(dfs_grp)
            read_template.close()
    ##############
            default_vlan_dict = dv.set_default_vlan(replace_host)
    ##############
            replace_dv(default_vlan_dict)
    ##############

            vlan_list = gvt.set_vlan_trunk(row, replace_host)

    ##############
            add_vlan_trunk(vlan_list)

            f.close()

            create(replace_host)

            row+=1
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print(replace_host)
            row+=1
            continue


if __name__ == '__main__':
    main()



