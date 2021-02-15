scores = input().split()
life = 3
score = 0
for sc in scores:
    if sc == 'I':
        life -= 1
    else:
        score += 1
    if life == 0:
        break

if life > 0:
    print("You won")
    print(score)
else:
    print("Game over")
    print(score)