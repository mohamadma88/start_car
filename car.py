def year (day,month,years):
    if day > 10 or month > 10 and month == 10 :
        birthday = years + 622
    elif day > 10 and month == 10 :
        birthday = years + 621
    else :
        birthday = years +621
    print(f'your birthday in {birthday}')

while True :
    day = int(input('plz enter your days birthday : ' ))
    month = int(input('plz enter your month birthday : ' ))
    years = int(input('plz enter your years birthday : ' ))
    year(day,month,years)