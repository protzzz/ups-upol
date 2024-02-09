# Motivace k použití iterátorů

# Údaje o filech jsou uloženy v souboru movie.tsv. 
# Soubor je ve formátu TSV (Tab-Separated Values).
# Každý řádek souboru odpovídá jednomu filmu.
# Údaje o filmu jsou odděleny tabulátorem.
# Tabulátor je v Pythonu znak "\t".
# Údaje o filmu jsou: identifikátor filmu,
# název filmu, rok vydání a délka filmu v minutách.

# Datová struktura film:
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

# Převod řádku na film:
def parse_movie(line):
    vals = line.strip().split("\t")
    return make_movie(vals[0], vals[1], int(vals[2]), int(vals[3]))

"""
>>> parse_movie("tt0044475	Captain Pirate	1952	85\n")
['movie', 'tt0044475', 'Captain Pirate', 1952, 85]
"""


# Převod filmu na řádek:
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

# Chceme do zadaného souboru uložit všechny filmy,
# které byly vydány po zadaném roce.
#
# Následující funkce úkol provede,
# ale míchá práci se soubory a s daty dohromady.

def store_movies_titles_after(output_filename, year):
    with open("movie.tsv") as input_file:
        with open(output_filename, "w") as output_file:
            line = input_file.readline()
            while line != "":
                movie = parse_movie(line)
                if get_movie_year(movie) > year:
                    # print(movie)
                    output_file.write(get_movie_title(movie) + "\n")
                line = input_file.readline()

