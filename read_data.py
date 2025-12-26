import json
def read_data(file_path='./data/result.json')->dict:
    """
    This function will read the json file and return the data as a dictionary.
    
    Parameters:
        file_path (str): Path of the file to be read
    Returns:
        dict: Dictionary containing the data of the json file.
    
    """
    
    file =open(file_path, 'r')
    data=file.read()
    message_data=json.loads(data)
    return message_data
if __name__ == "__main__":
    read_data()
