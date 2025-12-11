#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template with placeholders
    and a list of attendee objects.

    Args:
        template (str): The invitation template string with placeholders.
        attendees (list): A list of dictionaries, where each dictionary
                          represents an attendee's data.
    """
    
    # Check Input Types
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    if not isinstance(attendees, list):
        print("Error: Attendees is not a list of dictionaries.")
        return
    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees list is not a dictionary.")
        return

    # Handle Empty Inputs
    if not template:
        print("Error: Template is empty, no output files generated.")
        return
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    # Process Each Attendee
    for X, attendee in enumerate(attendees):
        output_filename = f"output_{X + 1}.txt"
        personalized_invitation = template

        # Define placeholders
        placeholders = ["{name}", "{event_title}", "{event_date}", "{event_location}"]

        for placeholder in placeholders:
            key = placeholder[1:-1]
            value = attendee.get(key)
            if value is None:
                personalized_invitation = personalized_invitation.replace(placeholder, "N/A")
            else:
                personalized_invitation = personalized_invitation.replace(placeholder, str(value))

        # Generate Output Files
        try:
            with open(output_filename, 'w') as f:
                f.write(personalized_invitation)
            print(f"Generated {output_filename}")
        except IOError as e:
            print(f"Error writing to file {output_filename}: {e}")
