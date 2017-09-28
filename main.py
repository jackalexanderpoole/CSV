import csv
import os

ACCEPTED_MSG = """
Dear {},
You have made it onto our course!
Your coach will be {}.
Thank you
"""

REJECTED_MSG = """
Dear {}
I'm afraid you haven't been accepted for our course.
Thank you
"""

file_path = 'text.txt'


file_exists = os.path.exists(file_path)
if file_exists:
	print('Text file exists')
else:
	print('Unable to find text file')
	
file = open(file_path, 'r+')

for line in file:
	print(line)

with open('sheet.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    for row in csv_reader:
        name, email, accepted, coach, language = row

        if accepted == "yes":
            msg = ACCEPTED_MSG.format(name,coach)
            file.write(msg)
        else:
            msg = REJECTED_MSG.format(name)
            file.write(msg)

        print("Send email to: {}".format(email))
        print("Email content: ")
        print(msg)
