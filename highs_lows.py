import csv
from matplotlib import pyplot as plt
from datetime import datetime


def main():
    # Get dates, high, low temperatures from file.
    filename = 'data/sitka_weather_2018_full.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        highs, lows, dates = [], [], []
        for row in reader:
            try:
                high = int(row[8])
                highs.append(high)

                low = int(row[9])
                lows.append(low)

                current_date = datetime.strptime(row[2], "%Y-%m-%d")
                dates.append(current_date)
            except ValueError:
                pass

    # Plot data.
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    plt.title("Daily high and low temperatures, 2018", fontsize=24)
    plt.xlabel('', fontsize=1)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major',labelsize=16)

    plt.show()


if __name__ == '__main__':
    main()
