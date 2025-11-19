"""
Sunshine Coast Puzzle Date – Puzzle & Picnic Quest
Falafel + Dips + Prosciutto + Olives + Greens + Sweet Treat (No-Cook Lunch)

Controls:
- Type your answer and press Enter
- Type 'hint' for a clue for that stage
- Type 'q' to quit
"""
import streamlit as st
from dataclasses import dataclass
from typing import List


@dataclass
class Stage:
    number: int
    name: str
    prompt: str
    acceptable_answers: List[str]
    hint: str


def normalize(text: str) -> str:
    """Normalize text for comparison: lowercase, remove non-alphanumeric."""
    return "".join(ch.lower() for ch in text if ch.isalnum())


def run_adventure(stages: List[Stage]) -> None:
    print("🌴 Sunshine Coast Puzzle Date – Puzzle & Picnic Quest 🌴")
    print("Type your answer for each stage.")
    print("You can also type 'hint' for a clue or 'q' to quit.\n")

    for stage in stages:
        print(f"\n--- Stage {stage.number}: {stage.name} ---")
        print(stage.prompt)

        normalized_accept = [normalize(ans) for ans in stage.acceptable_answers]

        while True:
            user_input = input("Your answer (or 'hint' / 'q'): ").strip()

            if user_input.lower() == "q":
                print("Adventure ended early. 👋")
                return

            if user_input.lower() == "hint":
                print(f"💡 Hint: {stage.hint}\n")
                continue

            user_norm = normalize(user_input)

            if user_norm in normalized_accept:
                print("✅ Correct! Moving to the next stage...")
                break
            else:
                print("❌ Not quite. Try again!\n(You can type 'hint' if you're stuck.)")

    print("\n🎉 You’ve completed all stages of the Sunshine Coast Puzzle Date! 🎉")


