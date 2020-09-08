ANTS = ['purple', 'red', 'brown', 'yellow', 'green']
"""A list of ID for the insect meeple

The ants will be identified by their colour.
The order in this list is not important
Each element is a string
"""

FOOD_TYPES = ['grapes', 'apple', 'bread', 'cheese', 'pepper']
"""A list of the types of token used for the trail

The food tokens will be labelled according to the name of the food idem depicted.
The order in this list is not important.
Each name is written in singular form except 'grapes'; this is in reflection of the 
real game pieces.
Each element is a string
"""

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

K_FOOD_V_COLOUR_DICT = dict((v, k) for k, v in K_COLOUR_V_FOOD_DICT.items())
"""Cross reference which ant colour matches with which food token

A dictionary to refer to when cross referencing is required between 
food type and ant colour.
This contains the same pairs as K_COLOUR_V_FOOD_DICT with the keys 
and values interchanged.
Keys are food IDs as strings.
Values are ant colours as strings.
"""