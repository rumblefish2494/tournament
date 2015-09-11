README
=================================
OVERVIEW:
=================================
This is a PSQL database app for a Swiss Pairings style tournament.
you can add players using the tournament, Enter wins, create pairings for
subsequent matches, delete matches, delete players, get player standings and
get player count.

=================================
INSTRUCTIONS:
=================================
Download all files from git hub repository at https://github.com/rumblefish2494/tournament.git
you must use Udacity vagrant vm setup provided by Udacity, it has been included in
repo https://github.com/rumblefish2494/tournament/tree/master/vagrant
run vagrant and ssh into vagrant. to test app function execute tournament_test.py in python
interpreter in virtual machine.

=================================
API
=================================
the following are available API functions
in the tournament.py file
deleteMatches() - deletes all recorded tournament matches
deletePlayers() - deletes all registered players
countPlayers() - returns count of registered players
registerPlayer(name) - register provide name of player
playerStandings() - returns the current standings of all registered players
reportMatch(winner, loser) - records the winner and loser of a match
swissPairings() - returns a list of pairs for next round of matches


players must be even amount.