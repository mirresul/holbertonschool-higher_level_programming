import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Error: template is expected to be a string, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: attendees is expected to be a list of dictionaries, got {type(attendees).__name__}.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            processed_template = processed_template.replace(f"{{{key}}}", str(value))
        
        filename = f"output_{index}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(processed_template)
        except Exception as e:
            print(f"An error occurred while writing to {filename}: {e}")
