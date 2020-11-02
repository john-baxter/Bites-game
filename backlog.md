# Bites project backlog

## Next steps
### Continuous
Liaise with Peter about the front-end

### Current
~~Add second wine rule~~

- ~~this will be "Oenophile", each wine is 1pt per wine~~

Make new score_wine() method in Player that receives the wine_rule as a parameter and uses this info to calculate the wine points.\
Update the score_hand() method to remove the dependancy on score_wine_Collector_method() and uses the new score_wine(wine_rule) method.\
Update render_game to show the wine rule.

### Next
Create a selection (possibly all) of the wine rules
- if doing Protégé remember to address the 0wine=0pts situation.

### Future
Chocolate\
Extra rules\
Fancy CLI

### Bugs discovered:
