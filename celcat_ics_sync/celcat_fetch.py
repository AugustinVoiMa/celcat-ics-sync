from . import fetch
from . import ical
import json
from datetime import datetime, timedelta

def displayEvent(ev):
    ev.pop("tag")
    ev.pop("sort")
    ev.pop("doubleClickDisabled")
    ev.pop("clickDisabled")
    ev.pop("resizeDisabled")
    ev.pop("moveDisabled")
    ev.pop("backColor")
    text = ev.pop("text")
    start = ev.pop("start")
    end = ev.pop("end")
    print("event text:")
    print(text)
    print()
    print(start)
    print(end)

def importexport(fromurl, tofile="test.ics", type="month", diff_from=-1, diff_to=10):
    events = []
    for diff_t in range(diff_from, diff_to):
        td = None
        if type=="month":
            td = timedelta(days=diff_t*31)
        elif type=="week":
            td = timedelta(week=diff_t)
        dte = datetime.now() + td
        str_date = dte.strftime("%Y%m%d")
        calurl=fromurl.replace("%date", str_date)
        jseventlist = fetch.getjseventlist(calurl)
        events += json.loads(jseventlist)
    ical.eventstoical(events, tofile)
