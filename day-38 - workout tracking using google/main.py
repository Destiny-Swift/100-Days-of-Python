# Modify run configuration with these environment variables
# PYTHONUNBUFFERED=1;NT_API_KEY=059b30e30deeb9975ea9abe0218ac0e6;NT_APP_ID=5110e7f3;
# SHEETY_AUTH_KEY=Basic ZGVzdGlueTpJIGFtIElyb24gTWFu;
# SHEET_ENDPOINT=https://api.sheety.co/59a6c6dc665a1b5959bdd313b8ec884b/myWorkouts/workouts

import requests
from datetime import datetime
import os


# STEP 1: Use the nutritionix api to get exercise output for exercise input in natural
# language
nutritionix_endpoint = 'https://trackapi.nutritionix.com'

app_id = os.environ['NT_APP_ID']
api_key = os.environ['NT_API_KEY']
GENDER = 'male'
WEIGHT_KG = '63'
HEIGHT_CM = '200'
AGE = '18'

natural_language_exercise_endpoint = f'{nutritionix_endpoint}/v2/natural/exercise'

headers = {
    'x-app-id': app_id,
    'x-app-key': api_key,

}

exercise_data = {
    'query': input('Tell me which exercises you did: '),
    "gender": GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

response = requests.post(url=natural_language_exercise_endpoint, json=exercise_data, headers=headers)
response.raise_for_status()
exercises = response.json()['exercises']
# print(exercises)


# STEP 2: Use the Sheety api to generate a new row of data in your Google Sheet for each exercise that you get back from
# the nutritionix api

sheety_googlesheet_endpoint = 'https://api.sheety.co/59a6c6dc665a1b5959bdd313b8ec884b/myWorkouts/workouts'

headers = {
    'Authorization': os.environ['SHEETY_AUTH_KEY']
}

for exercise in exercises:
    row_details = {
        'workout': {
            'date': datetime.now().date().strftime('%d/%m/%Y'),
            'time': datetime.now().time().strftime('%H:%M:%S'),
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }

    response = requests.post(url=sheety_googlesheet_endpoint, json=row_details, headers=headers)
    # response.raise_for_status()
    print(response.text)
    # I'd advise making a first row sheet entry to set formatting rules

# STEP 3: Store sensitive data as environment variables, in this case app_id, api_key and header authorization
# sensitive data was stored as persistent values using the 'edit configuration' function of pycharm, just as in
# pythonanywhere and replit's secrets(secret keys)
# you're good using the right config file
# print(os.environ)
