import typing
import random


def getPlayerThrow(winTable:typing.Dict[str, str]) -> str:
    possibleThrows = list(winTable.keys())
    throwNumbers = {}
    for number, throw in enumerate(possibleThrows):
        throwNumbers[number] = throw
    for number, throw in throwNumbers.items():
        print("%s: %s" %(number, throw))
    playerThrow = input("Select your throw.\n")
    playerThrow = int(playerThrow)
    return throwNumbers[playerThrow]


def determineOutcome(winTable:typing.Dict[str, str], computerThrow:str, playerThrow:str) -> typing.Tuple[str, str]:
    if computerThrow == playerThrow:
        result = "tied"
    elif playerThrow in winTable[computerThrow]:
        result = "won"
    else:
        result = "lost"
    return result, computerThrow


def getComputerThrow(winTable:typing.Dict[str, str]) -> str:
    possibleThrows = list(winTable.keys())
    return random.choice(possibleThrows)


def playARound(winTable:typing.Dict[str, str]) -> typing.Tuple[str, str]:
    computerThrow = getComputerThrow(winTable)
    playerThrow = getPlayerThrow(winTable)
    return determineOutcome(winTable, computerThrow, playerThrow)

