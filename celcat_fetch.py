#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import src.fetch as fetch
import src.ical as ical
import json

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

if __name__ == "__main__":
    jseventlist = fetch.getjseventlist("https://edt.univ-tlse3.fr/calendar/default.aspx?View=month&Type=group&ResourceName=formation_EMINAE_s1")
    events = json.loads(jseventlist)
    displayEvent(events[0])
    print(events[0])
    ical.eventstoical(events)
