# Project Summary: Population Data Visualizer

## About the project

This program takes population numbers for a few cities from a CSV file and turns them into something easier to read: totals, growth figures, charts and a simple forecast. It runs from a text menu in the terminal.

## How it works

1. It loads `population.csv` and checks each row. Rows with a bad year, a non-numeric population, or a population of zero or less are skipped, and a message says which row and why. Repeated city/year entries are cleaned up too.
2. The summary report shows the total population in the latest year, the largest city and the fastest-growing city.
3. For growth, it compares each city's first and last year and shows the result as a line chart, a bar chart, or both. The user picks.
4. There's also an interactive Plotly chart that opens in the browser.
5. The forecast fits a straight line to each city's data with NumPy and extends it to the year the user asks for.
6. Records can be viewed, added and deleted, and the CSV is updated each time.

## Libraries used

- pandas for loading and grouping the data
- NumPy for the trend line
- Matplotlib for the regular charts
- Plotly for the interactive chart
- csv and os from the standard library for file handling

## Testing

| Test | What I checked | Result |
|------|----------------|--------|
| 1 | Valid data loads and the summary looks right | Pass |
| 2 | Only one year of data: growth is skipped, no crash | Pass |
| 3 | Bad rows ("abc" and -500) are skipped with a message | Pass |
| 4 | Growth rates print and the chosen chart shows up | Pass |

## Limitations

- The forecast assumes the trend stays perfectly straight, which real populations rarely do.
- Growth only looks at the first and last year, so anything in between is ignored.
- Deleting a record overwrites the CSV file.

## Ideas for later

- Pick specific cities to compare.
- Show year-by-year growth instead of one overall figure.
- Save charts as images.
- Build a simple window-based interface instead of the text menu.