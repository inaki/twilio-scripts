from flask import Flask, request, redirect
import twilio.twiml
import random

app = Flask(__name__)

# Try adding your own number to this list!
messages = [
    "meh",
    "Never give up, unless defeat arouses that girl in accounting",
    "Ignores previous fortunes",
    "You will die alone and poorly dressed.",
    "The fortune you seek is in another cookie, server yourself.",
    "Today is probably a huge improvement over yesterday",
    "Life will be happy, until the end, when you will pee yourself a lot.",
    "I am watching you!",
    "Stop eating cookies, there is other foods dude!",
    "An alien of some sort will be appearing to you shortly",
    "Vampires will soon strike you if you do not bring more beer to the party.",
    "You will live a long happy life and eat lot of great cookies",
    "Smile to other people, is the right thing to do.",
    "Fortune Not Found: Abort, Retry, Ignore?",
    "run",
    "You laugh now, wait till you get home",
    "When you squeeze an orange, orange juice comes out -- because that is what is inside.",
    "Wait, do not eat this cookie, is...", "Do or do not. There is no try.",
    "You are free to invent your life.",
    "Good sense is the master of human life.",
    "Don't panic, but someone follow you.",
    "Wise people know that they don't know a lot of shit they don't know",
    "It could be better, but is good enough.",
    "Ignorance never settles a question.",
    "A person is never to old to learn how to code",
    "A party without beer is not a party, do your part",
    "You are busy, but you are happy",
    "You are almost there",
    "You are in good hands this evening.",
    "You are talented in many ways",
    "You look pretty",
    "You will make change for the better",
    "Your dreams are never silly; depend on them to guide you."
]

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""

    message = messages[random.randint(0, len(messages))]

    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
