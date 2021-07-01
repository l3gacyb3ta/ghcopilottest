import requests, json
import os
import webbrowser

def get_podcast_name() -> str:
    """ Gets the name of the podcast based on user input"""
    return input("Enter the name of the podcast: ")

def pretty_print_dict(dictionary: dict):
    """Prints out the dictionary in a pretty format"""
    print(json.dumps(dictionary, indent=4, sort_keys=True))

def pretty_print_json(json: str):
    """Prints out the json string pretty"""
    json_obj = json.loads(json)
    pretty_print_dict(json_obj)

def display_image_in_commandline(image_url: str):
    """Displays the image from the given url in the command line"""
    webbrowser.open(image_url)

def podcast_info(name: str):
    """Gets the number of episodes of a podcast and its description using an API"""
    url = "https://itunes.apple.com/search?term=" + name + "&entity=podcast"
    response = requests.get(url)
    response_dict = response.json()
    pretty_print_dict(response_dict)
    more_specific_podcast_info(response_dict['results'][0]['collectionViewUrl'])

def more_specific_podcast_info(url: str):
    """Gets the number of episodes of a podcast and its description using an API and the URL of an itunes podcast"""
    response = requests.get(url)
    response_dict = response.json()
    print(response)

print(podcast_info("My Brother My Brother And Me"))
