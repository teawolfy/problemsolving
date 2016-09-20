def BMI(weight, height):
    calc = 703 * (weight / (height**2))
    if calc <= 18.5:
        return 'you are underweight'
    elif calc <= 24.9:
        return 'you are at a normal weight'
    elif calc <= 29.9:
        return 'you are overweight'
    else:
        return 'you are obese'
user_height = int(input('Please input your height in inches \n'))
user_weight = int(input('Please input your weight in pounds \n'))

print(BMI(user_weight, user_height))