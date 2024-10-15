import pandas as pd
vlan_list = []

def add_to_vlan_list(vlan):
    global vlan_list
    if vlan > 0:
        vlan_list.append(vlan)
        vlan_set = set(vlan_list)
        return list(vlan_set)
    else:
        return vlan_list

def clear_vlan_list():
    global vlan_list
    vlan_list = []

def float_to_int(vlan_float):
    vlan_int = [int(num) for num in vlan_float]
    return vlan_int

def set_vlan_trunk(row, replace_host):
    clear_vlan_list()
    df_vlan = pd.read_excel('edit_conf/vlan_conf.xlsx',usecols="C, E, G")
    global vlan_list
    rack = replace_host.split("-")
    col_name = "ToR Switches"
    filtered_df = df_vlan[df_vlan[col_name].astype(str).str.contains(rack[1], case=False)]
    # Loop through the row indices and access cell values
    for _, row in filtered_df.iterrows():
        column_value = row['VLAN']  # Get the value of Column3 for the current row
        column_value_2 = row['New VLAN ID']    
        # Process the cell value as needed
        vlan_list = add_to_vlan_list(float(column_value))
        vlan_list = add_to_vlan_list(float(column_value_2))
    vlan_list = float_to_int(vlan_list)
    return vlan_list