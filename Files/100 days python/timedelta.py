from datetime import datetime

from datetime import timedelta

t = timedelta(days=4,hours=10)
print(t.seconds)

print(t.seconds/60/60)

eta =timedelta(hours=6)
today=datetime.today()

print(str(today+eta))





