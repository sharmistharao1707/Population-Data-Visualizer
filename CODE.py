import csv
import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

FILE_NAME = "population.csv"

# Create a small sample file if there isn't one yet.
# The last two rows are deliberately bad (text and a negative number)
# so we can check that the loader skips them (test case 3).
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["City", "Year", "Population"])
        writer.writerow(["Raipur", 2020, 1000000])
        writer.writerow(["Raipur", 2024, 1100000])
        writer.writerow(["Durg", 2020, 500000])
        writer.writerow(["Durg", 2024, 600000])
        writer.writerow(["Durg", 2020, "abc"])
        writer.writerow(["Bhilai", 2020, -500])


def load_data(path):
    """Read the CSV, skip rows with bad numbers, and drop repeated city/year pairs."""
    raw_df = pd.read_csv(path, dtype=str)
    good_rows = []

    for idx, row in raw_df.iterrows():
        row_num = idx + 2  # +2 because of the header line and 0-based index

        try:
            year = int(float(row["Year"]))
        except (ValueError, TypeError):
            print(f"Row {row_num} skipped: '{row['Year']}' is not a valid year.")
            continue

        try:
            pop = float(row["Population"])
        except (ValueError, TypeError):
            print(f"Row {row_num} skipped: '{row['Population']}' is not a valid population.")
            continue

        if pop <= 0:
            print(f"Row {row_num} skipped: population has to be above zero.")
            continue

        good_rows.append({"City": row["City"], "Year": year, "Population": int(pop)})

    data = pd.DataFrame(good_rows, columns=["City", "Year", "Population"])
    # If a city/year shows up twice, keep the last one
    data = data.drop_duplicates(subset=["City", "Year"], keep="last")
    return data.reset_index(drop=True)


def calculate_growth(data):
    """Percent change between each city's first and last year on record."""
    growth = {}
    for city, group in data.groupby("City", sort=False):
        group = group.sort_values("Year")
        if len(group) > 1:
            first = group.iloc[0]["Population"]
            last = group.iloc[-1]["Population"]
            growth[city] = (last - first) / first * 100
    return growth


def predict_future_population(city_df, target_year=2030):
    """Fit a straight line through a city's data and extend it to target_year."""
    years = city_df["Year"].values
    pops = city_df["Population"].values

    if len(years) < 2:
        return None

    slope, intercept = np.polyfit(years, pops, 1)
    return max(0, int(slope * target_year + intercept))


def read_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        return None


def show_line_chart(data):
    """Population over time, one line per city."""
    plt.figure(figsize=(7, 4))
    for city, group in data.groupby("City", sort=False):
        group = group.sort_values("Year")
        plt.plot(group["Year"], group["Population"], label=city, marker="o", linewidth=2)
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population Trend")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()


def show_bar_chart(growth):
    """Growth percentage per city."""
    plt.figure(figsize=(7, 4))
    plt.bar(list(growth.keys()), list(growth.values()))
    plt.xlabel("City")
    plt.ylabel("Growth (%)")
    plt.title("Population Growth by City")
    plt.axhline(0, color="black", linewidth=0.8)
    plt.tight_layout()
    plt.show()


def print_summary(data):
    """Print the summary report for whatever data frame we're given."""
    latest_year = data["Year"].max()
    latest_df = data[data["Year"] == latest_year]
    total_pop = latest_df["Population"].sum()
    largest = latest_df.loc[latest_df["Population"].idxmax()]
    growth = calculate_growth(data)

    print("\n" + "-" * 45)
    print("          POPULATION SUMMARY REPORT")
    print("-" * 45)
    if not growth:
        print(f"Total population: {total_pop:,} | Largest city: {largest['City']}")
        print("Growth: not available (only one year of data)")
    else:
        print(f"Total population ({latest_year}): {total_pop:,}")
        print(f"Largest city: {largest['City']} ({largest['Population']:,})")
        fastest = max(growth, key=growth.get)
        print(f"Fastest growing: {fastest} ({growth[fastest]:+.2f}%)")
    print("-" * 45)


df = load_data(FILE_NAME)
print(f"Valid rows: {len(df)}")

