import datetime

forecast: list = [
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

forecastHeaders: list = []
forecastLines: list = []

for categories in forecast:
    line = []
    for key, value in categories:
        if key not in forecastHeaders:
            forecastHeaders.append(key)
        if type(value) is tuple:
            value = '"' + ','.join(str(i) for i in value) + '"'
            forecast

        