import os
import json
from pprint import pprint
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

base_url = "https://rocketchat-student.21-school.ru"
login_url = f"{base_url}/api/v1/login"
get_mentioned_endpoint = f"{base_url}/api/v1/chat.getMentionedMessages"
channels_list_endpoint = f"{base_url}/api/v1/channels.list.joined"
groups_list_endpoint = f"{base_url}/api/v1/groups.list"

access_params = {
    "user": os.getenv("ROCKET_USER"),
    "password": os.getenv("ROCKET_PASSWORD")
}


def login():
    response = requests.post(login_url, json=access_params)
    response_data = response.json()
    if response.status_code == 200 and response_data.get('status') == 'success':
        return response_data['data']['authToken'], response_data['data']['userId']
    else:
        raise Exception("Failed to login to Rocket.Chat API. Check your credentials.")


def get_mentioned(headers):
    response = requests.get(get_mentioned_endpoint, headers=headers)
    return response.json()


def get_channels_list(headers):
    response = requests.get(channels_list_endpoint, headers=headers)
    
    return response.json()


def get_groups_list(headers: dict):
    response = requests.get(groups_list_endpoint, headers=headers)
    return response.json()


def extract_channel_names(channels_list_response):
    if channels_list_response['success']:
        channels = channels_list_response['channels']
        channel_names = [channel['name'] for channel in channels]
        return channel_names
    else:
        raise ValueError("Failed to retrieve channel list.")


def extract_groups_names(groups_list_response):
    if groups_list_response['success']:
        groups = groups_list_response['groups']
        groups_names = [group['name'] for group in groups]
        return groups_names
    else:
        raise ValueError("Failed to retrieve channel list.")


def main():
    try:
        auth_token, user_id = login()
        headers = {
            "Auth-Token": auth_token,
            "X-User-Id": user_id
        }
        channels_list = get_channels_list(headers)
        pprint(extract_channel_names(channels_list))
        groups_list = get_groups_list(headers)
        pprint(extract_groups_names(groups_list))
        # # Get mentioned messages
        # mentioned_messages = get_mentioned(headers)
        # pprint(mentioned_messages)
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
