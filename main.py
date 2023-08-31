from data import name_cards
import random

name_cards = name_cards.copy()


def formatting(person: dict):
    """formats and returns a person's dictionary as an f-string."""
    return f"{person['name']}, a {person['job']} from {person['city']}"


def pick_a_person():
    """picks a person from data list, deletes it from list and returns the dictionary."""
    return name_cards.pop(random.randint(0, len(name_cards) - 1))


person_1 = pick_a_person()
person_2 = pick_a_person()
score = 0
while True:
    answer = input(f"Compare A: {formatting(person_1)}...\nAgainst B: {formatting(person_2)}.\nWhich one has more followers? A or B? ")
    if (answer.lower() == 'a' and person_1['follower'] > person_2['follower']) or (answer.lower() == 'b' and person_1['follower'] < person_2['follower']):
        person_1 = person_2
        person_2 = pick_a_person()
        score += 1
        print(f'You are right! current score: {score}')
    else:
        if answer.lower() == 'a':
            print(f"You lost! {person_2['name']} has more followers than {person_1['name']}.\nFinal score: {score}")
        else:
            print(f"You lost! {person_1['name']} has more followers than {person_2['name']}.\nFinal score: {score}")
        break
