import random
def search():
    cnt = 1
    print('Hello! What is your name ?')
    name = input()
    print()
    print('Well,', name, 'I am thinking of a number between 1 and 20.')
    answer = random.randint(1,20)
    n = int(input())
    while n != answer:
        cnt += 1
        if(n > answer):
            print()
            print('Your guess is too high')
        elif(n < answer):
            print()
            print('Your guess is too low')
            n = int(input())
    print('Good job,', name + '!', 'You guessed my number in', cnt, 'guesses!')

search()
