from twilio.twiml.voice_response import VoiceResponse, Gather
from utils.stories import load_story,get_stories_message

def answer_call():
    """Respond to incoming phone calls with a menu of options"""
    # Start our TwiML response
    resp = VoiceResponse()
    resp.say("Welcome to the Twilio story teller application.")

    # Start our <Gather> verb
    gather = Gather(num_digits=1, action='/read-story')
    message = get_stories_message()
    gather.say(message)
    resp.append(gather)

    # If the user doesn't select an option, redirect them into a loop
    resp.redirect('/voice')

    return str(resp)

def read_story(story_number):
    # Start our TwiML response
    resp = VoiceResponse()
    # If Twilio's request to our app included already gathered digits,
    # process them
    if story_number:
        story = load_story(story_number)
        resp.say(story.content)
        return str(resp)
    else:
        # If the caller doesn't select an option with a story
        resp.say("Sorry, there is no story attached to that option at this time.")