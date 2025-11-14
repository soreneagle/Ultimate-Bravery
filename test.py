import random

killer = """A Nurse's Calling
Agitation
Alien Instinct
All-Shaking Thunder
Awakened Awareness
Bamboozle
Barbecue & Chilli
Batteries Included
Beast of Prey
Bitter Murmur
Blood Echo
Blood Warden
Bloodhound
Brutal Strength
Call of Brine
Corrupt Intervention
Coulrophobia
Coup de Grâce
Cruel Limits
Dark Arrogance
Dark Devotion
Darkness Revealed
Dead Man's Switch
Deathbound
Deerstalker
Discordance
Dissolution
Distressing
Dominance
Dragon's Grip
Dying Light
Enduring
Eruption
Fire Up
Forced Hesitation
Forced Penance
Forever Entwined
Franklin's Demise
Friends 'til the End
Furtive Chase
Game Afoot
Gearhead
Genetic Limits
Grim Embrace
Haywire
Help Wanted
Hex: Blood Favour
Hex: Crowd Control
Hex: Devour Hope
Hex: Face the Darkness
Hex: Fortune's Fool
Hex: Haunted Ground
Hex: Huntress Lullaby
Hex: No One Escapes Death
Hex: Nothing But Misery
Hex: Pentimento
Hex: Retribution
Hex: Ruin
Hex: The Third Seal
Hex: Thrill of the Hunt
Hex: Two Can Play
Hex: Undying
Hex: Wretched Fate
Hoarder
Hubris
Human Greed
Hysteria
I'm All Ears
Infectious Fright
Insidious
Iron Grasp
Iron Maiden
Knock Out
Languid Touch
Lethal Pursuer
Leverage
Lightborn
Machine Learning
Mad Grit
Make Your Choice
Merciless Storm
Mindbreaker
Monitor & Abuse
Nemesis
No Holds Barred
No Quarter
No Way Out
None Are Free
Nowhere to Hide
Oppression
Overcharge
Overwhelming Presence
Phantom Fear
Play with Your Food
Pop Goes the Weasel
Predator
Rancor
Rapid Brutality
Remember Me
Save the Best for Last
Scourge Hook: Floods of Rage
Scourge Hook: Hangman's Trick
Scourge Hook: Jagged Compass
Scourge Hook: Monstrous Shrine
Scourge Hook: Pain Resonance
Scourge Hook: Weeping Wounds
Septic Touch
Shadowborn
Shattered Hope
Sloppy Butcher
Spies from the Shadows
Spirit Fury
Starstruck
Stridor
Superior Anatomy
Surge
Surveillance
THWACK!
Terminus
Territorial Imperative
Thanatophobia
Thrilling Tremors
Tinkerer
Trail of Torment
Ultimate Weapon
Unbound
Undone
Unforeseen
Unnerving Presence
Unrelenting
Weave Attunement
Whispers
Zanshin Tactics"""
survivor = """Ace in the Hole"""

killer_perks = []
survivor_perks = []

with open ("killer.txt", "r") as file:
      for line in file:
            clean_line = line.strip("\n")
            killer_perks.append(clean_line)

with open ("survivor.txt", "r") as file:
      for line in file:
            clean_line = line.strip("\n")
            survivor_perks.append(clean_line)
            
def get_perks():
    killer_perks = []
    survivor_perks = []

    with open ("killer.txt", "r") as file:
        for line in file:
                clean_line = line.strip("\n")
                killer_perks.append(clean_line)

    with open ("survivor.txt", "r") as file:
        for line in file:
                clean_line = line.strip("\n")
                survivor_perks.append(clean_line)

    message = ""

    for i in range(1, 5):
        print(f"Survivor {i}:")
        perks = random.sample(survivor_perks, 4)
        message += f"  * {perks[0]}\n"
        message += f"  * {perks[1]}\n"
        message += f"  * {perks[2]}\n"
        message += f"  * {perks[3]}\n\n"

    print(f"Killer: ")
    k_perks = random.sample(killer_perks, 4)
    message += f"  * {k_perks[0]}\n"
    message += f"  * {k_perks[1]}\n"
    message += f"  * {k_perks[2]}\n"
    message += f"  * {k_perks[3]}\n\n"

    return message

get_perks()