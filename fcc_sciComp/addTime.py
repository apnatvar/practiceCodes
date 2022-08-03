def add_time(start, duration, day=""):
    if start[-2:]=='AM':
        start = start[:-3]
        add12 = False
    else:
        start = start[:-3]
        add12 = True
    suffixAMPM = " AM"
    suffixDaysAfter = ""
    start = start.split(':')
    duration = duration.split(':')
    hours = int(start[0])+int(duration[0])
    print(hours)
    if add12:
        hours += 12
    print(hours)
    minutes = int(start[1])+int(duration[1])
    extraHours = minutes//60
    if extraHours != 0:
        minutes -= extraHours*60
        hours += extraHours
        print(hours)
    extraDays = hours//24
    if extraDays != 0:
        hours -= extraDays*24
        print(hours)
        if extraDays == 1:
            suffixDaysAfter = " (next day)"
        else:
            suffixDaysAfter = f" ({extraDays} days later)"
    if hours//12 != 0:
        hours -= 12
        print(hours)
        suffixAMPM = " PM"
    if minutes < 10:
        minutes = "0"+str(minutes)
    else:
        minutes = str(minutes)
    if hours == 0:
        hours = "12"
    else:
        hours = str(hours)
    if day:
        dayToNum = {"mon":0, "tue":1, "wed":2, "thu":3, "fri":4, "sat": 5, "sun": 6}
        numToDay = {0: "Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
        day = ", " + numToDay[(dayToNum[day[:3].lower()]+extraDays)%7]
    return hours + ":" + minutes + suffixAMPM + day + suffixDaysAfter

print(add_time("2:59 AM", "24:00", "monday"))
