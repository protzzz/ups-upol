# Filmy
# Verze s iterátory.
#
# Chceme splnit stejný úkol jako v předchozím souboru,
# ale chceme oddělit práci se soubory a s daty.
#
# Připomeňme si zadání:
#
# Úkolem je do zadaného souboru uložit všechny filmy,
# které byly vydány po zadaném roce.

def make_movie(movie_id, title, year, duration):
    return ["movie", movie_id, title, year, duration]

def get_movie_id(movie):
    return movie[1]

def get_movie_title(movie):
    return movie[2]

def get_movie_year(movie):
    return movie[3]

def get_movie_duration(movie):
    return movie[4]

def parse_movie(line):
    vals = line.strip().split("\t")
    return make_movie(vals[0], vals[1], int(vals[2]), int(vals[3]))

"""
>>> parse_movie("tt0044475	Captain Pirate	1952	85\n")
['movie', 'tt0044475', 'Captain Pirate', 1952, 85]
"""

def stringify_movie(movie):
    movie_id = get_movie_id(movie)
    title = get_movie_title(movie)
    year = get_movie_year(movie)
    duration = get_movie_duration(movie)
    return f"{movie_id}\t{title}\t{year}\t{duration}\n"

"""
>>> stringify_movie(make_movie('tt0044475', 'Captain Pirate', 1952, 85))
'tt0044475\tCaptain Pirate\t1952\t85'
>>> print('tt0044475\tCaptain Pirate\t1952\t85\n')
tt0044475	Captain Pirate	1952	85

"""

def load_file_lines(filename):
    with open(filename) as file:
        for line in file:
            yield line

"""
>>> i = load_file_lines("movie.tsv")
>>> next(i)
'tt1042385\tSynapse\t2007\t90\n'
>>> next(i)
'tt0319585\tIvan Makarovich\t1968\t85\n'
"""

def store_file_lines(filename, lines):
    with open(filename, "w") as file:
        for line in lines:
            file.write(line)

"""
store_file_lines("test.tsv", get_file_lines("movie.tsv"))
"""

def parse_movies(lines):
    return map(parse_movie, lines)

"""
>>> movies = parse_movies(load_file_lines("movie.tsv"))
>>> next(movies)
['movie', 'tt1042385', 'Synapse', 2007, 90]
>>> next(movies)
['movie', 'tt0319585', 'Ivan Makarovich', 1968, 85]
>>> next(movies)
['movie', 'tt0281383', 'Yaz Bekari', 1974, 65]
"""

def load_movies():
    return parse_movies(load_file_lines("movie.tsv"))
    
def get_movies_after(movies, year):
    return map(get_movie_title,
               filter(lambda movie: get_movie_year(movie) > year,
                      movies))

"""
>>> titles = get_movies_after(load_movies(), 2020)
>>> next(titles)
'Real Emperor Kandanai Maneesawath'
>>> next(titles)
'The Tender Bar'
>>> next(titles)
'Left Behind: Rise of the Antichrist'
>>> next(titles)
'Free Puppies!'
"""

def store_strings(filename, strings):
    store_file_lines(filename,
                     map(lambda string: string + "\n", strings))

"""
store_strings("test.txt", ["a", "b", "c"])
"""

# Řešení:    
def store_movies_titles_after(output_filename, year):
    return store_strings(output_filename,
                         get_movies_after(load_movies(), year))

"""
store_movies_titles_after("test.txt", 2020)
"""