while True:
    print("\n" + "=" * 50)
    print("Population Data Visualizer")
    print("=" * 50)
    print("1. Summary report")
    print("2. Single year of data")
    print("3. Growth rates and charts")
    print("4. Interactive chart in the browser")
    print("5. Forecast a future population")
    print("6. Show cleaned data")
    print("7. Add a record")
    print("8. Delete a record")
    print("9. Exit")

    choice = read_int("Enter your choice (1-9): ")

    if choice == 1:
        if df.empty:
            print("No valid data available.")
            continue

        print_summary(df)
    elif choice == 2:
            # Test 2 (boundary case): one city, one year, so there's nothing to compare.
            # The data lives only in memory, so population.csv is left alone.
            print("\n--- Test 2: single year of data ---")
            print("Using one row: Raipur, 2024, 1100000 (population.csv is not changed)")
            single_row = pd.DataFrame([{"City": "Raipur", "Year": 2024, "Population": 1100000}])
            print_summary(single_row)

    elif choice == 3:
        if df.empty:
            print("No valid data available.")
            continue

        growth = calculate_growth(df)

        if not growth:
            print("Growth: not available (only one year of data)")
        else:
            print("\n--- City growth rates ---")
            print(" | ".join(f"{city}: {g:+.2f}%" for city, g in growth.items()))
            print("-------------------------\n")

        print("Which chart would you like to see?")
        print("  1. Population trend (line chart)")
        print("  2. Growth by city (bar chart)")
        print("  3. Both")
        print("  4. Back to main menu")
        chart_choice = read_int("Enter your choice (1-4): ")

        if chart_choice == 1:
            show_line_chart(df)
        elif chart_choice == 2:
            if growth:
                show_bar_chart(growth)
            else:
                print("Bar chart not available (only one year of data).")
        elif chart_choice == 3:
            show_line_chart(df)
            if growth:
                show_bar_chart(growth)
            else:
                print("Bar chart not available (only one year of data).")
        elif chart_choice == 4:
            continue
        else:
            print("Please pick a number from 1 to 4.")

    elif choice == 4:
        if df.empty:
            print("No valid data available.")
            continue

        print("Opening the chart in your browser...")
        fig = px.line(
            df.sort_values("Year"),
            x="Year",
            y="Population",
            color="City",
            title="Population Trend Explorer",
            markers=True,
            template="plotly_dark",
        )
        fig.show()

    elif choice == 5:
        if df.empty:
            print("No valid data available.")
            continue

        target_year = read_int("Year to forecast (press Enter for 2030): ") or 2030
        print(f"\n Population forecast for {target_year}")

        for city, group in df.groupby("City", sort=False):
            if group["Year"].nunique() > 1:
                projected = predict_future_population(group, target_year)
                current = group.sort_values("Year").iloc[-1]["Population"]
                print(f"- {city:<12}: now {current:,} -> projected {projected:,}")
            else:
                print(f"- {city:<12}: not enough data to forecast.")
        print("-" * 55)

    elif choice == 6:
        if df.empty:
            print("Nothing to show, the data is empty.")
        else:
            print("\n" + "-" * 35)
            print(f"{'City':<15} | {'Year':<6} | {'Population':<10}")
            print("-" * 35)
            for _, row in df.iterrows():
                print(f"{row['City']:<15} | {row['Year']:<6} | {row['Population']:<10,}")
            print("-" * 35)

    elif choice == 7:
        city = input("City name: ").strip()
        year = read_int("Year: ")
        pop = read_int("Population: ")

        if not city or year is None or pop is None:
            print("Invalid input: the city can't be blank, and year and population must be whole numbers.")
        elif pop <= 0:
            print("Invalid input: population must be greater than zero.")
        elif ((df["City"] == city) & (df["Year"] == year)).any():
            print("That city already has a record for this year.")
        else:
            df.loc[len(df)] = [city, year, pop]
            with open(FILE_NAME, "a", newline="") as file:
                csv.writer(file).writerow([city, year, pop])
            print("Record added.")

    elif choice == 8:
        city = input("City to delete: ").strip()
        year = read_int("Year to delete: ")

        if not city or year is None:
            print("Invalid input: please give both a city name and a year.")
        else:
            match = (df["City"].str.lower() == city.lower()) & (df["Year"] == year)
            if match.any():
                df = df[~match].reset_index(drop=True)
                df.to_csv(FILE_NAME, index=False)
                print(f"Deleted the record for '{city}' ({year}).")
            else:
                print(f"No record found for '{city}' in {year}.")
    elif choice == 9:
        print("~YAYYY Bye Bye:)~")
        break

    else:
        print("Please pick a number from 1 to 9.")