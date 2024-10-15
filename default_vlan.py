import pandas as pd

default_vlan = {}

def add_to_dict(port,vlan):
    global default_vlan
    port = str(port)
    vlan = str(vlan)
    if port not in default_vlan:
        default_vlan[port] = vlan
    else:
        return default_vlan
    return default_vlan
def clear_dict():
    global default_vlan
    default_vlan = {}

def set_default_vlan(replace_host):
    clear_dict()
    global default_vlan
    col_name = "ToR Switches"
    df_vlan = pd.read_excel('edit_conf/vlan_conf.xlsx',usecols="C, E, F, G")
    criteria = {col_name:replace_host}
    filtered_df = df_vlan.loc[(df_vlan[list(criteria)] == pd.Series(criteria)).all(axis=1)]
    # Loop through the row indices and access cell values
    for _, row in filtered_df.iterrows():
        column_value = row['ToR Switches Port']  # Get the value of Column3 for the current row
        column_value_2 = row['New VLAN ID']    
        # Process the cell value as needed
        if type(column_value_2) is float:
            column_value_2 = row['VLAN']                
        default_vlan = add_to_dict(column_value, column_value_2)
    return default_vlan


