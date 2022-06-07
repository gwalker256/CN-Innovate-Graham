import random

print ("Ghostbusters!\n")

starring = ["Bill Murray", "Dan Aykroyd", "Sigourney Weaver"]

for i in starring: 
    print (f"Starring {i}\n")

quotes = [
    "Dr. Peter Venkman: We came, we saw, we kicked its ass!", 
    "Dr. Peter Venkman: We've been going about this all wrong. This Mr. Stay Puft's okay! He's a sailor, he's in New York; we get this guy laid, we won't have any trouble!",
    "Winston Zeddemore: I'm Winston Zeddmore, Your Honor. I've only been with the company for a couple of weeks, but these things are real. Since I joined these men, I've seen shit that'll turn you white.",
    "Winston Zeddemore: Ray, when someone asks you if you're a god, you say, 'yes!'",
    "Dr. Raymond Stantz: Listen... you smell something"]

randomQuote = random.randint(0, 4)
print ("Random Quote: \n" + (quotes[randomQuote]))

win = False

def game():
    global win
    while win == False:    
        print ("g")
        win == True
game()

# while i < 6:
#   print(i)
#   i += 1