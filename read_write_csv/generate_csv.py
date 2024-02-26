# --------------------------------------
# Exercise 1:
# Create a function to convert the 
# sample data below into a csv file
# --------------------------------------
# Exercise 2:
# Create a function to parse the
# student.csv sample file into a dict
# --------------------------------------
import datetime
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4, sort_dicts=True)

wReport: list = [
    (
        ("temperature", 42),
        ("date", datetime.date(2017, 1, 22)),
        ("locations", ("Berlin", "Paris")),
        ("weather", "sunny"),
    ),
    (
        ("temperature", -42),
        ("date", datetime.date(2017, 1, 22)),
        ("locations", ("Marseille", "Moscow")),
        ("weather", "cloudy"),
    ),
    (
        ("temperature", 30),
        ("date", datetime.date(2017, 1, 23)),
        ("locations", ("London", "New York")),
        ("weather", "rainy"),
    ),
    (
        ("temperature", 20),
        ("date", datetime.date(2017, 1, 23)),
        ("locations", ("Tokyo", "Sydney")),
        ("weather", "windy"),
    ),
]

def generate_csv(dataList: list):
    import csv
    column_names: list = []
    fdata = []
    for line in dataList:
        currentLine = []
        for info, value in line:
            info: str = info.capitalize()
            if info not in column_names:
                column_names.append(info)
            if isinstance(value, (list,tuple)):                     # list or tuple
                value: str = ','.join(str(i) for i in list(value))
                currentLine.append(value)
            elif type(value) == datetime.date:                      # date obj.
                value = value.strftime("%m/%d/%Y")
                currentLine.append(value)
            else:
                currentLine.append(value)                           # str or int
        fdata.append(currentLine)
    with open('forecast_data.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(column_names)
        writer.writerows(fdata)
    pp.pprint(fdata)
generate_csv(wReport)

# --------------------------------------
# --------------------------------------

def parse_csv():
    from csv import DictReader
    from datetime import datetime
    table: list[dict] = []
    with open('students.csv', 'r') as file:
        reader = DictReader(file, quotechar='"')
        for people in reader:
            person: dict = {}
            for info in people:
                if info == 'Birthdate':
                    person[info] = datetime.strptime(people[info], "%m/%d/%Y").date()
                elif info == 'Marks':
                    person[info] = list(int(i) for i in people[info].split(','))
                else:
                    person[info] = people[info]
            table.append(person)
    pp.pprint(table)
    
parse_csv()