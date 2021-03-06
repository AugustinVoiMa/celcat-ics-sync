import datetime
import time
import os

from .rulesmanager import RulesManager

#See rfc 5545 for ical/ics format https://tools.ietf.org/html/rfc5545
icsdatef = "%Y%m%dT%H%M00"
isodatef = "%Y-%m-%dT%H:%M:%S"

def eventstoical(eventlist, filename, conf):
    # Check for dir
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:
            raise
    with open(filename, "w", encoding="utf-8") as file:
        icalbegin(file)
        for event in eventlist:
            icaladdevent(file, event, conf)
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

def icaladdevent(file, ev, conf):
    start = (time.strptime(ev.get("start"), isodatef)) # ISO date format
    end = (time.strptime(ev.get("end"), isodatef)) # ISO date format
    safeprint(file, "BEGIN:VEVENT")
    safeprint(file, "UID:"+ev.get("id"))
    safeprint(file, "DTSTAMP:"+datetime.date.fromtimestamp(time.time()).strftime(icsdatef))
    safeprint(file, "DTSTART:"+ time.strftime(icsdatef, start))
    safeprint(file, "DTEND:"+time.strftime(icsdatef, end))
    icaladdsummary(file,ev, conf)
    safeprint(file, "END:VEVENT")
    return

def icaladdsummary(file, ev, conf):
    text=ev.get("text").split("<br>")
    time_summ = len(text) > 0 and text[0] or "at cookie time"
    category = len(text) > 1 and text[1] or "something"
    title = len(text) > 2 and text[2] or "- [[cookieing]]"
    detail = len(text) > 3 and text[3].replace(";","\\n") or "doing some cookies..."
    loc = len(text) > 4 and text[4] or "maybe on the moon...";

    #DESCRIPTION
    txt = "DESCRIPTION:"\
        +title+"\\n"\
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
    light_title = "- ".join(title.split("- ")[1:]);
    light_title = conf.rulesmanager.digest(light_title)
    txt = "SUMMARY:"\
        + light_title# remove module number (is in the desc)
    safeprint(file, txt)

def safeprint(file, txt):
    for i in range(75,len(txt), 75):
        txt=txt[:i]+"\r\n\t"+txt[i:]
    print(txt, file=file, end="\r\n")
