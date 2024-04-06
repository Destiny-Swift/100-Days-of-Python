import requests
from datetime import datetime

USERNAME = 'swift'
TOKEN = 'I am Iron Man'
GRAPH_ID = 'graph1'
DATE = datetime.now().date().strftime('%Y%m%d')  # f'{datetime.now().date()}'.replace('-', '')

# STEP 1: create a new user profile on Pixela with requests.post()
pixela_endpoint = 'https://pixe.la/v1/users'  # endpoint for creating a new profile

user_params = {
    'token': TOKEN,
    'username': 'USERNAME',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)
# user profile created successfully; notice the use of 'json' arg and not the 'params' arg


# STEP 2: create a new graph with requests.post()
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': GRAPH_ID,
    'name': 'Coding Graph',
    'unit': 'hours',
    'type': 'float',
    'color': 'shibafu',
}

headers = {
    'X-USER-TOKEN': TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# response.raise_for_status()
# print(response.text)
# notice the use of the 'headers' argument and the corresponding parameter...that's for safekeeping.


# STEP 3: posting a pixel on our habit graph with requests.post()
pixel_creation_endpoint = f'{graph_endpoint}/{GRAPH_ID}'

pixel_creation_data = {
    'date': DATE,
    'quantity': str(float(input('How many hours did you code today? '))),

}

response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_data, headers=headers)
response.raise_for_status()
print(response.text)
# pixel posted


# STEP 4: Updating a pixel with requests.put()
pixel_replacement_endpoint = f'{pixel_creation_endpoint}/{DATE}'

# pixel_replacement_data = {
#     'quantity': str(float(input('Enter replacement for hours you spent coding today: ')))
# }

# response = requests.put(url=pixel_replacement_endpoint, json=pixel_replacement_data, headers=headers)
# response.raise_for_status()
# print(response.text)
# pixel updated successfully


# STEP 4: Deleting a pixel with requests.delete()
pixel_deletion_endpoint = pixel_replacement_endpoint

# response = requests.delete(url=pixel_deletion_endpoint, headers=headers)
# response.raise_for_status()
# print(response.text)
# pixel deleted successfully

# with all said and done this needs a UI to work and perhaps also display the amazing habits graph.
# I'm thinking working directly with the API to make realtime edits like pick a day and change the value
