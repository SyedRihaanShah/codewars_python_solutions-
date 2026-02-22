def score(dice):
    points = 0
    points += (dice.count(1) // 3) * 1000
    points += (dice.count(2) // 3) * 200
    points += (dice.count(3) // 3) * 300
    points += (dice.count(4) // 3) * 400
    points += (dice.count(5) // 3) * 500
    points += (dice.count(6) // 3) * 600
    if dice.count(5) >= 4   :
        points += (7 - dice.count(5) ) * 50
    if dice.count(5) < 3 :
        points += dice.count(5) * 50
    if dice.count(1) >= 4:
        points += (7 - dice.count(1) ) * 100
    if dice.count(1) < 3:
        points += dice.count(1) * 100
    return points

a = score([1,1,1,1,1])
print(a)