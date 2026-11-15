# Population Data Visualizer
This is a small command-line Python project I built to look at city population data. It reads a CSV file, throws out the rows that don't make sense, and then lets you see reports, charts and a rough forecast.

## What you can do with it
- See a quick summary: total population for the latest year, the biggest city, and which city grew the fastest.
- Check growth rates and pick which chart you want: a line chart of the trend, a bar chart of growth, or both.
- Open an interactive chart in your browser (you can hover and zoom).
- Forecast a city's population for a year you type in (it defaults to 2030).
- View the cleaned data as a table.
- Add or delete records. Changes are saved straight to the CSV.

## What you need
Python 3.8 or later and these libraries:
```
pip install pandas numpy matplotlib plotly
```
## Running it
```
python population_visualizer.py
```

If there's no `population.csv` in the folder, the program makes a small sample one for you. I left two bad rows in it on purpose (a row with "abc" as the population and one with a negative number) so you can see them get skipped.

## CSV format

Three columns, with a header row:

```
City,Year,Population
Raipur,2020,1000000
Raipur,2024,1100000
Durg,2020,500000
Durg,2024,600000
```

## What happens to bad data

A row gets skipped, and the program tells you which row it was, when:

- the year isn't a number,
- the population isn't a number, or
- the population is zero or negative.

If a city has two entries for the same year, the later one wins.

## The menu

1. Summary report
2. Growth rates, then choose a line chart, bar chart or both
3. Interactive chart in the browser
4. Forecast a future population
5. Show the cleaned data
6. Add a record
7. Delete a record (the city name doesn't have to match the capitalisation)
8. Exit

## Things to keep in mind

- Growth is worked out from a city's first year to its last year, so a city needs at least two different years to show a growth figure.
- The forecast just draws a straight line through the data. With only two or three data points it's a very rough guess, so don't read too much into it.
- Deleting a record rewrites the whole CSV, so make a copy first if the data matters to you.