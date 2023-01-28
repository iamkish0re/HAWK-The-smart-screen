import json

CREDENTIALS_SCHEMA = {"name": "", "password": "", "face_encoding": ""}
CREDENTIALS_FILE   = 'resources/credentials.json'

def read_all_user():
    with open(CREDENTIALS_FILE) as json_file:
        credentials = json.load(json_file)
    return credentials

def save_credentials(credentials : dict):
    with open(CREDENTIALS_FILE) as cred_file:
        json.dump(credentials, cred_file)

def is_user_exists(user_list, username):
    if len(user_list) == 0:
        return 0 # NO USERS
    else:
        for user in user_list:
            if user['name'] == username:
                return 1 # USER FOUND
            else:
                return 2 # USER NOT FOUND 
    return 2 # USER NOT FOUND

def add_user(user_details : dict):
    credentials = read_all_user()
    is_user = is_user_exists(credentials['users'], user_details['name'])
    if is_user == 0 or is_user == 2: # If user is empty or not found, insert
        credentials['users'].append(user_details)
        save_credentials(credentials)
        return 1 # USER DETAILS SAVED
    else:
        return 0 # USER EXISTS

def create_user(username, password):
    new_user = CREDENTIALS_SCHEMA
    new_user['name'] = username
    new_user['password'] = password
    new_user['face_encoding'] = []
    return new_user

# def delete_user(username: str):

print(add_user({'name': 'test_user', 'password': 'test_pass', 'face_encoding': 'test_encoding'}))