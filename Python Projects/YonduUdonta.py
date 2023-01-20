
'''
Project Name: Yondu Udonta
Author: Cossette Gomez
Due Date: 1/21/23
Course: CS1400-zzz

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.

ok so I start with units_zero and then it turns into units_one
but then after everything is declared I start using units 
'''

def main():
    '''
    Program starts here.
    '''
    try:
        #input and declaring important variables
        # (1) replace pass with your code
        units_zero = input("Units Brought In: ")
        crew_amount = input("Number of Crew Members: ")

        units_zero = int(units_zero)
        crew_amount = int(crew_amount)
        reavers = crew_amount
        units = units_zero

        yondu_share = 0
        peter_share = 0
        crew_share = 0
    except ValueError:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return

    # (2) replace pass with your code
    #print("Here I can put the rest of my code right")
    pass
    #first day
    npc_crew = crew_amount - 2
    spent_units = npc_crew * 3
    units_one = units_zero - spent_units
    units = units_one

    #yondu's share
    yondu_withdraw = units * 13//100
    '''
    test_u = units * .13
    print(yondu_withdraw)
    print(test_u)
    '''
    units -= yondu_withdraw
    yondu_share += yondu_withdraw

    #peter share
    peter_withdraw = units * 11//100
    units -= peter_withdraw
    peter_share += peter_withdraw

    #the next day
    crew_share = units//crew_amount
    peter_share += crew_share
    yondu_share += crew_share

    units -= crew_share*crew_amount
    rbf = units

    #print
    print("Peter's share is ", peter_share)
    print("Yondu's share is ", yondu_share)
    print("Any other crew member's share is ", crew_share)
    print("The amount going to RBF is ", units)

    #checking my work
    unit_payout = (crew_share*npc_crew) +peter_share + yondu_share
    remainder = units_one - unit_payout
    if remainder != rbf:
        print("There's a theiving rat in this port")


if __name__ == "__main__":
    main()
