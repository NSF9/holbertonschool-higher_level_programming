def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Error: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(d, dict) for d in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for i, person in enumerate(attendees, start=1):
        output = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = person.get(key) or "N/A"
            output = output.replace(f"{{{key}}}", value)
        with open(f"output_{i}.txt", "w") as file:
            file.write(output)