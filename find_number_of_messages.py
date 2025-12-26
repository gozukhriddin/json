from read_data import read_data

def find_number_of_messages(data=read_data())->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    message_number=0
    for message in data['messages']:
        if message['type']=='message':
            message_number+=1
    
    return message_number
if __name__ == "__main__":
   find_number_of_messages()