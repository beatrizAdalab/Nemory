import requests
import random

colors = ['amber', 'blue', 'blueGrey', 'brown', 'cyan', 'deepOrange', 'deepPurple', 'green', 'grey', 'indigo', 'lime', 'orange', 'pink', 'purple', 'red', 'teal']


def create_avatar(name, lastname):
    color_random = random.choice(colors)
    response = requests.get(f"https://avatars.dicebear.com/api/initials/{name}%20{lastname}.svg?options[radius]=50&options[backgroundColors][]={color_random}")
    print(response.text)
    return response.text


