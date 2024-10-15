def set_host(row, df, read_template, f):
    holder = []
    col = 0
    while col != 2:
        holder.append(df.iat[row,col])
        col += 1
        #holder[0]=HOSTNAME
        #holder[1]=V_IP
    replace_host  = str(holder[0]) 
    replace_V_IP = str(holder[1])
    Variables = ["HOSTNAME_R","V_IP"]
    for sentences in read_template.readlines():
        words = sentences.split()
        for word in words:
            if word not in Variables and word == words[-1]: # Not replace but at last place
                f.write(word)
            elif word not in Variables: # Not replace but at beginning/middle
                f.write(word+ " ")
            elif word in Variables and word == words[-1]:
                if word == Variables[0]:
                    f.write(replace_host)
                elif word == Variables[1]:
                    f.write(replace_V_IP)
            elif word in Variables and word != words[-1]:
                if word == Variables[0]:
                    f.write(replace_host + " ")
                elif word == Variables[1]:
                    f.write(replace_V_IP + " ")
        f.write("\n")
    f.close()
    return replace_host