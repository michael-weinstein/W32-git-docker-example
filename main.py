import rpsSupport

if __name__ == "__main__":
    while True:
        winTable = rpsSupport.standardWins
        result, computerThrow = rpsSupport.game.playARound(winTable)
        print("Computer chose %s. You %s!" %(computerThrow, result))