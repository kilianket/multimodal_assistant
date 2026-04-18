import requests

def get_image_from_nouns(query):
    url = f"https://source.unsplash.com/800x600/?{query}"
    return url