from icalendar import Calendar

def open_cal(path: str) -> Calendar:
    with open(path, "rb") as f:
        return Calendar.from_ical(f.read())

def export_cal(path: str, cal: Calendar):
    with open(f"edited_{path}", "wb") as f:
        f.write(cal.to_ical())


def print_cal(cal: Calendar):
    for c in cal.walk():
        if c.name == "VEVENT":
            print("Titel:", c.get("summary"))
            print("Start:", c.get("dtstart").dt)
            print("Ende:", c.get("dtend").dt)
            print("Ort:", c.get("location"))
            print("---")

def delete_entries(cal: Calendar, name: str) -> Calendar:
    new_subcomponents = []
    deleted = 0
    for c in cal.subcomponents:
        if c.name == "VEVENT" and str(c.get("summary")) == name:
            deleted += 1
        else:
            new_subcomponents.append(c)

    print(f"Amount of deleted entries: {deleted}")
    cal.subcomponents = new_subcomponents

def delete_all_but(cal: Calendar, name: str) -> Calendar:
    new_subcomponents = []
    deleted = 0
    for c in cal.subcomponents:
        if c.name == "VEVENT" and str(c.get("summary")) != name:
            deleted += 1
        else:
            new_subcomponents.append(c)

    print(f"Amount of deleted entries: {deleted}")
    cal.subcomponents = new_subcomponents

if __name__ == "__main__":
    path = "example.ics"
    cal = open_cal(path)
    delete_all_but(cal, "Datenbanken")
    #delete_entries(cal, "Datenbanken ÜL-I1")
    print_cal(cal)
    export_cal(path, cal)
