import nflgame
def getTotalSacks(s, w, t):
    games = nflgame.games_gen(s, w, t, t)
    plays = nflgame.combine_plays(games)

    sks = 0
    for p in plays.filter(team=t):
        if p.defense_sk > 0:
            sks += 1

    return sks

print getTotalSacks(2013, None, "BAL")
