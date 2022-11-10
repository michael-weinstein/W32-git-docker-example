rock = "rock"
paper = "paper"
scissors = "scissors"
lizard = "lizard"
spock = "spock"


rpsWinners = {
    rock : [paper],
    paper : [scissors],
    scissors : [rock]
}

rpslsWinners = {
    rock : [paper, spock],
    paper : [scissors, lizard],
    scissors : [rock, spock],
    lizard : [rock, scissors],
    spock : [lizard, paper]
}