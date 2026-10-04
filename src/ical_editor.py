from icalendar import Calendar

# Open calendar file
def open_cal(path: str) -> Calendar:
    with open(path, "rb") as f:
        return Calendar.from_ical(f.read())

# Write to new calendar file
def export_cal(path: str, cal: Calendar):
    with open(f"{path}_edited.ics", "wb") as f:
        f.write(cal.to_ical())

# Print calendar to console
def print_cal(cal: Calendar):
    for c in cal.walk():
        if c.name == "VEVENT":
            print("Titel:", c.get("summary"))
            print("Start:", c.get("dtstart").dt)
            print("Ende:", c.get("dtend").dt)
            print("Ort:", c.get("location"))
            print("---")

# Delete all entries with the name
def delete_entries(cal: Calendar, names: list) -> Calendar:
    new_subcomponents = []
    deleted = 0
    for c in cal.subcomponents:
        if c.name == "VEVENT" and str(c.get("summary")) in names:
            deleted += 1
        else:
            new_subcomponents.append(c)

    print(f"Amount of deleted entries: {deleted}")
    cal.subcomponents = new_subcomponents

# Deletes all entries but one 
def delete_all_but(cal: Calendar, names: list) -> Calendar:
    new_subcomponents = []
    deleted = 0
    for c in cal.subcomponents:
        if c.name == "VEVENT" and str(c.get("summary")) not in names:
            deleted += 1
        else:
            new_subcomponents.append(c)

    print(f"Amount of deleted entries: {deleted}")
    cal.subcomponents = new_subcomponents

if __name__ == "__main__":
    #path = f"/home/YBolleininger/Downloads/Icals/Pflichtmodule/5_Sem_INF_Künstliche_Intelligenz_Gr_3.ics"
    
    #keep = ["Computer Grafik ÜL-I6", "Computer Grafik"]
    
    #cal = open_cal(path)

    #print_cal(cal)

    #delete_all_but(cal, keep)
    #print_cal(cal)
    #export_cal(path, cal)
    print("hello")
