#! /usr/bin/python
# -*- coding : utf-8 -*-
# Filename: cacu.py
# Arthur: Hansson Ji
# Date: 9/3/2018

import random
import time
random.seed()
sumP1 = 0
sumPC = 0
count = 0
die1 = 0
die2 = 0
temp = 0
temp2 = 0
tempPc = 0
round_po = 0
round_pc = 0
dec = ''
ask = '\tRoll or hold your dice? (Type in \"R\" to roll, \"H\" to hold. Remenber to press \'Enter\' )\n\tWhat\'s your choice?  '
print('\tWelcome to PIG!!!\n')
time.sleep(.5)
print('\tThis is a easy game, for each round you\n')
time.sleep(.5)
print('\tneed to choose to roll a dice or hold it. \n')
time.sleep(.5)
print('\tYou can keep rolling your dice as long as\n')
time.sleep(.5)
print('\tyou don\'t get a one. If you don\'t hold your\n')
time.sleep(.5)
print('\tpoints, they will be stored in a temporary \n')
time.sleep(.5)
print('\tvariable which means your points will not \n')
time.sleep(.5)
print('\tcount as a part of your sum until you choose\n')
time.sleep(.5)
print('\tto hold the dice. If you get a one, you lose\n')
time.sleep(.5)
print('\tall your temporary points but your sum does\n')
time.sleep(.5)
print('\tnot change if you have chose to hold the dice.\n')
time.sleep(.5)
print('''
\tBy the way, this game also have deluxe and gold edition.
\tThey have more content and more funny staff! There are 
\talso different levels of the game and a better game
\t experience with the computer player!
\t\t\t If you have any interest in these editions
\t\t\t send an email to the email address below:
\t\t\t\t\t murong1213888@gmail.com''')
while sumP1 < 50 and sumPC < 50:

            count = count + 1
            print('\n\tNow is round ' + str(count) + '\n')
            dec = input(ask)
            if dec != 'R' and dec != 'H':
                print('\tPlease enter a valid input.')
                count = count - 1
            if dec == 'R':
                die1 = random.randint(1, 6)
                if sumP1 >= 50:
                    break

                if die1 != 1:
                    temp2 = temp + die1
                    round_po = round_po + temp2
                    time.sleep(.5)
                    print('\tYou rolled: ' + str(die1) + ' points.')
                    time.sleep(1)
                    print('\tNow you have ' + str(round_po) + ' points in round. ')
                    time.sleep(1)
                    print('\tNow you have ' + str(sumP1) + ' points.')
                    time.sleep(1)
                else:
                    round_po = 0
                    temp2 = 0
                    time.sleep(1)
                    print('\tYou rolled: ' + str(die1) + ' point, you lost your turn.')
                    time.sleep(1)
                    print('\tNow you have ' + str(round_po) + ' points in round. ')
                    time.sleep(1)
                    print('\tNow you have ' + str(sumP1) + ' points.')
                    time.sleep(1)

            if dec == 'H':
                    sumP1 = sumP1 + round_po
                    round_po = 0
                    temp2 = 0

                    time.sleep(1)
                    print('\tYou chose to hold, now you have ' + str(sumP1) + ' points.')
                    if sumP1 >= 50:
                        print('\t\nWinner Winner, Chicken Dinner! \n')
                        break
            time.sleep(.5)

            if dec == 'H' or die1 == 1:
                while sumPC < 50:
                    count = count + 1
                    time.sleep(.5)
                    print('\n\tNow is round: ' + str(count))
                    time.sleep(.5)
                    print('\n\tNow is the computer\'s turn. \n')
                    time.sleep(1)
                    die2 = random.randint(1, 6)
                    pc_cho = random.randint(1, 10)  # 计算机随机选择系统
                    if round_pc >= 15:
                        pc_cho = 0
                    if round_pc < 8:
                        pc_cho = 10

                    if round_pc + sumPC >= 50:
                        pc_cho = 0
                    if pc_cho > 3:  # 计算机分数计算
                        if die2 != 1:  # 当计算机选择掷筛子时的分数计算
                            tempPc = temp + die2
                            round_pc = round_pc + tempPc
                            time.sleep(1)
                            print('\tThe computer rolled: ' + str(die2) + ' points.')
                            time.sleep(1)
                            print('\tNow the computer has ' + str(round_pc) + ' points in round. ')
                            time.sleep(1)
                            print('\tNow the computer has ' + str(sumPC) + ' points. ')
                            time.sleep(1)

                            if sumP1 >= 50:
                                break
                        else:  # 当计算机掷出1点时的分数计算
                            round_pc = 0
                            print('\tThe computer rolled: ' + str(die2) + ' point, it lost its turn. ')
                            time.sleep(1)
                            print('\tNow the computer has ' + str(round_pc) + ' points in round. ')
                            time.sleep(1)
                            print('\tNow the computer has ' + str(sumPC) + ' points.')
                            time.sleep(1)
                            if die2 == 1:
                                break
                            if sumP1 >= 50:
                                break
                    else:  # 当计算机选择hold时的分数计算
                        sumPC = sumPC + round_pc
                        round_pc = 0
                        tempPc = 0

                        print('\tThe computer chose to hold, now computer has ' + str(sumPC) + ' points.')
                        time.sleep(.5)
                        break
            if sumPC >= 50:
                print('\n\tYou lose! \n')
                break
            if sumP1 >= 50:
                print('\t\nWinner Winner, Chicken Dinner! \n')
                break


print('\tThis game took ' + str(count) + ' rounds. ')
print('Goodbye! ')
time.sleep(60)
if __name__ == '__main__':
    time.sleep(.5)