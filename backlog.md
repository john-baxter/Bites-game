# Bites project backlog

Additionally, this could be a good opportunity to learn about and practice using keyword arguments with default values. For example, prompt_text='choose between'. However, upon looking at the contents of the function, I think this would make more sense once the allowed_choices are incorporated into the input text.

When will you add the allowed_choices to the input text? It's okay if that's not within the scope of this branch and PR, but make sure it's in your backlog of tasks.

I can see why you've kept the ant and direction tests separate, because that's how you developed it because they were originally separate functions. However, the new make_choice function doesn't care whether the options are ants or directions, so generalising the tests would be a good idea. For example test_the_first_string_from_a_list_of_one_string_is_a_valid_choice, test_the_first_string_from_a_list_of_several_strings_is_a_valid_choice, test_a_middle_string_from_a_list_of_several_strings_is_a_valid_choice, test_the_last_string_from_a_list_of_several_strings_is_a_valid_choice.

Suggestions of other unit tests:

What if the allowed_choices is an empty list
What if the allowed_choices is a list of something that's not strings (e.g. ints, floats, bools)
What if the allowed_choices is not a list (e.g. it's None, or a single string, or a single number)
What if the user types a number

Update readme.md
  specift python version
  give list of packages used

Edgecase in define_allowed_direction where ant has food 'behind' (eg) it but those food have ants on them so they are not accessible.