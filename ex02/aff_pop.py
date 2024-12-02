import sys
import matplotlib
import matplotlib.pyplot as plt
from load_csv import load
matplotlib.use('TkAgg')


def strchr(s, c):
    for i in range(len(s)):
        if s[i] == c:
            return i
    return -1


def main():
    """se balade dans les fichiers detecte les infos,
    les stocks, les traites, les retires etc...
    modofie k pour tout afficher en millions"
    puis affiche ce qui est demande dans l'exo"""
    data = load("population_total.csv")
    if data is None:
        sys.exit(1)
    choosen_country = "France"
    second_country = "Belgium"
    i = 0
    while (i < len(data[0])):
        if data[i][0] == choosen_country:
            break
        i += 1
    j = 0
    while (j < len(data[0])):
        if data[j][0] == second_country:
            break
        j += 1
    if i == len(data[0]):
        print(f"Error: The country '{choosen_country}' was not found.")
        sys.exit(1)
    if j == len(data[0]):
        print(f"Error: The country '{second_country}' was not found.")
        sys.exit(1)
    tmp_fr = data[i].copy()
    tmp_other = data[j].copy()
    k = 0
    France_data = []
    while (k < len(tmp_fr)):
        if strchr(tmp_fr[k], 'M') != -1:
            tmp_fr[k] = tmp_fr[k].replace('M', '')
            try:
                France_data.append(float(tmp_fr[k]))
            except ValueError:
                try:
                    France_data.append(int(tmp_fr[k]))
                except ValueError:
                    print
                    (f"Error: Unable to convert data for '{choosen_country}'")
                    sys.exit(1)
        k += 1

    k = 0
    other_data = []
    while k < len(tmp_other):
        if 'M' in tmp_other[k] or 'k' in tmp_other[k]:
            if 'M' in tmp_other[k]:
                M = 1
            else:
                M = 0
            tmp_other[k] = tmp_other[k].replace('M', '')
            tmp_other[k] = tmp_other[k].replace('k', '')
            try:
                value = float(tmp_other[k])
                if M == 0:
                    value = float(f"0.{str(value).replace('.', '')}")
                other_data.append(value)
            except ValueError:
                try:
                    value = int(tmp_other[k])
                    if M == 0:
                        value = float(f"0.{str(value).replace('.', '')}")
                    other_data.append(value)
                except ValueError:
                    print
                    (f"Error: Unable to convert data for '{second_country}'")
                    sys.exit(1)
        k += 1

    l_un = France_data[:-50]
    l_deux = other_data[:-50]
    years = list(map(int, data[0][1:252]))
    plt.plot(years, l_un, label=choosen_country)
    plt.plot(years, l_deux, label=second_country)
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.xticks(range(years[0], years[len(years) - 1], 40))
    plt.yticks(range(20, 61, 20), [f"{i}M" for i in range(20, 61, 20)])
    plt.legend(loc="lower right")
    plt.show()


if __name__ == "__main__":
    main()
