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
        hint="Turn each number into a letter; you'll get a six-letter name on a big sign at Forest Glen.",
    ),

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
            "  • Are you more into light, delicate foods or big hearty meals?\n\n"
            "Type the meat's name:"
        ),
        acceptable_answers=["prosciutto", "proscuitto"],
        hint="Take just the capital letters in order – they spell a thin Italian ham.",
    ),

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
        name="Coastal Lighthouse Acrostic",
        prompt=(
            "TRAVEL TO THIS STAGE:\n"
            "From the marketplace, DRIVE out to a well-known headland lighthouse.\n\n"
            "PUZZLE 6 – ACROSTIC\n"
            "Take the FIRST letter of each line:\n\n"
            "  Pillars of white rise where the seas collide,\n"
            "  Over looking the mouth where the river is wide.\n"
            "  In storms and calm I shine through the night,\n"
            "  Navigating sailors with my sweeping light.\n"
            "  Tall on the headland, a steadfast sight.\n\n"
            "ROMANTIC PROMPT:\n"
            "  • What ocean place feels like 'home' to you, and why?\n\n"
            "Type the full landmark name:"
        ),
        acceptable_answers=[
            "Point Cartwright Lighthouse",
            "Point Cartwright",
            "Cartwright Lighthouse",
        ],
        hint="First letters form a 5-letter word at the start of the lighthouse name.",
    ),

    Stage(
        number=7,
        name="Warehouse Café – Hidden Name",
        prompt=(
            "TRAVEL TO THIS STAGE:\n"
            "From the lighthouse, DRIVE to a converted warehouse café in Mooloolaba.\n\n"
            "PUZZLE 7 – NAME RIDDLE\n"
            "Story on the card:\n\n"
            "  'We roll up to a hidden spot near the sand.\n"
            "   Inside, old BIKE frames hang on the walls,\n"
            "   and worn-out WHEELS rest in every corner.\n"
            "   It feels like a secret PROJECT someone built\n"
            "   just for riders who want good coffee.'\n\n"
            "Back of the card:\n"
            "  'Take the idea of a BIKE and a PROJECT.\n"
            "   Think of a two-word café name: first a word for a type of bike,\n"
            "   then a word for a plan.'\n\n"
            "ROMANTIC PROMPT:\n"
            "  • If we could teleport to any café in the world, where would you pick?\n\n"
            "Type the café’s name:"
        ),
        acceptable_answers=["The Velo Project", "Velo Project"],
        hint="A French-ish word for 'bike' plus a word meaning 'plan' or 'task'.",
    ),

    Stage(
        number=8,
        name="Rock Pools – Alphabet Number Code",
        prompt=(
            "TRAVEL TO THIS STAGE:\n"
            "From the café, go to the rock pools near the Spit.\n\n"
            "PUZZLE 8 – NUMBER CODE\n"
            "Two rows of numbers:\n\n"
            "  18   15   3   11\n"
            "  16   15   15   12   19\n\n"
            "Use A=1, B=2, ... Z=26 to decode.\n\n"
            "ROMANTIC PROMPT:\n"
            "  • Favourite childhood beach or rock-pool memory?\n\n"
            "Type the full location name:"
        ),
        acceptable_answers=[
            "Rock Pools", "The Rock Pools", "Mooloolaba Rock Pools",
            "Rock Pools Mooloolaba", "Rockpools"
        ],
        hint="You literally spell what these things are.",
    ),

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
            "Type the SIX-LETTER Italian word from 9A:"
        ),
        acceptable_answers=["gelato"],
        hint="Read down the first letters of those six lines.",
    ),

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
            "Type the headland / area name:"
        ),
        acceptable_answers=[
            "Alexandra Headland", "Alex Headland", "The Bluff",
            "Alex Bluff", "Alex"
        ],
        hint="Initials spell a short nickname surfers say all the time.",
    ),

    Stage(
        number=11,
        name="Coastal Whole-Food Store – Choice",
        prompt=(
            "TRAVEL TO THIS STAGE:\n"
            "From the headland, DRIVE to a coastal wholefoods area in Maroochydore.\n\n"
            "PUZZLE 11 – MULTI-ANSWER\n"
            "Your map circles three health/organic stores. Pick ANY ONE.\n\n"
            "Type the name of the store you choose:"
        ),
        acceptable_answers=[
            "Flannerys", "Flannerys Maroochydore",
            "Flannerys Organic and Wholefood Market",
            "Wholelife", "Wholelife Maroochydore",
            "Wholelife Healthfoods Maroochydore",
            "Fundies", "Fundies Maroochydore",
            "Fundies Wholefood Market",
        ],
        hint="Any of the big organic/health shops in Maroochydore is fine.",
    ),

    Stage(
        number=12,
        name="Dips – Riddle of the Spread",
        prompt=(
            "TRAVEL:\n"
            "Inside your chosen store – go to the chilled section.\n\n"
            "PUZZLE 12 – DIP RIDDLE\n"
            "  'I hide in tubs along the chilled wall,\n"
            "   I'm scooped or spread at every picnic and stall.\n"
            "   Chickpeas or yoghurt, beetroot so bright,\n"
            "   I'm perfect with bread in the soft afternoon light.'\n\n"
            "Type ONE dip you pick (e.g. hummus, tzatziki):"
        ),
        acceptable_answers=[
            "hummus", "houmous", "baba ganoush", "baba ganouj",
            "tzatziki", "beetroot dip", "dip"
        ],
        hint="Any realistic savoury dip is fine.",
    ),

    Stage(
        number=13,
        name="Bread – Texture Puzzle",
        prompt=(
            "TRAVEL:\n"
            "Same store – walk to the bread / bakery section.\n\n"
            "PUZZLE 13 – BREAD RIDDLE\n"
            "  'I crackle when you squeeze me,\n"
            "   I can be long or round or flat.\n"
            "   I'm born in a bakery and die in a sandwich.\n"
            "   Without me, the fillings fall flat.'\n\n"
            "Type the style of bread you pick (e.g. sourdough, ciabatta, Turkish bread):"
        ),
        acceptable_answers=[
            "sourdough", "ciabatta", "turkish bread",
            "turkish", "baguette", "rustic loaf", "bread"
        ],
        hint="Just name the loaf you're actually buying.",
    ),

    Stage(
        number=14,
        name="Picnic – Bushland Garden Riddle",
        prompt=(
            "TRAVEL TO THIS STAGE:\n"
            "From the coastal shops, DRIVE to a bushland botanic garden in Tanawha.\n\n"
            "PUZZLE 14 – GARDEN RIDDLE\n"
            "  'Find the garden where art meets trees,\n"
            "   Where stone and steel share space with leaves.\n"
            "   Not by the sea, but not too far,\n"
            "   A BUSHLAND BOTANIC hidden star.'\n\n"
            "Type the place in simple words (e.g. 'botanic garden'):"
        ),
        acceptable_answers=[
            "botanic garden", "botanic gardens",
            "bushland botanic garden",
            "maroochy botanic garden",
            "maroochy bushland botanic garden",
        ],
        hint="You're basically at a 'botanic garden' in the bushland.",
    ),

    Stage(
        number=15,
        name="Sweet Treat Place – Wildcard",
        prompt=(
            "TRAVEL TO THIS STAGE:\n"
            "After your picnic, DRIVE to any dessert / sweet-treat spot you like.\n\n"
            "PUZZLE 15 – CATEGORY\n"
            "  'Rings of dough? Frozen bowls? A raw treat stack?\n"
            "   Just write what KIND of shop you're heading back.'\n\n"
            "Type the STYLE of place (e.g. donut shop, dessert bar, acai bar, bakery):"
        ),
        acceptable_answers=[
            "donut shop", "doughnut shop", "dessert bar",
            "acai bar", "acai place", "healthy cafe",
            "healthy café", "bakery"
        ],
        hint="Just the category, not the brand name.",
    ),

    Stage(
        number=16,
        name="Sweet Treat – Menu Choice",
        prompt=(
            "TRAVEL:\n"
            "You're now inside your dessert place.\n\n"
            "PUZZLE 16 – WHAT DID YOU PICK?\n"
            "Type what you actually ordered (e.g. donut, acai bowl, bliss ball, raw slice):"
        ),
        acceptable_answers=[
            "donut", "doughnut", "acai bowl", "acai",
            "bliss ball", "raw slice", "brownie",
            "healthy brownie", "protein ball"
        ],
        hint="Whatever is on your plate/cup in front of you.",
    ),

    Stage(
        number=17,
        name="Riverwalk – Location Cipher",
        prompt=(
            "TRAVEL TO THIS STAGE:\n"
            "From your dessert spot, DRIVE to a riverfront walk at Cotton Tree.\n\n"
            "PUZZLE 17 – SCRAMBLED CHUNKS\n"
            "  TREE   COT   RIV   WALK\n\n"
            "Rearrange into a real place name including the suburb.\n\n"
            "Type the location:"
        ),
        acceptable_answers=[
            "Cotton Tree Riverwalk",
            "Cotton Tree",
            "Cotton Tree River Park",
            "Cotton Tree Park",
        ],
        hint="Put the suburb first, then something like 'riverwalk' or 'river park'.",
    ),

    Stage(
        number=18,
        name="Love Riddle – Reflection Choice",
        prompt=(
            "TRAVEL:\n"
            "You’re already on the riverwalk – just stroll a bit.\n\n"
            "PUZZLE 18 – CHOOSE ONE WORD\n"
            "Which feels most like LOVE to you now:\n"
            "  • moving\n"
            "  • reflected\n"
            "  • still\n\n"
            "Type one of those words:"
        ),
        acceptable_answers=["moving", "reflected", "still"],
        hint="There’s no wrong answer; choose the word that feels right.",
    ),

    Stage(
        number=19,
        name="Final Romantic Diagonal – Hidden Sentence",
        prompt=(
            "TRAVEL:\n"
            "Stay on the riverwalk somewhere quiet.\n\n"
            "PUZZLE 19 – ONE CAPITAL PER LINE\n"
            "Take the single CAPITAL letter in each line, top to bottom:\n\n"
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
            "Type the full hidden sentence:"
        ),
        acceptable_answers=["you are the best part of my day"],
        hint="Starts with 'you' and sums up the whole date.",
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

    if "stage_index" not in st.session_state:
        st.session_state.stage_index = 0
        st.session_state.finished = False

    if st.session_state.finished:
        st.success("🎉 You’ve completed all stages of the Sunshine Coast Puzzle Date! 🎉")
        if st.button("Restart adventure"):
            st.session_state.stage_index = 0
            st.session_state.finished = False
        return

    idx = st.session_state.stage_index
    stage = stages[idx]
    total = len(stages)

    st.progress((idx + 1) / total)
    st.subheader(f"Stage {stage.number}: {stage.name}")
    st.markdown(stage.prompt.replace("\n", "  \n"))

    answer = st.text_input("Your answer:")
    col1, col2 = st.columns(2)
    submit = col1.button("Submit ✅")
    show_hint = col2.button("Hint 💡")

    if show_hint:
        st.info(stage.hint)

    normalized_accept = [normalize(a) for a in stage.acceptable_answers]

    if submit:
        if not answer.strip():
            st.warning("Type something first 🙂")
        else:
            user_norm = normalize(answer)
            if user_norm in normalized_accept:
                st.success("Correct! 🎯")
                if idx + 1 < total:
                    if st.button("Next stage ➡️"):
                        st.session_state.stage_index += 1
                        st.experimental_rerun()
                else:
                    st.session_state.finished = True
                    st.experimental_rerun()
            else:
                st.error("Not quite. Try again or tap **Hint 💡**.")


if __name__ == "__main__":
    main()
