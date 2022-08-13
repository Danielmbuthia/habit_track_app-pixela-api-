import os

import requests
from datetime import datetime
import env

TOKEN = env.prefix('TOKEN')
pixela_endpoint = "https://pixe.la/"

user_params = {
    'token': TOKEN,
    'username': "mbuthia",
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
headers = {
    'X-USER-TOKEN': TOKEN,
}
update_user_params = {
    'newToken': TOKEN
}
create_graph_params = {
    'id': "graph1",
    'name': "mbuthia_pixela",
    'unit': "calory",
    'type': 'int',
    'color': "shibafu"
}
today = datetime.now()
today_date = str(today.date()).replace('-', '')
create_pixel_params = {
    'date': today_date,
    'quantity': '12'
}


def send_post_request(endpoint, parameters, header):
    if header:
        response = requests.post(url=endpoint, json=parameters, headers=header)
    else:
        response = requests.post(url=endpoint, json=parameters)
    print(response.text)
    response.raise_for_status()
    data = response.json()
    return data


def create_user():
    data = send_post_request(pixela_endpoint + "v1/users", user_params)
    return data


def create_a_graph(username):
    data = send_post_request(pixela_endpoint + "v1/users/" + username + "/graphs", create_graph_params, headers)
    return data


def update_user(username):
    response = requests.put(url=pixela_endpoint + "v1/users/" + username, json=update_user_params, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data


def post_a_pixel(username, graphid):
    response = send_post_request(pixela_endpoint + f"/v1/users/{username}/graphs/{graphid}", create_pixel_params,
                                 headers)
    response.raise_for_status()
    data = response.json()
    return data


post_a_pixel('mbuthia', 'graph1')
