#program that preforms an analysis on final grades
#program must use a loop and append each grade to the
#list as it is added
#program asks user to enter final grade (percent score as
#whole number) for 10 students
#program well then display:
#highest score in class
#lowest score in class
#average score in class

#declare final grade percent as whole number for 10 students
print('Hello, this program helps calculate information based on test scores!')
print('You will need to enter 10 values')

def main ():
    n1 = float(input('Grade 1: '))
    n2 = float(input('Grade 2: '))
    n3 = float(input('Grade 3: '))
    n4 = float(input('Grade 4: '))
    n5 = float(input('Grade 5: '))
    n6 = float(input('Grade 6: '))
    n7 = float(input('Grade 7: '))
    n8 = float(input('Grade 8: '))
    n9 = float(input('Grade 9: '))
    n10 = float(input('Grade 10: '))

    strGrade = [ n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

    print('These are the grades you entered: ', strGrade)

    average = sum(strGrade)/len(strGrade)
    high = max(strGrade)
    low = min(strGrade)

    print('The highest grade is: ', high)
    print('The lowest grade is: ', low)
    print('The average grade is: ', average)

    print('Would you like to add more grades?')
    answer = input('Put Y for yes and N for no: ')
    if answer == 'Y':
        while answer == 'Y':
              strGrade.append(float(input('Enter grade here: ')))
              average = sum(strGrade)/len(strGrade)
              high = max(strGrade)
              low = min(strGrade)
              print('These are your new values: ', strGrade)
              print('The new highest grade is: ', high)
              print('The new lowest grade is: ', low)
              print('The new average grade is: ', average)
              print('Would you like to add more grades?')
              answer = input('Put Y for yes and N for no: ')
              if answer == 'N':
                  print('Have a nice day!')
                  

              

    else:
        print('Have a nice day!')
        
             

          
         

main()

