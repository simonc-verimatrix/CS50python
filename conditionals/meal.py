def main():
    uhrzeit = input("What time is it? ")
    uhrzeit = convert(uhrzeit)
    if 7.5 <= uhrzeit<= 8:
        print("breakfast time")
    elif 12.0 <= uhrzeit<= 13:
        print("Lunch time") 
    elif 18 <= uhrzeit<= 19:
        print("Dinner time")
        
 #   print(convert(uhrzeit))

def convert(time):
    hour , minute = time.split(":")
    time = float(hour) + (float(minute) / 60)
    return time


if __name__ == "__main__":
    main()
