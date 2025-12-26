from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data = read_data(), users_id = find_all_users_id())->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    user_data={}
    for message in data['messages']:
        if 'from_id' in message:
            if message['from_id'] not in user_data:
                user_data[message['from_id']]={
                    'user': message['from'],
                    'message_count': 0
                    }
            else:
                user_data[message['from_id']]['message_count']+=1
    # for i,k in user_data.items():
    #     print(i,k)
    return user_data
# find_user_message_count()