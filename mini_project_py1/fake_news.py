import random

#now we make 3 lists of strings
subjects = [
    "Dr. A.P.J. Abdul Kalam",
    "Sachin Tendulkar",
    "Ratan Tata",
    "Kalpana Chawla",
    "Lata Mangeshkar",
    "Satyajit Ray",
    "Mary Kom",
    "C.V. Raman"
]
actions = [
    "launches a rocket made of bamboo",
    "dances with a robot",
    "declares war on boredom",
    "celebrates with rasgulla rain",
    "cancels gravity for a day",
    "paints the sky with poetry",
    "starts a startup for cows",
    "codes in Sanskrit"
]

places_or_things = [
    "in Red Fort",
    "in Mumbai Local Train",
    "a plate of samosas",
    "inside Parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "on a Kolkata tram",
    "under a banyan tree",
    "with a chai stall",
    "at Howrah Bridge",
    "in a Durga Puja pandal",
    "on top of Victoria Memorial"
]
# start the headline generation loop 
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    
    headline = f"{subject} {action} {place_or_thing}!"
    print(headline)
    
    user_input = input("Generate another headline? (yes/no): ").strip()
    if user_input.lower() != 'yes':
        break
#place a goodbye message 
print("Thanks for using the Fake News Generator! Stay curious!")