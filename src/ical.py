import datetime
import time

#See rfc 5545 https://tools.ietf.org/html/rfc5545
icsdatef = "%Y%m%dT%H%M"
isodatef = "%Y-%m-%dT%H:%M:%S"

def eventstoical(eventlist, filename):
    with open(filename, "w", encoding="utf-8") as file:
        icalbegin(file)
        for event in eventlist:
            icaladdevent(file, event)
        icalend(file)
    return

def icalbegin(file):
    print("BEGIN:VCALENDAR", file=file)
    print("VERSION:2.0", file=file)
    print("PRODID:-//Augustin-VM//celcat-to-ics", file=file)
    return


def icalend(file):
    print("END:VCALENDAR", file=file)
    return

def icaladdevent(file, ev):
    start = (time.strptime(ev.get("start"), isodatef)) # ISO date format
    end = (time.strptime(ev.get("end"), isodatef)) # ISO date format
    print(start)
    print(type(start))
    print("BEGIN:VEVENT", file=file)
    print("UID:"+ev.get("id") , file=file)
    print("DTSTAMP:"+datetime.date.fromtimestamp(time.time()).strftime(icsdatef), file=file)
    print("DTSTART:"+ time.strftime(icsdatef, start), file=file)
    print("DTEND:"+time.strftime(icsdatef, end), file=file)
    print("SUMMARY:"+ev.get("text"), file=file)
    print("END:VEVENT", file=file)
    return
