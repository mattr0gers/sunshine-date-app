"""
Sunshine Coast Puzzle Date – Puzzle & Picnic Quest
Falafel + Dips + Prosciutto + Olives + Greens + Sweet Treat (No-Cook Lunch)

Runs as a Streamlit app:
- Shows one stage at a time
- Lets you type answers
- 'Hint' button for each puzzle
- Automatically moves to the next stage on a correct answer
"""

import streamlit as st
from dataclasses import dataclass
from typing import List


# ---------- Data model ----------

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


# ---------- All stages ----------

stages: List[Stage] = [

    # STAGE 1 – KUNARA

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
            "kunara",
            "kunara organic marketplace",
            "kunara organics",
            "kunara organic market",
        ],
        hint="Turn each number into a letter; you'll get a six-letter name on a big sign at Forest Glen.",
    ),

    # STAGE 2 – FALAFEL

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
        acceptable_answers=["falafel", "falafels"],
        hint="Classic chickpea street food you'd wrap with salad and tahini.",
    ),

    # STAGE 3 – OLIVES

    Stage(
        number=3,
        name="Salty Antipasto – Number Word Puzzle",
        prompt=(
            "TRAVEL:\n"
            "Still in the marketplace – head to the deli / antipasto area.\n\n"
            "PUZZLE 3 – TWO-ROW NUMBER CODE\n"
            "Your card shows two rows of numbers (A=1, B=2, ..., Z=26):\n\n"
            "  15   12   9\n"
            "  22   5   19\n\n"
            "Instruction on the card:\n"
            "  'Decode BOTH rows.\n"
            "   Row 1 is the first part of the word.\n"
            "   Row 2 is the second part.\n"
            "   Together they name a salty ingredient we’re buying –\n"
            "   it’s a SINGLE word split across two rows.'\n\n"
            "ROMANTIC PROMPT:\n"
            "  • Are you more of a 'sweet tooth' or 'olive/cheese board' person?\n\n"
            "Type the ingredient you decode:"
        ),
        acceptable_answers=[
            "olives", "marinated olives", "greek olives", "kalamata olives"
        ],
        hint="Decode both rows and think of a briny thing in jars on antipasto platters.",
    ),

    # STAGE 4 – PROSCIUTTO

    Stage(
        number=4,
        name="Delicate Cured Meat – Hidden Inside",
        prompt=(
            "TRAVEL:\n"
            "Still in the marketplace – walk to the deli / cold meats section.\n\n"
            "PUZZLE 4 – HIDDEN INSIDE A SENTENCE\n"
            "Your next card reads:\n\n"
            "  I'm a delicate cured meat that PROtectS Chefs In Unbelievably\n"
            "  Tender TOasts when shaved paper-thin.\n\n"
            "Look carefully: the capitals hide the word.\n\n"
            "ROMANTIC PROMPT:\n"
            "  • Are you more into light, delicate foods or big hearty meals?\n\n"
            "Type the meat's name:"
        ),
        acceptable_answers=["prosciutto", "proscuitto"],
        hint="Take just the capital letters in order – they spell a thin Italian ham.",
    ),

    # STAGE 5 – GREENS

    Stage(
        number=5,
        name="Greens – LOVE Vowel Puzzle",
        prompt=(
            "TRAVEL:\n"
            "Still at the marketplace – head to the fresh produce / salad section.\n\n"
            "PUZZLE 5 – ONLY VOWELS FROM 'LOVE'\n"
            "Your card shows nearly-complete words:\n\n"
            "  R _ C K E T\n"
            "  B _ B Y  SP N CH\n"
            "  S L _ D  M X\n"
            "  M X _ D  L E _ V E S\n\n"
            "Instruction:\n"
            "  'You may ONLY use vowels from LOVE (O and E), plus A once.\n"
            "   Fill the blanks to form REAL leafy salad ingredients.\n"
            "   Choose ONE of the valid greens and type its name.'\n\n"
            "ROMANTIC PROMPT:\n"
            "  • What does a 'healthy day' look like for you – food, movement, rest?\n\n"
            "Type the name of the greens you pick:"
        ),
        acceptable_answers=[
            "rocket", "baby spinach", "spinach", "spinach leaves",
            "salad greens", "mixed salad greens", "salad mix",
            "mixed leaves", "mesclun"
        ],
        hint="Think of actual bagged salad names you see in the fridge section.",
    ),

