import datetime
import pandas as pd

raw_data: list = [
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
]

column_names: list = []
data: list = []

for line in raw_data:

    currentLine = []

    for key, value in line:
        if key not in column_names:
            column_names.append(key)

        if isinstance(value, tuple):
            value: str = '"' + ','.join(str(i) for i in value) + '"'
            currentLine.append(value)

        elif isinstance(value, datetime.date):
            value = value.strftime("%m/%d/%Y")
            currentLine.append(value)

        else:
            currentLine.append(value)

    data.append(currentLine)

df = pd.DataFrame(data, columns = column_names)

df.to_csv('forecast_data.csv', index=False)