import random

#Veriable to list all the available bosses we need the computer to pick from
boss = ("Barrows", "Wildy boss", "Nex", "Nightmare", "Tempoross", "Vorkath", "Wintertodt", "Zalcano", "Zulrah", "Cox", "Tob", "Toa", "Ba", "Giants Foundry", "GOTR", "Volcanic Mine", "CG") 
wildy_boss = ("Artio/Callisto", "Calvar'ion/Vet'ion", "Spindel/Venenatis", "Chaos Elemental", "Chaos Fanatic", "Crazy Archaeologist", "Scorpia")

#veriable to pick a boss from the list of bosses above and then print which boss has been assigned
chosen_boss = random.choice(boss)
print("You're assigned to do " + chosen_boss)

#if statement for if a wildy boss has been chosen and to then randomly pick from the wildy boss list
if chosen_boss == "Wildy boss":
    chosen_wildy_boss = random.choice(wildy_boss)
    print("Your assigned boss is " + chosen_wildy_boss)

#random number to define how many time you need to do the boss
boss_times = random.randint(10,50)

#if statement to define how many times you would need to do queen kills in barb assult as this would take longer to do one kill
if chosen_boss == "Ba":
    boss_times = random.randint(1,3)

#print statment to make the boss times a strong to display how many times you need to do the boss
print(str(boss_times) + " Times")