Stage(
    number=6,
    name="Forest Glen → Headland – Indo Surf Forecast Navigation (Hardest)",
    prompt=(
        "TRAVEL PUZZLE – SOLVE ON THE DRIVE (PASSENGER ONLY)\n"
        "You’ve left Kunara and you’re heading toward the coast.\n"
        "Your next clue is disguised as a 'MORNING SURF FORECAST' from\n"
        "a fictional Indo island chain.\n\n"
        "PUZZLE 6 – INDO SURF FORECAST NAVIGATION (HARDEST)\n"
        "Each 'break' has a wave forecast (ft). Only some breaks matter.\n\n"
        "SURF REPORT:\n"
        "  Padang Left – 2 ft\n"
        "  Legian Backreef – 4 ft\n"
        "  Ombak Murni – 3 ft\n"
        "  Impossibles Bay – 5 ft\n"
        "  Nusa Dua Outpost – 6 ft\n"
        "  Temples Righthander – 7 ft\n"
        "  Teluk Putih – 11 ft\n"
        "  Canggu River Mouth – 13 ft\n"
        "  Amed Bowls – 17 ft\n"
        "  Rote Bend – 19 ft\n"
        "  Quinn’s Bluff – 9 ft\n"
        "  Tanjung Set – 23 ft\n"
        "  Wilis Peak – 29 ft\n"
        "  Maui - 30 ft\n"
        "  Raja Right – 31 ft\n"
        "  Indo Marlin Ledge – 37 ft\n"
        "  Gili Street Banks – 41 ft\n"
        "  Ekkas - 340 ft\n"
        "  Helang Corner – 43 ft\n"
        "  Mentawais - 40 ft\n"
        "  Gerupuk - 100 ft\n"
        "  Tongkat Bay – 47 ft\n\n"
        "SCRIBBLED CLUES ON THE CARD:\n"
        "  'Some surf forecasts are dodgy – the ones that can be split neatly into\n"
        "   equal chunks again and again, or the ones that sit too perfectly on\n"
        "   the grid like 4 or 9. Others end in 0 or 5, like old signs where\n"
        "   the paint has worn off just right. Those spots are red herrings.\n\n"
        "   The true breaks are rare: their wave forecasts stand alone, made only by\n"
        "   1 and themselves. Keep those special forecasts, let the rest wash away.\n\n"
        "   Then, in the order the report is written, take the very first letter\n"
        "   of each break that survives. String those letters together and you'll\n"
        "   see a name that doesn’t belong in Indo at all, but somewhere much\n"
        "   closer – a Sunshine Coast headland you know by heart.'\n\n"
        "ROMANTIC PROMPT (ON THE DRIVE):\n"
        "  • If we did a surf trip anywhere in Indonesia together, where would\n"
        "    you want to go first, and what board would you bring?\n\n"
        "Your answer should be the headland with the lighthouse.\n\n"
        "Type the landmark name:"
    ),
    acceptable_answers=[
        "point cartwright",
        "point cartwright lighthouse",
        "cartwright lighthouse",
    ],
    hint=(
        "Distances that are composites, squares, or end in 0 or 5 are decoys.\n"
        "The remaining ones are primes (only divisible by 1 and themselves).\n"
        "Prime distances left: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47.\n"
        "Take the first letters of THOSE break names in order."
    
    ),
),


    # STAGE 7 – RECEIPT CIPHER: THE VELO PROJECT

    Stage(
        number=7,
        name="Warehouse Café – The Long Receipt Cipher",
        prompt=(
            "TRAVEL TO THIS STAGE:\n"
            "From the headland, DRIVE toward Mooloolaba.\n"
            "You’re heading to a tucked-away warehouse-style breakfast café,\n"
            "but its name is hidden in a fake 'receipt' on your card.\n\n"
            "PUZZLE 7 – THE LONG RECEIPT CIPHER (HARD)\n"
            "The card shows a printed receipt:\n\n"
            "    -------------------------------------------------\n"
            "    08:02   1x Vanilla latte\n"
            "    08:03   1x Eggs on toast\n"
            "    08:05   2x Loaded granola\n"
            "    08:06   2x Orange juice\n"
            "    08:08   2x Pancake stack\n"
            "    08:10   2x Raspberry muffin\n"
            "    08:11   3x Overnight oats\n"
            "    08:13   1x Jam toast\n"
            "    08:14   1x Espresso shot\n"
            "    08:16   1x Chai latte\n"
            "    08:18   2x Thick-cut toast\n"
            "    -------------------------------------------------\n"
            "    RANDOM CODE:\n"
            "       21   4   10   13     |     14   16   12   9   4   2   18\n"
            "    -------------------------------------------------\n"
            "    INSTRUCTION:\n"
            "      'Use A=1, B=2, ... Z=26.\n"
            "       First, take each RANDOM CODE number and ADD the quantity\n"
            "       shown at the front of the matching line above – in order.\n"
            "       (1st code number uses the 1st line, 2nd uses the 2nd line, etc.)\n"
            "       Then convert the NEW numbers to letters.\n"
            "       The first four letters form word one.\n"
            "       The last seven letters form word two.'\n\n"
            "ROMANTIC PROMPT (ON THE DRIVE):\n"
            "  • If we owned our own little warehouse breakfast spot, what would\n"
            "    you put on the menu that feels the most 'us'?\n\n"
            "Type the full two-word café name you decode:"
        ),
        acceptable_answers=[
            "the velo project",
            "velo project",
            "theveloproject",
        ],
        hint=(
            "Start with the first code number (21) and add the quantity in front of\n"
            "the first menu item (1) → 22 → V.\n"
            "Do that all the way along, then decode with A=1."
        ),
    ),

    # STAGE 8 – ROCK POOLS

    Stage(
        number=8,
        name="Rock Pools – Alphabet Number Code",
        prompt=(
            "TRAVEL TO THIS STAGE:\n"
            "From the warehouse café, go to the rock pools near the Spit in Mooloolaba.\n"
            "- Drive a few minutes, then walk down toward the rocks.\n\n"
            "PUZZLE 8 – NUMBER CODE\n"
            "Two rows of numbers:\n\n"
            "  18   15   3   11\n"
            "  16   15   15   12   19\n\n"
            "Use A=1, B=2, ... Z=26 to decode.\n\n"
            "ROMANTIC PROMPT:\n"
            "  • Favourite childhood beach or rock-pool memory?\n\n"
            "Type the full location name (you can include the suburb if you like):"
        ),
        acceptable_answers=[
            "rock pools",
            "the rock pools",
            "mooloolaba rock pools",
            "rock pools mooloolaba",
            "rockpools",
        ],
        hint="You literally spell what these things are with A=1, B=2, etc.",
    ),

    # STAGE 9 – GELATO + GPS

    Stage(
        number=9,
        name="Frozen Treat – Secret GPS Coordinates",
        prompt=(
            "TRAVEL TO THIS STAGE:\n"
            "From the rock pools, WALK back along the beach/esplanade to the strip.\n\n"
            "PUZZLE 9A – ACROSTIC\n"
            "First letter of each line:\n\n"
            "  Glistening scoops wait in frosty rows,\n"
            "  Every flavour shining under the glass,\n"
            "  Laughter spills out as people choose their favourites,\n"
            "  Afternoons here taste like holidays,\n"
            "  Tasting sunshine in every cold mouthful,\n"
            "  On the esplanade, hearts and hands both full.\n\n"
            "PUZZLE 9B – GPS (OPTIONAL HARD)\n"
            "A=0, B=1, ..., J=9. Each CAPITAL in the next lines is one digit.\n"
            "First 6 capitals = latitude, next 6 = longitude.\n\n"
            "ROMANTIC PROMPT:\n"
            "  • If you could freeze this exact moment, what tiny detail\n"
            "    would you want to remember most?\n\n"
            "For the game, just type the SIX-LETTER Italian word from 9A:"
        ),
        acceptable_answers=["gelato"],
        hint="Read down the first letters of those six lines.",
    ),

    # STAGE 10 – ALEXANDRA HEADLAND

    Stage(
        number=10,
        name="Headland Lookout – Coastal Acrostic",
        prompt=(
            "TRAVEL TO THIS STAGE:\n"
            "From the esplanade, DRIVE north to a favourite surf headland.\n\n"
            "PUZZLE 10 – ACROSTIC\n"
            "First letters of each line:\n\n"
            "  A rocky bluff sits between two shining beaches,\n"
            "  Little lines of surfers wait out the back,\n"
            "  Endless sets peel along the point at sunset,\n"
            "  X-marks the bend in the coast that locals love.\n\n"
            "ROMANTIC PROMPT:\n"
            "  • If we could watch the sunset from any place in the world\n"
            "    (cliff, mountain, city, beach), where would you choose?\n\n"
            "Type the headland / area name:"
        ),
        acceptable_answers=[
            "alexandra headland",
            "alex headland",
            "the bluff",
            "alex bluff",
            "alex",
        ],
        hint="The initials of the four lines form a short nickname surfers use.",
    ),

    # STAGE 11 – COASTAL WHOLE-FOOD STORE

    Stage(
        number=11,
        name="Coastal Whole-Food Store – Choice",
        prompt=(
            "TRAVEL TO THIS STAGE:\n"
            "From the headland, DRIVE to a coastal wholefoods area in Maroochydore.\n\n"
            "PUZZLE 11 – MULTI-ANSWER\n"
            "Your map circles three health/organic stores. Pick ANY ONE.\n\n"
            "ROMANTIC PROMPT (PARKED OUTSIDE):\n"
            "  • If we cooked together regularly, what kind of food\n"
            "    do you imagine us making the most?\n\n"
            "Type the name of the store you actually go to:"
        ),
        acceptable_answers=[
            "flannerys",
            "flannerys maroochydore",
            "flannerys organic and wholefood market",
            "wholelife",
            "wholelife maroochydore",
            "wholelife healthfoods maroochydore",
            "fundies",
            "fundies maroochydore",
            "fundies wholefood market",
        ],
        hint="Any of the big organic/health shops in Maroochydore is fine.",
    ),

    # STAGE 12 – DIPS

    Stage(
        number=12,
        name="Dips – Riddle of the Spread",
        prompt=(
            "TRAVEL:\n"
            "Inside your chosen store – go to the chilled section.\n\n"
            "PUZZLE 12 – DIP RIDDLE\n"
            "  I hide in tubs along the chilled wall,\n"
            "  I'm scooped or spread at every picnic and stall.\n"
            "  Chickpeas or yoghurt, beetroot so bright,\n"
            "  I'm perfect with bread in the soft afternoon light.\n\n"
            "ROMANTIC PROMPT (CHOOSING DIPS):\n"
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

    # STAGE 13 – BREAD

    Stage(
        number=13,
        name="Bread – Texture Puzzle",
        prompt=(
            "TRAVEL:\n"
            "Same store – walk to the bread / bakery section.\n\n"
            "PUZZLE 13 – BREAD RIDDLE\n"
            "  I crackle when you squeeze me,\n"
            "  I can be long or round or flat.\n"
            "  I'm born in a bakery and die in a sandwich.\n"
            "  Without me, the fillings fall flat.\n\n"
            "ROMANTIC PROMPT (CHOOSING BREAD):\n"
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
        hint="Just name the loaf you’re actually buying.",
    ),

    # STAGE 14 – BOTANIC GARDEN PICNIC

    Stage(
        number=14,
        name="Picnic – Bushland Garden Riddle",
        prompt=(
            "TRAVEL TO THIS STAGE:\n"
            "From the coastal shops, DRIVE to a bushland botanic garden in Tanawha.\n\n"
            "PUZZLE 14 – GARDEN RIDDLE\n"
            "  Find the garden where art meets trees,\n"
            "  Where stone and steel share space with leaves.\n"
            "  Not by the sea, but not too far,\n"
            "  A BUSHLAND BOTANIC hidden star.\n\n"
            "ROMANTIC PROMPT (AT THE PICNIC):\n"
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
        hint="Keep it simple – you’re basically in a 'botanic garden' in the bushland at Tanawha.",
    ),

    # STAGE 15 – SWEET-TREAT VENUE TYPE

    Stage(
        number=15,
        name="Sweet Treat Place – Wildcard",
        prompt=(
            "TRAVEL TO THIS STAGE:\n"
            "After your picnic, DRIVE to any dessert / sweet-treat spot you like.\n\n"
            "PUZZLE 15 – CATEGORY\n"
            "  Rings of dough? Frozen bowls? A raw treat stack?\n"
            "  Just write what KIND of shop you're heading back.\n\n"
            "In real life, go to ANY dessert / sweet-treat spot you like nearby.\n\n"
            "ROMANTIC PROMPT (AT THE COUNTER):\n"
            "  • What's your go-to 'treat' when you've had a huge week?\n\n"
            "For the game, type the STYLE of place you chose, for example:\n"
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

    # STAGE 16 – SWEET-TREAT ITEM

    Stage(
        number=16,
        name="Sweet Treat – Menu Choice",
        prompt=(
            "TRAVEL:\n"
            "You're now at your chosen dessert place.\n\n"
            "PUZZLE 16 – MENU CHOICE\n"
            "  Pick something that balances us:\n"
            "  a little JOY, a little NOURISH.\n"
            "  It might be round with icing,\n"
            "  blended in a bowl,\n"
            "  rolled into a ball,\n"
            "  or sliced from something whole.\n\n"
            "ROMANTIC PROMPT:\n"
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

    # STAGE 17 – COTTON TREE RIVERWALK

    Stage(
        number=17,
        name="Riverwalk – Location Cipher",
        prompt=(
            "TRAVEL TO THIS STAGE:\n"
            "From your dessert place, DRIVE to a riverfront walk at Cotton Tree.\n\n"
            "PUZZLE 17 – SCRAMBLED CHUNKS\n"
            "  TREE   COT   RIV   WALK\n\n"
            "Rearrange these into a sensible two or three word place name\n"
            "along the river where the suburb is also in the name.\n\n"
            "ROMANTIC PROMPT (START OF THE WALK):\n"
            "  • When do you feel most at peace in nature – ocean, river, forest, mountains?\n\n"
            "Type the location:"
        ),
        acceptable_answers=[
            "cotton tree riverwalk",
            "cotton tree",
            "cotton tree river park",
            "cotton tree park",
        ],
        hint="Put the suburb word first, then a phrase for the river path or park there.",
    ),

    # STAGE 18 – LOVE WORD

    Stage(
        number=18,
        name="Love Riddle – Reflection Choice",
        prompt=(
            "TRAVEL:\n"
            "You’re already on the riverwalk – just stroll a bit.\n\n"
            "PUZZLE 18 – CHOOSE ONE WORD\n"
            "Which feels most like LOVE to you right now:\n"
            "  • moving\n"
            "  • reflected\n"
            "  • still\n\n"
            "There is no wrong answer – just what feels true.\n\n"
            "ROMANTIC PROMPT (AFTER ANSWERING):\n"
            "Share with each other:\n"
            "  • Why did you choose that word? What about your connection feels like that?\n\n"
            "Type your chosen word:"
        ),
        acceptable_answers=[
            "moving",
            "reflected",
            "still",
        ],
        hint="This is about feeling, not correctness. Pick the word that resonates.",
    ),

    # STAGE 19 – FINAL HIDDEN SENTENCE

    Stage(
        number=19,
        name="Final Romantic Diagonal – Hidden Sentence",
        prompt=(
            "TRAVEL:\n"
            "Stay right here on the riverwalk, maybe pause somewhere quiet with a view.\n\n"
            "PUZZLE 19 – ONE CAPITAL PER LINE\n"
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
            "ROMANTIC PROMPT (AFTER TYPING IT):\n"
            "Say it out loud to each other and just pause for a moment.\n\n"
            "Type that full sentence here to finish the adventure:"
        ),
        acceptable_answers=[
            "you are the best part of my day",
        ],
        hint="It starts with 'you' and sums up how this whole date has felt.",
    ),
]


# ---------- Streamlit UI ----------

def main():
    st.set_page_config(
        page_title="Sunshine Coast Puzzle Date",
        page_icon="🌴",
        layout="centered",
    )

    st.title("🌴 Sunshine Coast Puzzle Date – Puzzle & Picnic Quest")
    st.write(
        "Type your answer for each stage. Tap **Hint 💡** if you get stuck.\n\n"
        "_Answers ignore case, spaces, and punctuation._"
    )

    # Initialise session state
    if "stage_index" not in st.session_state:
        st.session_state.stage_index = 0
        st.session_state.finished = False

    # If finished, show end screen
    if st.session_state.finished:
        st.success("🎉 You’ve completed all stages of the Sunshine Coast Puzzle Date! 🎉")
        if st.button("Restart adventure"):
            st.session_state.stage_index = 0
            st.session_state.finished = False
        return

    # Current stage
    idx = st.session_state.stage_index
    stage = stages[idx]
    total = len(stages)

    # Progress & header
    st.progress((idx + 1) / total)
    st.subheader(f"Stage {stage.number}: {stage.name}")

    # Show puzzle text
    st.markdown(stage.prompt.replace("\n", "  \n"))

    # Input + submit / hint buttons
    answer = st.text_input("Your answer:", key=f"answer_{stage.number}")
    col1, col2 = st.columns(2)
    submit = col1.button("Submit ✅")
    show_hint = col2.button("Hint 💡")

    # Show hint
    if show_hint:
        st.info(stage.hint)

    # Normalised answers
    normalized_accept = [normalize(a) for a in stage.acceptable_answers]

    # Handle submit (auto-advance on correct)
    if submit:
        if not answer.strip():
            st.warning("Type something first 🙂")
        else:
            user_norm = normalize(answer)
            if user_norm in normalized_accept:
                st.success("Correct! 🎯 Moving on...")
                if idx + 1 < total:
                    st.session_state.stage_index += 1
                else:
                    st.session_state.finished = True
                st.rerun()
            else:
                st.error("Not quite. Try again or tap **Hint 💡**.")

    # --- Manual navigation buttons (back / forward) ---
    nav_col1, nav_col2 = st.columns(2)
    with nav_col1:
        if st.button("⬅ Previous stage"):
            if st.session_state.stage_index > 0:
                st.session_state.stage_index -= 1
                st.rerun()
    with nav_col2:
        if st.button("Next stage ➡"):
            if st.session_state.stage_index < total - 1:
                st.session_state.stage_index += 1
                st.rerun()


if __name__ == "__main__":
    main()



