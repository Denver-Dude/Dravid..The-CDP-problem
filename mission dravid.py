import pandas as pd
import random
from tabulate import tabulate  # Import the tabulate library

# Define the time slots
time_slots = [
    "8:30-8:45 (Planning)",
    "8:45-9:00 (Yoga/Sports)",
    "9:00-10:15",
    "10:15-11:15",
    "11:15-12:10",
    "12:10-13:00",
    "13:20-14:10",
    "14:10-14:40"
]

# Define the student names and their class schedules
students = {
    "Student 1": ["Class A", "Class B", "Class C", "Class D", "Class E", "Class F", "Class G", "Class H"],
    "Student 2": ["Class B", "Class C", "Class D", "Class E", "Class F", "Class G", "Class H", "Class A"],
    # Add more students and their schedules here
}

# Create an empty timetable DataFrame
timetable = pd.DataFrame(columns=time_slots)

# Iterate over each student and assign classes randomly
for student, schedule in students.items():
    random.shuffle(schedule)  # Shuffle the class order for each student
    timetable.loc[student] = schedule

# Print the timetable as a table
print(tabulate(timetable, headers='keys', tablefmt='pretty'))
