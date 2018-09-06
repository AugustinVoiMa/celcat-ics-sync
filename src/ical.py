import datetime
import time

#See rfc 5545 https://tools.ietf.org/html/rfc5545
icsdatef = "%Y%m%dT%H%M00"
isodatef = "%Y-%m-%dT%H:%M:%S"

def eventstoical(eventlist, filename):
    with open(filename, "w", encoding="utf-8") as file:
        icalbegin(file)
        for event in eventlist:
            icaladdevent(file, event)
        icalend(file)
    return

def icalbegin(file):
    print("BEGIN:VCALENDAR", file=file, end="\r\n")
    print("VERSION:2.0", file=file, end="\r\n")
    print("PRODID:-//Augustin-VM//celcat-to-ics", file=file, end="\r\n")
    return


def icalend(file):
    print("END:VCALENDAR", file=file, end="\r\n")
    return

def icaladdevent(file, ev):
    start = (time.strptime(ev.get("start"), isodatef)) # ISO date format
    end = (time.strptime(ev.get("end"), isodatef)) # ISO date format
    print("BEGIN:VEVENT", file=file, end="\r\n")
    print("UID:"+ev.get("id") , file=file, end="\r\n")
    print("DTSTAMP:"+datetime.date.fromtimestamp(time.time()).strftime(icsdatef), file=file, end="\r\n")
    print("DTSTART:"+ time.strftime(icsdatef, start), file=file, end="\r\n")
    print("DTEND:"+time.strftime(icsdatef, end), file=file, end="\r\n")
    icaladdsummary(file,ev)
    print("END:VEVENT", file=file, end="\r\n")
    return

def icaladdsummary(file, ev):
    txt = "SUMMARY:"+ev.get("text")
    for i in range(75,len(txt), 75):
        txt=txt[:i]+"\r\n\t"+txt[i:]
    print(txt, file=file, end="\r\n")
