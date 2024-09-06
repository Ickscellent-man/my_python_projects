years = [
    1983, 1984, 1986, 1988, 1991,
    1996, 1997, 2003, 2008, 2016,
    2023
]
albums_count = 0
for year in years:
    if year > 2000:
        albums_count += 1

print('В ХХI веке Metallica выпустила', albums_count, ' альбома')