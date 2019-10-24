#orig code: https://www.saltycrane.com/blog/2010/10/how-get-date-n-days-ago-python/

from datetime import datetime, timedelta

N = input("Enter days to subtract: ")

date_N_days_ago = datetime.now() - timedelta(days=int(N))

print(datetime.now())
print(date_N_days_ago)