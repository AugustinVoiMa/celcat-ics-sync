#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import celcat_ics_sync.celcat_fetch as fetcher
from celcat_ics_sync.conf import Conf

if __name__ == "__main__":
    c = Conf()
    for site in c.sites:
        s = c.getsite(site)
        url = s["url"]
        for cal in s["calendars"]:
            icsout = cal["out"]
            tags = cal["tags"]
            icsout=icsout.replace("%name", tags["name"])
            calurl = str(url)
            for t in ["type", "formation"]:
                calurl=calurl.replace("%"+t, tags[t])
            print("importing "+tags["name"])
            fetcher.importexport(calurl, c, icsout, tags["type"], int(cal["from"]), int(cal["to"]))
