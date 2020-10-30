
K_COLOUR_V_FOOD_DICT = {
  "purple": "grapes",
  "red": "apple",
  "brown": "bread",
  "yellow": "cheese",
  "green": "pepper"}
"""Cross reference which food token matches with which ant colour

A dictionary to refer to when cross referencing is required between 
ant colour and food type.
Keys are ant colours as strings
Values are food IDs as strings
"""


ANTS = K_COLOUR_V_FOOD_DICT.keys()
"""A list of ID for the insect meeple

The ants will be identified by their colour.
The order in this list is not important
Each element is a string
"""


STANDARD_FOOD_TYPES = K_COLOUR_V_FOOD_DICT.values()
"""A list of the standard types of food token used for the trail

These food tokens will be labelled according to the name of the food idem depicted.
The order in this list is not important.
Each name is written in singular form except 'grapes'; this is in reflection of the 
real game pieces (but is a deviation from the nomenclature in the game literature, 
which uses singular form for all).
Each element is a string
"""


K_FOOD_V_COLOUR_DICT = dict((v, k) for k, v in K_COLOUR_V_FOOD_DICT.items())
"""Cross reference which ant colour matches with which food token

A dictionary to refer to when cross referencing is required between 
food type and ant colour.
This contains the same pairs as K_COLOUR_V_FOOD_DICT with the keys 
and values interchanged.
Keys are food IDs as strings.
Values are ant colours as strings.
"""


SPECIAL_FOOD_TYPES = ["wine"]
"""A list of the special types of food token used for the trail

Each element is a string.
"""


NUMBER_OF_EACH_STANDARD_FOOD_TOKEN = 9
NUMBER_OF_EACH_SPECIAL_FOOD_TOKEN = 5
"""As per the standard rules of the game, there are this many of each  
food token.
"""


STANDARD_TOKENS_FOR_TRAIL = {food : NUMBER_OF_EACH_STANDARD_FOOD_TOKEN for food in STANDARD_FOOD_TYPES}
"""The standard number of each standard food token

A dictionary showing how many of each standard food token will be 
used as per the rules.
Keys are foods as strings
Values are integers
"""


SPECIAL_TOKENS_FOR_TRAIL = {food : NUMBER_OF_EACH_SPECIAL_FOOD_TOKEN for food in SPECIAL_FOOD_TYPES}
"""The standard number of each special food token

A dictionary showing how many of each special food token will be 
used as per the rules.
Keys are foods as strings
Values are integers
"""


PROMPT_TEXT_ANT_CHOICE  = "please enter your choice of ant"
PROMPT_TEXT_DIRECTION_CHOICE = "please pick a direction to collect food from"
PROMPT_TEXT_ANTHILL_FOOD_CHOICE = "please enter your choice of food"
PROMPT_TEXT_ANTHILL_PLACEMENT_CHOICE = "please enter your choice of anthill level"
"""The text statements that are used during the various call of Player.make_choice()
"""


MIN_PLAYERS = 2
MAX_PLAYERS = 5
"""As per the standard rules of the game, these many players must take part.
"""


ANTHILL_CARD_DICT = {
  "top down": [4, 3, 2, 1, 0],
  "bottom up": [0, 1, 2, 3, 4],
  "leave gaps": [4, 2, 0, 3, 1],
  "user choice": None}
"""The various lists that are used to determine the order that the anthill is filled
"""
