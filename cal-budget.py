print("Hello World!")

'''
For men:
BMR = 13.397W + 4.799H - 5.677A + 88.362
For women:
BMR = 9.247W + 3.098H - 4.330A + 447.593

where:
W is body weight in kg
H is body height in cm
A is age
'''

#gender = input(str('Gender M/F: '))
#age = input(int('Enter your age: '))


def height_conversion(): 

    heightImperial = input('Enter height in feet inches, separated by a comma: ')

    height = heightImperial.split(',')
    feet = int(height[0])
    inches = int(height[1])
    inches += feet * 12 
    heightMetric = round(inches * 2.54, 1)
    print(heightMetric)


height_conversion()





