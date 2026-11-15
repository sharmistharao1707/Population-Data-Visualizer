# Project Summary: Population Data Visualizer

## About the project

This program takes population numbers for a few cities from a CSV file and turns them into something easier to read: totals, growth figures, charts, and a simple forecast. It runs from a text menu in the terminal.

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
| 4 | Growth rates print, and the chosen chart shows up | Pass |

## Limitations

- The forecast assumes the trend stays perfectly straight, which real populations rarely do.
- Growth only looks at the first and last year, so anything in between is ignored.
- Deleting a record overwrites the CSV file.

## Ideas for later

- Pick specific cities to compare.
- Show year-by-year growth instead of one overall figure.
- Save charts as images.
- Build a simple window-based interface instead of the text menu.


 #### TEST CASE- 01

<img width="291" height="101" alt="image" src="https://github.com/user-attachments/assets/fdc40f06-322a-413a-ac67-937698ce33ac" />

#### TEST CASE- 02

<img width="407" height="150" alt="image" src="https://github.com/user-attachments/assets/62c4087b-54b7-4a7d-b996-c2da50008f7b" />

#### TEST CASE- 03

<img width="293" height="45" alt="image" src="https://github.com/user-attachments/assets/ba8ea8fd-3c2a-4762-b805-4b8d80663a38" />

#### TEST CASE- 04

<img width="221" height="146" alt="image" src="https://github.com/user-attachments/assets/0455ca98-9bd4-4534-b131-35f32b15bc61" />

#### LINE CHART

<img width="426" height="277" alt="image" src="https://github.com/user-attachments/assets/8404150f-8bc0-4941-8a65-bc5d04bf8a00" />
  #### BAR GRAPH

<img width="521" height="346" alt="image" src="https://github.com/user-attachments/assets/3679f98b-80e7-447a-a709-5425f7bd164e" />

#### INTERACTIVE BROWSER LINE CHART

<img width="954" height="503" alt="image" src="https://github.com/user-attachments/assets/0177c9bb-885f-4007-a9b7-ab52107cea4d" />

#### FORECAST FOR FUTURE PREDICTION

<img width="329" height="106" alt="image" src="https://github.com/user-attachments/assets/c850041c-5768-436f-821b-660cd0e3ebf4" />

#### DISPLAYING CLEAN DATA

<img width="250" height="126" alt="image" src="https://github.com/user-attachments/assets/c868735a-da43-4732-a0fd-e3e44a169c0f" />

#### ADDING A RECORD

<img width="113" height="62" alt="image" src="https://github.com/user-attachments/assets/315e9d16-0add-4524-88fe-0a0d886da57f" />

#### DELETING A RECORD

<img width="224" height="52" alt="image" src="https://github.com/user-attachments/assets/4a201d24-8499-481f-9e6c-c294c2a2f452" />

#### EXITING A PROGRAM

<img width="166" height="27" alt="image" src="https://github.com/user-attachments/assets/f5c73a01-72a2-4714-b893-8db438b5b7e2" />










