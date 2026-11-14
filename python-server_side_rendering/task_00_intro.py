#!/usr/bin/python3
"""Module for generating personalized invitation files from a template."""
import os


def generate_invitations(template, attendees):
    """Generate sequential output invitation files from a template and list."""
    if not isinstance(template, str):
        print(f"Invalid input: template must be a string, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for idx, attendee in enumerate(attendees, start=1):
        content = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace(f"{{{key}}}", str(value))

        filename = f"output_{idx}.txt"
        try:
            if os.path.exists(filename):
                print(f"Warning: {filename} already exists, overwriting.")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
        except OSError as e:
            print(f"Error writing {filename}: {e}")
