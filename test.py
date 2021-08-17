
from datetime import datetime
import os

print()
date_string = "Feb 25 2021  4:20PM"
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(datetime_object)

print(os.getcwd())

