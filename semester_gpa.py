#!/usr/bin/env python3
'''A simple program that computes a semester GPA and cumulative GPA for a 
given student.

Programming features:
    * tuple assignment
'''

def get_grades():
    '''Prompts user for semester grades and assigns it to variable
    semester_grades.

    Returns a list of sublists, in which each sublist contains the letter
    grade for a given course, and the assiciated number of credits. 
    '''
    return


def calculate_gpa(semester_grades, cumm_gpa_info):
    '''Returns a tuple containing the semester GPA and new cummulative GPA
    of the user
    '''
    return

def convert_grade(grade):
    return

# ------- Main

# Program Greeting
print('This program calculates new semester and cummulative GPAs\n')

# Get current GPA info
total_credits = int(input('Enter total number of earned credits: '))
cumm_gpa = float(input('Enter your current cumulative GPA: '))

cumm_gpa_info = (cumm_gpa, total_credits) # Bundled together to allow them to be passed to functions as one parameter

# Get current semester grade info
print()
semester_grades = get_grades()

# Calculate semester gpa and new cummulative gpa
semester_gpa, cumm_gpa = calculate_gpa(semester_grades, cumm_gpa_info)

# Display semester gpa and new cumulative gpa
print('\nYour semester GPA is', format(semester_gpa, '.2f'))
print('Your new cumulative GPA is', format(cumulative_gpa, '.2f'))
