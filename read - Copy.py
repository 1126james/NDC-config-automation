import os
import pandas as pd

df = pd.read_excel('edit_conf/read_this.xlsx',usecols=["Hostname","IP Address"])
df_vlan = pd.read_excel('edit_conf/vlan_conf')


##### Handle df first
row = 0
while row != 170:
    holder = []
    col = 0
    while col != 2:
        holder.append(df.iat[row,col])
        col += 1
        #holder[0]=HOSTNAME
        #holder[1]=V_IP
    read_conf_file = open('template/swt01klngc-bm08.txt', 'r') # Read Only
    f = open('creation/creation.txt', 'w') # Append file

    replace_host  = str(holder[0]) 
    replace_V_IP = str(holder[1])

    Variables = [
    "HOSTNAME_R",
    "OOBMgmtIP",
    "DevMgmtIP",
    "XGE1_R",
    "XGE2_R"]

    for sentences in read_conf_file.readlines():
        words = sentences.split()
        for word in words:
            if word not in Variables and word == words[-1]: # Not replace but at last place
                f.write(word)
            elif word not in Variables: # Not replace but at beginning/middle
                f.write(word+ " ")
            elif word in Variables and word == words[-1]: # Is replace and is at last place
                print("Success")
                if word == Variables[0]: #HOSTNAME
                    f.write(replace_host)
                    print("Replaced"+ Variables[0])
                elif word == Variables[1]: #OOBMgmtIP
                    f.write(replace_oobmgmt)
                    print("Replaced"+ Variables[1])
                elif word == Variables[2]: #DevMgmtIP
                    f.write(replace_devmgmt)
                    print("Replaced"+ Variables[2])
                elif word == Variables[3]: #XGE1
                    f.write(replace_xge1)
                    print("Replaced"+ Variables[3])
                elif word == Variables[4]: #XGE2
                    f.write(replace_xge2)
                    print("Replaced"+ Variables[4])
                else:
                    print("Unknow error") 
                    quit
            elif word in Variables and word != words[-1]: # Is replace and is at beginning/middle
                print("Success")
                if word == Variables[0]: #HOSTNAME
                    f.write(replace_host+ " ")
                    print("Replaced"+ Variables[0])
                elif word == Variables[1]: #OOBMgmtIP
                    f.write(replace_oobmgmt+ " ")
                    print("Replaced"+ Variables[1])
                elif word == Variables[2]: #DevMgmtIP
                    f.write(replace_devmgmt+ " ")
                    print("Replaced"+ Variables[2])
                elif word == Variables[3]: #XGE1
                    f.write(replace_xge1+ " ")
                    print("Replaced"+ Variables[3])
                elif word == Variables[4]: #XGE2
                    f.write(replace_xge2+ " ")
                    print("Replaced"+ Variables[4])
                else:
                    print("Unknow error") 
                    quit
        f.write("\n") # new lines
    f.close()


    newname = replace_host+".txt"
    old = r"C:\Users\02007356\Desktop\self work\python\config\creation.txt"
    new = r"C:\Users\02007356\Desktop\order\HKSP-i86922\fs_conf\\"+newname
    os.rename(src=old,dst=new, src_dir_fd=None, dst_dir_fd=None)

    row += 1

