# Bites project backlog

## Next steps
### Continuous
Liaise with Peter about the front-end

### Current

### Next
Chocolate:
- ~~include chocolate in the trail~~
- ~~figure out how/where to position it within the trail~~
- ~~create a mechanism for it to be 'spent' from the player's hand~~
- ~~prompt player to use chocolate before and/or after regular turn~~
  * ~~only if they have chocolate~~
- ~~implement the following rules:~~
  * ~~Doubler~~
  * ~~Theif~~
- ~~update `choose_game_rule()` to allow players to choose chocolate rule~~
- update the `take_turn()` method so that it recieves the chocolate_rule as a parameter and calls the appropriate rule from the CHOC_RULES dict.
- include an extra print statement in `render_game()` to show the choc rule while playing.


### Future
Change printing of '--' in trail so that it only prints one if there are multiple in a row.\
Check the justification wrt chocolate.\
Consider changing player hand to a counter instead of a dict\
Create new companion doc for 
<span>README.md</span> 
that has tables explaining each rule\
Create a selection (possibly all) of the wine rules
- if doing Protégé remember to address the 0wine=/=0pts situation.

Create a selection (possibly all) of the chocolate rules\
Extra rules\
Fancy CLI\
Look at 
[comment](https://github.com/john-baxter/Bites-game/pull/27#discussion_r520486699) 
from feature-wine pull request\
Investigate the possibility of refactoring the chocolate methods into their own class Chocolate(), which could be inherited by Player

### Bugs discovered:
Game crashing at end (calc score phase). Incorrect number of arguments in score_hand().