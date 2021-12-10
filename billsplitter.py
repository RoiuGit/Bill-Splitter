# write your code here
import random as rd

n = int(input('Enter the number of friends joining (including you):\n'))
party = {}
lucky = None
if n > 0:
    print('Enter the name of every friend (including you), each on a new line:')
    for _ in range(1, n + 1):
        name = input()
        party[name] = 0
    bill = int(input('Enter the total bill value:\n'))
    is_lucky = input('Do you want to use the "Who is lucky" feature? Write Yes/No:\n')
    if is_lucky == 'Yes':
        is_lucky = True
    else:
        is_lucky = False
    if is_lucky:
        lucky = rd.choice(list(party.items()))
        print(lucky[0] + ' is the lucky one!')
        for name in party:
            if name not in lucky:
                party[name] = round(bill / (n - 1), 2)
    else:
        print('No one is going to be lucky')
        for name in party:
            party[name] = round(bill / n, 2)
    print(party)
else:
    print('No one is joining for the party')