def main():
    stages = [

        # ------------------------- #
        #   STAGE 1 – KUNARA CODE   #
        # ------------------------- #

        Stage(
            number=1,
            name="Organic Marketplace – Number Code",
            prompt=(
                "PUZZLE 1 – NUMBER CODE (A=1, B=2, ... Z=26)\n\n"
                "This is your FIRST stop of the day.\n"
                "Your opening card shows a single row of numbers:\n\n"
                "  11   21   14   1   18   1\n\n"
                "Instruction on the card:\n"
                "  'Use A=1, B=2, C=3 ... Z=26 to turn these numbers into letters.\n"
                "   The result is the name of the big organic marketplace where your\n"
                "   adventure begins.'\n\n"
                "TRAVEL ONCE SOLVED:\n"
                "After you decode the name, actually DRIVE there in Forest Glen.\n"
                "- Park in the main front car park.\n\n"
                "ROMANTIC PROMPT (ON THE DRIVE):\n"
                "Ask each other:\n"
                "  • If we ran our own little organic café or deli, what would we call it?\n\n"
                "Type the name that the code spells:"
            ),
            acceptable_answers=[
                "Kunara",
                "Kunara Organic Marketplace",
                "Kunara Organics",
                "Kunara Organic Market",
            ],
            hint="Turn each number into a letter and you’ll get a six-letter name you’ll see huge on a sign at Forest Glen.",
        ),

        # ------------------------- #
        #   STAGE 2 – FALAFEL       #
        # ------------------------- #

        Stage(
            number=2,
            name="Crispy Chickpea Balls – Menu Cipher",
            prompt=(
                "TRAVEL:\n"
                "You are now at the organic marketplace. Head inside and walk to the\n"
                "fridge/ready-meal section.\n\n"
                "PUZZLE 2 – MENU CIPHER\n"
                "On a ready-meal shelf you see this note:\n\n"
                "  F _ L A _ E L\n\n"
                "Two letters are missing but the card says:\n"
                "  'Add the same letter twice to complete the name of\n"
                "   the crispy chickpea balls you're buying.'\n\n"
                "ROMANTIC PROMPT:\n"
                "Ask each other:\n"
                "  • If we travelled somewhere in the Middle East together,\n"
                "    which country would you want to go to first, and why?\n\n"
                "Fill in the blanks and type the word:"
            ),
            acceptable_answers=[
                "falafel",
                "falafels",
            ],
            hint="Think of the classic chickpea street food you’d wrap with salad and sauce.",
        ),

        # ------------------------- #
        #   STAGE 3 – OLIVES        #
        # ------------------------- #

        Stage(
            number=3,
            name="Salty Antipasto – Number Word Puzzle",
            prompt=(
                "TRAVEL:\n"
                "Still in the marketplace – head to the deli / antipasto area.\n\n"
                "PUZZLE 3 – TWO-ROW NUMBER CODE\n"
                "Your card shows two rows of numbers, using A=1, B=2, ..., Z=26:\n\n"
                "  15   12   9\n"
                "  22   5   19\n\n"
                "Instruction on the card:\n"
                "  'Decode BOTH rows.\n"
                "   Row 1 is the first part of the word.\n"
                "   Row 2 is the second part.\n"
                "   Together they name a salty ingredient we’re buying –\n"
                "   it’s a SINGLE word split across two rows.'\n\n"
                "ROMANTIC PROMPT (WHILE YOU TASTE TEST):\n"
                "Ask each other:\n"
                "  • Are you more of a 'sweet tooth' or 'olive/cheese board' person?\n\n"
                "Type the ingredient you decode:"
            ),
            acceptable_answers=[
                "olives",
                "marinated olives",
                "greek olives",
                "kalamata olives",
            ],
            hint="Decode both rows and think of something briny that often comes marinated in jars.",
        ),

        # ------------------------- #
        #   STAGE 4 – PROSCIUTTO    #
        # ------------------------- #

        Stage(
            number=4,
            name="Delicate Cured Meat – Hidden Inside",
            prompt=(
                "TRAVEL:\n"
                "Still in the marketplace – walk to the deli / cold meats section.\n\n"
                "PUZZLE 4 – HIDDEN INSIDE A SENTENCE\n"
                "Your next card reads:\n\n"
                "  'I'm a delicate cured meat that PROtectS Chefs In Unbelievably\n"
                "   Tender TOasts when shaved paper-thin.'\n\n"
                "Look carefully: the capitals hide the word.\n\n"
                "ROMANTIC PROMPT:\n"
                "Ask each other:\n"
                "  • Are you more into light, delicate foods or big hearty meals?\n\n"
                "Type the meat's name:"
            ),
            acceptable_answers=[
                "prosciutto",
                "proscuitto",
            ],
            hint="Read ONLY the capital letters in order; they spell an Italian-style cured ham.",
        ),

        # ------------------------- #
        #   STAGE 5 – GREENS        #
        # ------------------------- #

        Stage(
            number=5,
            name="Greens – LOVE Vowel Puzzle",
            prompt=(
                "TRAVEL:\n"
                "Still at the marketplace – head to the fresh produce / salad section.\n\n"
                "PUZZLE 5 – ONLY VOWELS FROM 'LOVE'\n"
                "Your card shows some nearly-complete words:\n\n"
                "  R _ C K E T\n"
                "  B _ B Y  SP N CH\n"
                "  S L _ D  M X\n"
                "  M X _ D  L E _ V E S\n\n"
                "Instruction on the card:\n"
                "  'You may ONLY use the vowels that appear in the word LOVE (O and E),\n"
                "   plus A once where you really need it, because salads deserve it.\n"
                "   Fill the blanks to form REAL leafy salad ingredients.\n"
                "   Choose ONE of the valid greens for your sandwich and type its name.'\n\n"
                "ROMANTIC PROMPT (WHILE CHOOSING GREENS):\n"
                "Ask each other:\n"
                "  • What does a 'healthy day' look like for you – food, movement, rest?\n\n"
                "Type the name of the greens you pick:"
            ),
            acceptable_answers=[
                "rocket",
                "baby spinach",
                "spinach",
                "spinach leaves",
                "salad greens",
                "mixed salad greens",
                "salad mix",
                "mixed leaves",
                "mesclun",
            ],
            hint="Imagine the actual leaf names you’d see printed on salad or mesclun bags.",
        ),

        # ------------------------- #
        #   STAGE 6 – LIGHTHOUSE    #
        # ------------------------- #

        Stage(
            number=6,
            name="Coastal Lighthouse Acrostic",
            prompt=(
                "TRAVEL TO THIS STAGE:\n"
                "From the organic marketplace, DRIVE out to the coast to a well-known\n"
                "lighthouse on a headland.\n"
                "- Drive time: roughly 15–20 minutes.\n\n"
                "PUZZLE 6 – SIMPLE ACROSTIC\n"
                "Take the FIRST letter of each line to reveal where you are heading.\n\n"
                "  Pillars of white rise where the seas collide,\n"
                "  Over looking the mouth where the river is wide.\n"
                "  In storms and calm I shine through the night,\n"
                "  Navigating sailors with my sweeping light.\n"
                "  Tall on the headland, a steadfast sight.\n\n"
                "The first letters spell the start of this landmark’s name.\n\n"
                "ROMANTIC PROMPT:\n"
                "When you reach the headland, ask each other:\n"
                "  • What’s one place by the ocean that feels like 'home' to you, and why?\n\n"
                "Type the full landmark name:"
            ),
            acceptable_answers=[
                "Point Cartwright Lighthouse",
                "Point Cartwright",
                "Cartwright Lighthouse",
            ],
            hint="Read down the first letters of each line; they give you a 5-letter word at the start of the lighthouse name.",
        ),

        # ------------------------- #
        #   STAGE 7 – CAFE RIDDLE   #
        # ------------------------- #

        Stage(
            number=7,
            name="Warehouse Café – Hidden Name",
            prompt=(
                "TRAVEL TO THIS STAGE:\n"
                "From the lighthouse, DRIVE along the coast to a converted\n"
                "warehouse-style café near the beach in Mooloolaba.\n"
                "- Drive time: around 7–10 minutes.\n"
                "- Park along a nearby street or the Esplanade.\n\n"
                "PUZZLE 7 – REVEAL THE CAFE NAME\n"
                "Your card shows a little story:\n\n"
                "  'We roll up to a hidden spot near the sand.\n"
                "   Inside, old BIKE frames hang on the walls,\n"
                "   and worn-out WHEELS rest in every corner.\n"
                "   It feels like a secret PROJECT someone built\n"
                "   just for riders who want good coffee.'\n\n"
                "On the back of the card, another clue:\n\n"
                "  'Take the idea of a BIKE and a PROJECT.\n"
                "   Think of a two-word café name that fits:\n"
                "   first a word for a type of bike, then a word for a plan.'\n\n"
                "ROMANTIC PROMPT (AT THE TABLE):\n"
                "While you wait for food, ask each other:\n"
                "  • If we could teleport to any café in the world right now, where would you pick?\n\n"
                "Type the café’s name:"
            ),
            acceptable_answers=[
                "The Velo Project",
                "Velo Project",
            ],
            hint="Think of a French-ish word tied to bicycles plus a word meaning 'plan' or 'task'.",
        ),

        # ------------------------- #
        #   STAGE 8 – ROCK POOLS    #
        # ------------------------- #

        Stage(
            number=8,
            name="Rock Pools – Alphabet Number Code",
            prompt=(
                "TRAVEL TO THIS STAGE:\n"
                "From the café, head to the rock pools near the Spit.\n"
                "- Best: DRIVE ~3 minutes to the Mooloolaba Spit car park (easy parking).\n"
                "- Optional: WALK ~18–20 minutes along the esplanade if you want a longer stroll.\n\n"
                "PUZZLE 8 – A=1, B=2, C=3… CODE\n"
                "Your card shows two rows of numbers:\n\n"
                "  18   15   3   11\n"
                "  16   15   15   12   19\n\n"
                "Instruction on the card:\n"
                "  'Use A=1, B=2, C=3 ... Z=26 to turn these numbers into letters.'\n"
                "  Row 1 spells the first word; row 2 spells the second.\n\n"
                "ROMANTIC PROMPT (ON THE WAY / WALKING):\n"
                "Ask each other:\n"
                "  • What’s your favourite childhood memory of the beach or rock pools?\n\n"
                "Once you decode the words, they tell you where to go next.\n\n"
                "Type the full location name (you can include the suburb if you like):"
            ),
            acceptable_answers=[
                "Rock Pools",
                "The Rock Pools",
                "Mooloolaba Rock Pools",
                "Rock Pools Mooloolaba",
                "Rockpools",
            ],
            hint="Turn each number into a letter; you’ll literally spell what this place physically is.",
        ),

        # ------------------------- #
        #   STAGE 9 – GELATO + GPS  #
        # ------------------------- #

        Stage(
            number=9,
            name="Frozen Treat – Secret GPS Coordinates",
            prompt=(
                "TRAVEL TO THIS STAGE:\n"
                "From the rock pools, WALK along the beach and path back toward the\n"
                "Mooloolaba Esplanade.\n"
                "- Walk time: about 12–15 minutes, relaxed pace.\n\n"
                "PUZZLE 9A – WHAT ARE YOU ABOUT TO EAT?\n"
                "Take the FIRST letter of each line:\n\n"
                "  Glistening scoops wait in frosty rows,\n"
                "  Every flavour shining under the glass,\n"
                "  Laughter spills out as people choose their favourites,\n"
                "  Afternoons here taste like holidays,\n"
                "  Tasting sunshine in every cold mouthful,\n"
                "  On the esplanade, hearts and hands both full.\n\n"
                "The first letters spell the name of the sweet Italian treat\n"
                "you’re about to order together.\n\n"
                "PUZZLE 9B – SECRET GPS COORDINATES (HARDER, OPTIONAL)\n"
                "Below the poem, your card has a second puzzle:\n\n"
                "  'Use the first TEN letters of the alphabet as digits:\n"
                "     A = 0,  B = 1,  C = 2,  D = 3,  E = 4,\n"
                "     F = 5,  G = 6,  H = 7,  I = 8,  J = 9.\n\n"
                "   Each CAPITAL letter hidden in the next lines is part\n"
                "   of a six-letter code. The first six lines give LATITUDE,\n"
                "   the next six give LONGITUDE.'\n\n"
                "LATITUDE code (first 6 lines):\n"
                "  in the shoCk of cold, the first lick wakes you up\n"
                "  gelato driGps lazily down the side of the cone\n"
                "  a little Giggle escapes as you try to catch it\n"
                "  the marina wInd brushes sunlight across your face\n"
                "  a small Breeze crosses the path between you\n"
                "  you notIce the boats rocking gently in the harbour\n\n"
                "LONGITUDE code (next 6 lines):\n"
                "  nearby taBles fill with holiday chatter\n"
                "  best Friends savour every last mouthful\n"
                "  someone orDers another round of scoops\n"
                "  a soft Breeze rolls in from the channel\n"
                "  cafe musiC drifts out through the doorway\n"
                "  the same maGic pulls you both further into the evening\n\n"
                "Instruction on the card:\n"
                "  'Turn each capital letter into a digit using A=0, B=1, ..., J=9.\n"
                "   • For LATITUDE (first 6 capitals), write the six digits and put\n"
                "     a decimal point after the first TWO digits.\n"
                "   • For LONGITUDE (next 6 capitals), write the six digits and put\n"
                "     a decimal point after the first THREE digits.\n\n"
                "   One number is SOUTH of the equator and the other is EAST of\n"
                "   Greenwich. Think about where Queensland is on the globe and\n"
                "   add S and E in the obvious way.'\n\n"
                "These numbers give you the GPS coordinates of where you're standing –\n"
                "right by your treat.\n\n"
                "ROMANTIC PROMPT (WHILE EATING):\n"
                "Ask each other:\n"
                "  • If you could freeze this exact moment and come back to it\n"
                "    any time in the future, what tiny detail would you want\n"
                "    to remember most?\n\n"
                "Now, for the game, just type the SIX-LETTER ITALIAN WORD\n"
                "you decoded in Puzzle 9A:"
            ),
            acceptable_answers=[
                "gelato",
            ],
            hint="Read down the first letters of the poem lines; it’s the classic Italian word for this kind of frozen dessert.",
        ),

        # ------------------------- #
        #   STAGE 10 – HEADLAND     #
        # ------------------------- #

        Stage(
            number=10,
            name="Headland Lookout – Coastal Acrostic",
            prompt=(
                "TRAVEL TO THIS STAGE:\n"
                "From the esplanade, DRIVE north along the coast to a well-known headland.\n"
                "- Drive time: ~4 minutes.\n"
                "- Park at the bluff car park or near the surf club/lookout.\n\n"
                "PUZZLE 10 – SHORT ACROSTIC\n"
                "Your next clue is a small poem:\n\n"
                "  A rocky bluff sits between two shining beaches,\n"
                "  Little lines of surfers wait out the back,\n"
                "  Endless sets peel along the point at sunset,\n"
                "  X-marks the bend in the coast that locals love.\n\n"
                "Instruction on the card:\n"
                "  'Take the FIRST letter of each line to find the nickname locals use\n"
                "   for this headland.'\n\n"
                "ROMANTIC PROMPT (AT THE LOOKOUT):\n"
                "Ask each other:\n"
                "  • If we could watch the sunset from any place in the world\n"
                "    (cliff, mountain, city, beach), where would you choose?\n\n"
                "Type the headland / area name:"
            ),
            acceptable_answers=[
                "Alexandra Headland",
                "Alex Headland",
                "The Bluff",
                "Alex Bluff",
                "Alex",
            ],
            hint="The initials of the four lines form a short nickname surfers use all the time.",
        ),

        # ------------------------- #
        #   STAGE 11 – WHOLEFOODS   #
        # ------------------------- #

        Stage(
            number=11,
            name="Coastal Whole-Food Store – Choice Puzzle",
            prompt=(
                "TRAVEL TO THIS STAGE:\n"
                "From the headland, DRIVE to a coastal whole-foods area around Maroochydore.\n"
                "- Drive time: 6–8 minutes.\n\n"
                "PUZZLE 11 – MULTI-ANSWER LOCATION RIDDLE\n"
                "Your map has three health/organic stores circled around\n"
                "Maroochydore. The note says:\n\n"
                "  'There are three options:\n"
                "   • A coastal organic supermarket with green signage.\n"
                "   • A healthfoods and pharmacy hybrid.\n"
                "   • A smaller wholefood market on Wises Rd.\n\n"
                "   Choose ANY ONE of these as your ingredient stop.\n"
                "   The adventure continues no matter which you pick.'\n\n"
                "ROMANTIC PROMPT (PARKED OUTSIDE):\n"
                "Ask each other:\n"
                "  • If we cooked together regularly, what kind of food\n"
                "    do you imagine us making the most?\n\n"
                "Type the name of the store you actually go to:"
            ),
            acceptable_answers=[
                "Flannerys",
                "Flannerys Maroochydore",
                "Flannerys Organic and Wholefood Market",
                "Wholelife",
                "Wholelife Maroochydore",
                "Wholelife Healthfoods Maroochydore",
                "Fundies",
                "Fundies Maroochydore",
                "Fundies Wholefood Market",
            ],
            hint="Pick one of the well-known organic/health stores in Maroochydore that fits those descriptions.",
        ),

        # ------------------------- #
        #   STAGE 12 – DIPS         #
        # ------------------------- #

        Stage(
            number=12,
            name="Dips – Riddle of the Spread",
            prompt=(
                "TRAVEL:\n"
                "You are already inside your chosen coastal whole-food store.\n"
                "Just walk to the chilled section.\n\n"
                "PUZZLE 12 – FOOD RIDDLE\n"
                "Inside the store, your clue for the next ingredient says:\n\n"
                "  'I hide in tubs along the chilled wall,\n"
                "   I'm scooped or spread at every picnic and stall.\n"
                "   Chickpeas or yoghurt, beetroot so bright,\n"
                "   I'm perfect with bread in the soft afternoon light.'\n\n"
                "ROMANTIC PROMPT (CHOOSING DIPS):\n"
                "Ask each other:\n"
                "  • What’s your ultimate dream picnic spread?\n\n"
                "Name ONE dip you choose for your sandwich (e.g. hummus, tzatziki):"
            ),
            acceptable_answers=[
                "hummus",
                "houmous",
                "baba ganoush",
                "baba ganouj",
                "tzatziki",
                "beetroot dip",
                "dip",
            ],
            hint="Think of savoury spreads you scoop from tubs to go with bread and salad.",
        ),

        # ------------------------- #
        #   STAGE 13 – BREAD        #
        # ------------------------- #

        Stage(
            number=13,
            name="Bread – Texture Puzzle",
            prompt=(
                "TRAVEL:\n"
                "Still inside the same store – now walk to the bakery / bread section.\n\n"
                "PUZZLE 13 – TEXTURE & CRUST\n"
                "The card reads:\n\n"
                "  'I crackle when you squeeze me,\n"
                "   I can be long or round or flat.\n"
                "   I'm born in a bakery and die in a sandwich.\n"
                "   Without me, the fillings fall flat.'\n\n"
                "ROMANTIC PROMPT (CHOOSING BREAD):\n"
                "Ask each other:\n"
                "  • Are you more 'crusty sourdough' or 'soft Turkish' as a personality?\n\n"
                "Type the style of bread you pick (e.g. sourdough, ciabatta, Turkish bread):"
            ),
            acceptable_answers=[
                "sourdough",
                "ciabatta",
                "turkish bread",
                "turkish",
                "baguette",
                "rustic loaf",
                "bread",
            ],
            hint="Choose a loaf that would make a great base for a big, stacked sandwich.",
        ),

        # ------------------------- #
        #      PICNIC & TREAT       #
        # ------------------------- #

        Stage(
            number=14,
            name="Picnic – Bushland Garden Riddle",
            prompt=(
                "TRAVEL TO THIS STAGE:\n"
                "From the coastal shopping area, DRIVE to a bushland botanic garden\n"
                "in Tanawha.\n"
                "- Drive time: about 8–10 minutes.\n"
                "- Park in the main visitor car park, then WALK a short way to\n"
                "  a picnic table or sculpture garden area.\n\n"
                "PUZZLE 14 – GARDEN RIDDLE\n"
                "With all your ingredients packed, your next riddle says:\n\n"
                "  'Find the garden where art meets trees,\n"
                "   Where stone and steel share space with leaves.\n"
                "   Not by the sea, but not too far,\n"
                "   A BUSHLAND BOTANIC hidden star.'\n\n"
                "ROMANTIC PROMPT (AT THE PICNIC):\n"
                "Ask each other:\n"
                "  • If we could pause time for 24 hours and stay in this exact moment,\n"
                "    what would you want to do together in that time?\n\n"
                "This is where you assemble your sandwich: dips + falafel + cured meat\n"
                "+ olives + greens and share lunch.\n\n"
                "Type the place in simple words:"
            ),
            acceptable_answers=[
                "botanic garden",
                "botanic gardens",
                "bushland botanic garden",
                "maroochy botanic garden",
                "maroochy bushland botanic garden",
            ],
            hint="Keep it simple – you’re in a kind of 'botanic garden' in the bushland at Tanawha.",
        ),

        Stage(
            number=15,
            name="Sweet Treat Place – Wildcard Puzzle",
            prompt=(
                "TRAVEL TO THIS STAGE:\n"
                "After lunch at the garden, DRIVE to any dessert / sweet-treat spot\n"
                "you like (Mooloolaba, Alex, or Maroochydore work well).\n"
                "- Drive time: about 10–15 minutes depending on where you go.\n\n"
                "PUZZLE 15 – CHOICE-BASED CLUE\n"
                "After lunch, a small card in your bag says:\n\n"
                "  'You've mastered savoury – now find something sweet.\n"
                "   Choose any place that makes your heart beat.\n"
                "   Rings of dough? Frozen bowls? A raw treat stack?\n"
                "   Just write what KIND of shop you're heading back.'\n\n"
                "In real life, go to ANY dessert / sweet-treat spot you like nearby.\n\n"
                "ROMANTIC PROMPT (AT THE COUNTER):\n"
                "Ask each other:\n"
                "  • What's your go-to 'treat' when you've had a huge week?\n\n"
                "For the game, type the STYLE of place you chose, e.g.:\n"
                "  donut shop / dessert bar / acai bar / healthy cafe / bakery"
            ),
            acceptable_answers=[
                "donut shop",
                "doughnut shop",
                "dessert bar",
                "acai bar",
                "acai place",
                "healthy cafe",
                "healthy café",
                "bakery",
            ],
            hint="You’re just naming the category of dessert place, not its specific brand.",
        ),

        Stage(
            number=16,
            name="Sweet Treat – Menu Choice",
            prompt=(
                "TRAVEL:\n"
                "You're now at your chosen dessert place.\n\n"
                "PUZZLE 16 – MENU CHOICE\n"
                "Your sweet clue says:\n\n"
                "  'Pick something that balances us:\n"
                "   a little JOY, a little NOURISH.\n"
                "   It might be round with icing,\n"
                "   blended in a bowl,\n"
                "   rolled into a ball,\n"
                "   or sliced from something whole.'\n\n"
                "ROMANTIC PROMPT:\n"
                "Ask each other:\n"
                "  • If our relationship was a dessert, what would it be and why?\n\n"
                "Type what you actually ordered (e.g. donut, acai bowl, bliss ball, raw slice):"
            ),
            acceptable_answers=[
                "donut",
                "doughnut",
                "acai bowl",
                "acai",
                "bliss ball",
                "raw slice",
                "brownie",
                "healthy brownie",
                "protein ball",
            ],
            hint="Just write the treat that ended up in front of you.",
        ),

        # ------------------------- #
        #     WALK & ROMANCE        #
        # ------------------------- #

        Stage(
            number=17,
            name="Riverwalk – Location Cipher",
            prompt=(
                "TRAVEL TO THIS STAGE:\n"
                "From your dessert place, DRIVE to a riverfront walk at Cotton Tree.\n"
                "- Drive time: about 4–7 minutes.\n"
                "- Park near the riverside park or along The Esplanade.\n\n"
                "PUZZLE 17 – LETTER STRIP\n"
                "Your river clue is written as jumbled chunks:\n\n"
                "  TREE   COT   RIV   WALK\n\n"
                "Rearrange these into a sensible two or three word place name\n"
                "along the river where the suburb is also in the name.\n\n"
                "ROMANTIC PROMPT (START OF THE WALK):\n"
                "Ask each other:\n"
                "  • When do you feel most at peace in nature – ocean, river, forest, mountains?\n\n"
                "Type the location:"
            ),
            acceptable_answers=[
                "Cotton Tree Riverwalk",
                "Cotton Tree",
                "Cotton Tree River Park",
                "Cotton Tree Park",
            ],
            hint="Put the suburb word first, then a phrase for the river path or park there.",
        ),

        Stage(
            number=18,
            name="Love Riddle – Reflection Puzzle",
            prompt=(
                "TRAVEL:\n"
                "You are already at the riverwalk – just WALK a little along\n"
                "the riverside path together.\n\n"
                "PUZZLE 18 – LOVE RIDDLE\n"
                "At the river, your final thinking puzzle reads:\n\n"
                "  'Look for three things:\n"
                "   1. Something MOVING – like water or wind.\n"
                "   2. Something REFLECTED – in the surface or glass.\n"
                "   3. Something STILL – a rock, a tree, or just your quiet breath.\n\n"
                "   Which of these feels most like LOVE to you?'\n\n"
                "There is no wrong answer – just what feels true.\n\n"
                "ROMANTIC PROMPT (AFTER ANSWERING):\n"
                "Share with each other:\n"
                "  • Why did you choose that word? What about your connection feels like that?\n\n"
                "Type your chosen word (moving / reflected / still):"
            ),
            acceptable_answers=[
                "moving",
                "reflected",
                "still",
            ],
            hint="This is about how it feels, not being 'correct'. Pick the word that resonates.",
        ),

        Stage(
            number=19,
            name="Final Romantic Diagonal – Hidden Sentence",
            prompt=(
                "TRAVEL:\n"
                "Stay right here on the riverwalk, maybe pause somewhere quiet with a view.\n\n"
                "PUZZLE 19 – HIDDEN SENTENCE IN REAL WORDS\n"
                "Your last card looks like a block of perfectly normal sentences –\n"
                "except each line hides ONE capital letter somewhere in the middle.\n"
                "The note says:\n\n"
                "  'In each line there is exactly ONE CAPITAL letter.\n"
                "   Read those capital letters from TOP to BOTTOM\n"
                "   to reveal what you already feel.'\n\n"
                "The card reads:\n\n"
                "  lazy daYs leave golden light on the water\n"
                "  soft fOam gathers gently at our feet\n"
                "  sea spray wraps aroUnd us as we laugh\n"
                "  this place alwAys feels like a secret\n"
                "  under youR gaze the world slows down\n"
                "  every small dEtail suddenly matters\n"
                "  together we sTand by the rivers edge\n"
                "  the wind brusHes your hair across your face\n"
                "  therE is nowhere else i'd rather be\n"
                "  being with you is a Bright kind of calm\n"
                "  even quiet momEnts feel full with you\n"
                "  shared silence growS into something warm\n"
                "  this liTtle walk turns into a memory\n"
                "  each moment we sPend here feels gentle\n"
                "  and your lAugh fits perfectly in this place\n"
                "  i can heaR my own heartbeat settle\n"
                "  the preseT feels better than any future plan\n"
                "  only nOw really seems to matter\n"
                "  fresh river air Fills my lungs slowly\n"
                "  my chest feels warM instead of tight\n"
                "  in your companY i finally exhale\n"
                "  the worlD can wait for us a while\n"
                "  as the lAst light touches the water\n"
                "  i know that todaY was better with you in it\n\n"
                "Now follow the instruction: take the single CAPITAL letter\n"
                "from each line, top to bottom, to read the hidden sentence.\n\n"
                "ROMANTIC PROMPT (AFTER TYPING IT):\n"
                "Say it out loud to each other and just pause for a moment.\n\n"
                "Type that full sentence here to finish the adventure:"
            ),
            acceptable_answers=[
                "you are the best part of my day",
            ],
            hint="It starts with 'you' and sums up how this whole date felt to the speaker.",
        ),
    ]

    run_adventure(stages)


if __name__ == "__main__":
    main()


