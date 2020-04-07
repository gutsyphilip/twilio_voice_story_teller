import json

with open('stories.json') as read_file:
    json_data = json.loads(read_file.read())
    
def load_story(story_number):
        return json_data[story_number - 1]

def get_stories_message():
    message = ""
    for idx, story in enumerate(json_data):
        message += f"To listen to {story['title']}, Press {idx+1}"
    return message