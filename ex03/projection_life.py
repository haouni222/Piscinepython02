import sys
import matplotlib
import matplotlib.pyplot as plt
from load_csv import load
matplotlib.use('TkAgg')


def main():
    """se balade dans les fichiers detecte les infos,
    les stocks, les traites, les retires etc...
    puis affiche ce qui est demande dans l'exo"""
    data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy = load("life_expectancy_years.csv")
    if data is None:
        sys.exit(1)
    i = 1
    ii = 1
    to_take_off = []
    life_infos = []
    while (ii < len(life_expectancy[0])):
        if int(life_expectancy[0][ii]) == 1900:
            break
        ii += 1
    j = 1
    while j < len(life_expectancy):
        try:
            life_infos.append(float(life_expectancy[j][ii]))
        except ValueError:
            try:
                life_infos.append(int(life_expectancy[j][ii]))
            except ValueError:
                to_take_off.append(life_expectancy[j][0])
                pass
        j += 1
    while (i < len(data[0])):
        if int(data[0][i]) == 1900:
            break
        i += 1
    j = 1
    infos = []
    while j < len(data):
        if data[j][0] not in to_take_off:
            infos.append(int(data[j][i]))
        j += 1
    plt.title("1900")
    plt.plot(infos, life_infos, 'o')
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
