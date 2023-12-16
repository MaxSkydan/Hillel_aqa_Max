"""
Hometask 4 List of tuples.

Given list of tuples
(people list -> name, surname, age, profession, City location)
1 - Add your new record with similar random data to the beginning
of the given list
2 - In modified list swap elements with indexes 1 and 5  (1<->5)
and print result
3 - check condition that all people in modified list with records indexes
6, 10, 13 have age >=30 and print result.
"""

import logging

_log = logging.getLogger()
console_handler = logging.StreamHandler()
log_format = logging.Formatter('[%(asctime)s %(levelname)s]: %(message)s')
console_handler.setFormatter(log_format)
_log.addHandler(console_handler)
_log.setLevel(logging.DEBUG)

people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix'),
]

# Add a new record to the beginning of the list
people_records.insert(0, ('Max', 'Sky', 31, 'Engineer', 'Kharkiv'))

# Swap elements with indexes 1 and 5 and print result
people_records[1], people_records[5] = people_records[5], people_records[1]
_log.info(people_records)

# Create variables with age using indexes
# Then we check the age >=30 and print result
age_1 = people_records[6][2]
age_2 = people_records[10][2]
age_3 = people_records[13][2]
check = all((age_1, age_2, age_3 >= 30))
_log.info(check)
