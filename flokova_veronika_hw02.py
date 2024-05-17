import json

movies = []
with open('netflix_titles.tsv', encoding='utf-8') as file:
    for line in file:
        movies.append(line.split('\t'))

header = movies[0]
data = movies[1:]

title_index = header.index('PRIMARYTITLE')
directors_index = header.index('DIRECTOR')
cast_index = header.index('CAST')
genres_index = header.index('GENRES')
year_index = header.index('STARTYEAR')

output = []


def clean_item_list(item):
    if len(item) == 1 and item[0] == "":
        return []
    return item


for line in data:
    movie = {
        "title": line[title_index],
        "directors": clean_item_list(line[directors_index].split(',')),
        "cast": clean_item_list(line[cast_index].split(', ')),
        "genres": line[genres_index].split(','),
        "decade": int(line[year_index]) // 10 * 10
    }
    output.append(movie)

with open('hw02_output.json', mode='w', encoding='utf-8') as output_file:
    json.dump(output, output_file, indent=4, ensure_ascii=False)
