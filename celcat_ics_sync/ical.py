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
    safeprint(file, "BEGIN:VCALENDAR")
    safeprint(file, "VERSION:2.0")
    safeprint(file, "PRODID:-//Augustin-VM//celcat-to-ics")
    return


def icalend(file):
    safeprint(file, "END:VCALENDAR")
    return

def icaladdevent(file, ev):
    start = (time.strptime(ev.get("start"), isodatef)) # ISO date format
    end = (time.strptime(ev.get("end"), isodatef)) # ISO date format
    safeprint(file, "BEGIN:VEVENT")
    safeprint(file, "UID:"+ev.get("id"))
    safeprint(file, "DTSTAMP:"+datetime.date.fromtimestamp(time.time()).strftime(icsdatef))
    safeprint(file, "DTSTART:"+ time.strftime(icsdatef, start))
    safeprint(file, "DTEND:"+time.strftime(icsdatef, end))
    icaladdsummary(file,ev)
    safeprint(file, "END:VEVENT")
    return

def icaladdsummary(file, ev):
    text=ev.get("text").split("<br>")
    time_summ = text[0]
    category = text[1]
    title = text[2]
    detail = text[3].replace(";","\\n")
    loc = len(text) > 4 and text[4] or "maybe on the moon...";

    #DESCRIPTION
    txt = "DESCRIPTION:"\
        +time_summ+"\\n"\
        +category+"\\n"\
        +loc+"\\n\\n"\
        +detail
    safeprint(file, txt)

    #LOCATION
    txt = "LOCATION:"\
        +loc
    safeprint(file,txt)

    #CATEGORY
    txt = "CATEGORY:"\
        +category
    safeprint(file, txt)

    #SUMMARY
    txt = "SUMMARY:"\
        +title
    safeprint(file, txt)

def safeprint(file, txt):
    for i in range(75,len(txt), 75):
        txt=txt[:i]+"\r\n\t"+txt[i:]
    print(txt, file=file, end="\r\n")
