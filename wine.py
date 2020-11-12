def score_wine_Collector_method(hand, standard_tokens_for_trail):
  """Uses the Collector rule to calculate the number of points for wine tokens
  
  Each wine is worth 1 point for each different type of food you have at least one of.

  Parameters
  ----------
  standard_tokens_for_trail : (dict)
    A dictionary containing the 'standard' tokens used to prepare the trail for this game. 

    Used to cross-reference the player's hand to see which tokens will 
    interact with the wine.
    Keys are food types as strings
    Values are integers.
  
  Returns
  -------
  wine_score : (integer)
    An integer showing the player's total points from wine. 
  """
  wine_score = hand["wine"] *\
    (len([food for food in hand\
    if food in standard_tokens_for_trail and hand[food] > 0]))
  return wine_score

def score_wine_Oenophile_method(hand, standard_tokens_for_trail):
  """Uses the Oenophile rule to calculate the number of points for wine tokens

  Each wine is worth one point for each wine you have.

  Parameters
  ----------
  standard_tokens_for_trail : (dict)
    A dictionary containing the 'standard' tokens used to prepare the trail for this game. 

    Used to cross-reference the player's hand to see which tokens will 
    interact with the wine. Not needed for this method but passed because the method 
    which calles this also calls others where this is required. It is included here for concistency.
    Keys are food types as strings
    Values are integers.

  Returns
  -------
  wine_score : (integer)
    An integer showing the player's total points from wine. 
  """
  wine_score = hand["wine"] * hand["wine"]
  return wine_score
