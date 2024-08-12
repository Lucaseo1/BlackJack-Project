"""
Digital Ready Summer 2024
Card Game Project

Write your card game here!
"""
from card import Card
from rank import Rank
from suit import Suit
from card import deck
import random

CompCards = []
PlayerCards = []
print("BlackJack")
while len(CompCards) < 2:
    choices = deck
    comp = random.choices(choices)
    PH = PlayerCards
    PlayerCards.append(comp)
    CH = CompCards
    choices = deck
    comp = random.choices(choices)
    CompCards.append(comp)
    
print("Players Hand is:" +str(PlayerCards))
print("Computer Hand is:" +str(CompCards))
score2 = 0
for card in PlayerCards:
    score2 += card[0].rank
while score2 < 21:
    HorS = input("Would you like to 'hit' or 'stand'")
    if HorS != 'hit' and HorS != 'stand':
        print("That is an invalid option")
    if HorS == 'hit':
        choices = deck
        comp = random.choices(choices)
        PlayerCards.append(comp)
        print("You drew a", comp)
        print(PlayerCards)
        score2 += comp[0].rank
    if HorS == 'stand':
        print("Your final hand is", PlayerCards)
        score2 += 100

score = 0
for card in CompCards:
    score += card[0].rank

if score2 <= 21:
    while score < 17:
        choices = deck
        comp = random.choices(choices)
        CompCards.append(comp)
        score += comp[0].rank

if HorS == 'hit' and score2 > 21:
    score2 += 100
if score2 > 21:
    score2 -= 100

print(CompCards)
print("Computers final score is:" +str(score))
print("Players final score is:" +str(score2))

if score > score2 and score <= 21:
    print("Dealer Victory You Lose")
if score < score2 and score2 <= 21:
    print("Player Victory Congratulations")
if score > 21:
    print("Computer goes over 21 and busts Player Victory")
if score2 > 21:
    print("Players hand went over 21 and bust Computer Victory")
