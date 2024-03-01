# Write a function named friday_the_13th that 
# returns the date of the next friday the 13th.

def friday_the_13th():
    from datetime import datetime, timedelta 
    now = datetime.now()
    
    format = "%A %d"
    
    delta = timedelta(days=1)
    
    while True:
        if now.strftime(format) == 'Friday 13':
            return now.date().isoformat()
            break
        else:
            now += delta

print(friday_the_13th())