from read_data import read_data

def find_all_users_name(data=read_data())->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    messeges=data['messages']
    users_name=[]
    for messege in messeges:
        if 'from_id' in messege and messege['from_id'].startswith('user'):
            if messege['from'] not in users_name:
                users_name.append(messege['from'])
                # print(messege['from'])
    
    return users_name


if __name__ == "__main__":
    find_all_users_name()