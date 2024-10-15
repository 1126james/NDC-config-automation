def set_dfs(replace_host, error_dict, error_file, error_file2, error_count):

    if type(replace_host) is str:
        hostname = replace_host[:5]
        if hostname[-1] == "1":
            return 1
        elif hostname[-1] == "2":
            return 2
        else:
            error_dict['error'+str(error_count)] = replace_host
            print("Bad1")
            error_count+=1
    else:
        error_dict['error'+str(error_count)] = replace_host
        print("Bad2")
        error_count+=1

    #Show Error Files

    for key , value in error_dict.items():
        if type(value[4]) is not float:
            error_file.writelines(key,value)
            print(key,value)

    for key , value in error_dict.items():
        if type(value[4]) is float:
            error_file2.writelines(key,value)           
    return