# CSCI 134 Webpage

## Content Changes

All content is specified by `builder/src/components/csci134.json`.

### Info Bar

Each link on the "info bar", i.e. this:

![information bar](images/infobar.png)

is represented by a datum in the following format:

    {
        "id": "info-K",
        "title": "NAME FOR THE LINK",
        "locked": false/true,
        "link": "PUT URL HERE"
    }

### Schedule

Each week in the schedule is represented by a datum in the following format:

    {
        "id": "week-NUM",
        "week": NUM,
        "lab": LAB-DATUM,
        "mon": [MONDAY-DATA],
        "wed": [WEDNESDAY-DATA],
        "fri": [FRIDAY-DATA]
    }



