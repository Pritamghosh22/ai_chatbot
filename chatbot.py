import random
import re

class LifeBot:
    negative_res = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    
    
    random_question = (
        "Are you feeling okay today?",
        "Did you eat your food on time?",
        "Have you taken enough rest?",
        "Did you drink enough water today?",
        "Are you feeling happy right now?"
    )
    
    def __init__(self):
        self.life_patterns = {
            'feeling_intent': r'.*\s*(sad|happy|ok|fine|not well).*',
            'food_intent': r'.*\s*(food|eat|meal|hungry).*',
            'sleep_intent': r'.*\s*(sleep|rest|tired).*',
            'water_intent': r'.*\s*(drink|water|thirsty).*'
        }
    
    def greet(self):
        self.name = input("What is your name?\n")
        will_chat = input(f"Hi {self.name}, I'm LifeBot. Can I ask you about your day?\n")
        if will_chat.lower() in self.negative_res:
            print("Okay, take care and have a good day!")
            return 
        self.chat()
        
    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Goodbye! Stay healthy and take care.")
                return True

    def chat(self):
        reply = input(random.choice(self.random_question) + "\n").lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply) + "\n").lower()
            
    def match_reply(self, reply):
        for intent, regex_pattern in self.life_patterns.items():
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'feeling_intent':
                return self.feeling_response()
            elif found_match and intent == 'food_intent':
                return self.food_response()
            elif found_match and intent == 'sleep_intent':
                return self.sleep_response()
            elif found_match and intent == 'water_intent':
                return self.water_response()
        
        return self.no_match_intent() 
    
    def feeling_response(self):
        responses = (
            f"I'm glad to hear how you feel, {self.name}.",
            "Your feelings matter. Do you want to share more?",
            "I care about your emotions."
        )
        return random.choice(responses)
    
    def food_response(self):
        responses = (
            "Eating on time keeps you strong.",
            "Food is important, don't skip meals.",
            "I hope you had something healthy today."
        )
        return random.choice(responses)
    
    def sleep_response(self):
        responses = (
            "Rest is important, don't forget to sleep well.",
            "Sleep recharges your mind and body.",
            "A short nap can also help if you're tired."
        )
        return random.choice(responses)
    
    def water_response(self):
        responses = (
            "Water keeps you refreshed, drink enough.",
            "Staying hydrated is key to good health.",
            "Maybe have a glass of water right now?"
        )
        return random.choice(responses)
    
    def no_match_intent(self):
        responses = (
            "Tell me more about your day.",
            "I'm listening, go on.",
            "That's interesting, share more with me.",
            "Hmm, can you explain more?"
        )
        return random.choice(responses)


bot = LifeBot()
bot.greet()
