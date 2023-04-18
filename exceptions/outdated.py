# Accepted formaat are 9/8/1636 or September 8, 1636

months = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December" ]

while True:
    date = input("Date: ").title()
    if "/" in date:
        month, day, year = date.split("/")

    elif "," in date:
        date = date.replace(",", "")
        month, day, year = date.split(" ")
        if month in months:
            #Index counting always start from 0
            month = months.index(month) +1
    else:
        continue
    try:
        if int(month) > 12 or int(day) > 31:
            continue
        else:
            break
    except ValueError:
        continue
            #This will present the result in the format 2023-03-05 
            # because of the :02 similar to :.1f for significant fig 
print(year + '-' + f"{int(month):02}" + '-' + f"{int(day):02}")