from dateutil.relativedelta import relativedelta
from datetime import date, datetime , timedelta

today = date.today()
days = timedelta(days=-1)
print('하루전날쨔' , (today + days))


from dateutil.parser import parse
userDate = parse('2021-7-16')
print('userDate - ' , userDate)






