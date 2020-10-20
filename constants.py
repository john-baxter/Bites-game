
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


FOOD_TYPES = K_COLOUR_V_FOOD_DICT.values()
"""A list of the types of token used for the trail

The food tokens will be labelled according to the name of the food idem depicted.
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


NUMBER_OF_EACH_FOOD_TOKEN = 9
"""As per the standard rules of the game, there are this many of each standard 
food token.
"""


TOKENS_FOR_TRAIL = {i : NUMBER_OF_EACH_FOOD_TOKEN for i in FOOD_TYPES}
"""The standard number of each standard food token

A dictionary showing how many of each standard food token will be 
used as per the rules.
Keys are foods as strings
Values are integers
"""


PROMPT_TEXT_ANT_CHOICE  = "please enter your choice of ant"
"""The text which will be contained in the question when asking the user to choose which 
ant to move.
"""

PROMPT_TEXT_DIRECTION_CHOICE = "please pick a direction to collect food from"
"""The text which will be contained in the question when asking the user to choose which 
direction to collect food from.
"""

PROMPT_TEXT_ANTHILL_FOOD_CHOICE = "please enter your choice of food"
"""The text which will be contained in the question when asking the user to choose 
which food to collect from the anthill.
"""


MIN_PLAYERS = 2
MAX_PLAYERS = 5
"""As per the standard rules of the game, these many players must take part.
"""


ANTHILL_ORDER_TOP_DOWN = [4, 3, 2, 1, 0]
ANTHILL_ORDER_BOTTOM_UP = [0, 1, 2, 3, 4]
"""The various lists that are used to determine the orser that the anthill is filled
"""