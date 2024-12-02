import sys
import matplotlib
import matplotlib.pyplot as plt
from load_csv import load
matplotlib.use('TkAgg')


def main():
    """cherche les infos sur la France et les affiche"""
    data = load("life_expectancy_years.csv")
    if data is None:
        sys.exit(1)
    choosen_country = "France"
    i = 0
    while (i < len(data[0])):
        if data[i][0] == choosen_country:
            break
        i += 1
    if i == len(data[0]):
        print(f"Error: The country '{choosen_country}' was not found.")
        sys.exit(1)
    try:
        france_data = list(map(float, data[i][1:]))
        years = list(map(int, data[0][1:]))

    except ValueError:
        print(f"Error: Unable to convert data for '{choosen_country}'")
        sys.exit(1)

    plt.plot(years, france_data, label=choosen_country)
    plt.title(choosen_country + " Life expectancy Projections")
    plt.xticks(range(years[0], years[-1], 40))
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
