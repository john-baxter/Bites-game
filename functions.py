def show_allowed_choices_from_list(list):
  """Prints the elements of a list preceeded by prompt text

  Used when the user needs to choose an option from a list.

  Parameters
  ----------
  list : (list)
    A list of elements for the user to choose between
  """
  print("\nThe available options are:")
  for i in list:
    print(i)
