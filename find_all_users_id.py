from read_data import read_data


def find_all_users_id(data=read_data())->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    messeges=data['messages']
    users_id=[]
    for messege in messeges:
        if 'from_id' in messege and messege['from_id'].startswith('user'):
            if messege['from_id'] not in users_id:
                users_id.append(messege['from_id'])

    return users_id


if __name__ == "__main__":
   find_all_users_id()