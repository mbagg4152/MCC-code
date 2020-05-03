#create program that reads all info in a text file
#and that calculates the sum of all numbers in text file
#then displays value as total points to screen
#then calculate average off all values (scores) then
#display average as a percent score to screen
#make sure program handles IOerror and ValueError exceptions

try:
    #open numdata file
    datafile = open('numdata.txt', 'r')

    #read all numbers from the file
    num1 = int(datafile.readline())
    num2 = int(datafile.readline())
    num3 = int(datafile.readline())
    num4 = int(datafile.readline())
    num5 = int(datafile.readline())
    num6 = int(datafile.readline())
    num7 = int(datafile.readline())
    num8 = int(datafile.readline())

    #close the file
    datafile.close()

    #add numbers/get average/ get percent
    total = num1 + num2 + num3 + num4+ num5 + num6 + num7 + num8
    average = total/8
    per = average/total
    percent = per * 100

    #disply numbers and info
    print('The scores are: ', num1, num2, num3, num4, num5, num6, num7, num8)
    print('The total of the scores is: ', total)
    print('The average score is: ', average)
    print('The percentage of the average is : ', percent) 

except IOError:
    print('An error has occured while reading the data file')
