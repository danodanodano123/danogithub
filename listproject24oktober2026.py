import random
when = ["Yesterday, ", "Just now, ", "Once upon a time, ", "In 1987, ", "Last Christmas, ", "5 seconds ago, "]
who = ["a man ", "a woman ", "a robot ", "a ghost ", "a beetle ", "a bag of chips ", "a snowman ", "a dog ", "a cat "]
name = ["Beetlejuice ", "Penny ", "Barbara ", "Rendang ", "Couscous ", "Adams ", "LeBron ", "Chuck Norris ", "Michael Jackson "]
went = ["laundry ", "bar ", "bakery ", "Indomaret ", "mall ", "war museum ", "beach ", "White House ", "Arctic "]
act = ["caused a ruckus.", "had a lot of fun.", "got kicked out.", "made a lot of money.", "made a TikTok.", "met a zombie.", "fainted."]

print(random.choice(when) + random.choice(who) + "named " + random.choice(name) + "went to the " + random.choice(went) + "and " + random.choice(act))