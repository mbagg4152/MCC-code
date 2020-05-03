#create program that displays the value
#of a savings account w/ compounded interest
#interest calculated by year
#get initial value
#display total value of account after
#compounding interest for the period of 5 yrs
#annual interest 2%
#run loop w/ out error
#include loop that calculates for 5 years
#display corect grand total
#A=P(1+(r/n))^(nt)
#A=total, r=interest rate , n=times compounded
#anually , t=time periods in years

#create variable to control loop
keep_going = 'yes'
while keep_going == 'yes':

#get initial input from user

    print('Let us see how you account will grow!')

    prin = float(input('What is the current balance of your account? : ' ))
    rate = float(input('What is your annual interest rate/100 (ex. x% => 0.0x) : ' ))


    time = float(input('How many years to you plan on letting your money grow : '))

    #when solved num can be ignored since num is 1

    t_one = int('1')+rate
    #in example tone should be 1.02
    t_two = t_one**time
    #in example ttwo should be 1.104
    t_three = t_two*prin
    #in example tthre should be 552.04

    total = str(round(t_three,2))

    print('Wow that is a long time!')
    print('By then, your account will have $' , total)

    #see if user wants to calculate another

    keep_going = input('Would you like to calculate different' + \
                   ' values? (Enter yes for yes): ')



