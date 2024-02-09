# Filmy (popis dat)
#
# Údaje o filmech a režisérech se nalázají ve třech souborech:
#   1. movie.tsv
#   2. person.tsv
#   3. director.tsv      
#
# Soubory jsou ve formátu TSV (Tab-Separated Values).
# Každý řádek souboru obsahuje položky oddělené tabulátorem.
#
# Údaje o filmech a režisérech se nalázají ve třech souborech:
#   1. movie.tsv
#      Řádek popisuje film.
#
#   2. person.tsv
#      Řádek popisuje osobu.
#
#   3. director.tsv
#      Řádek určuje režiséra filmu.
#      (Film může mít více režisérů)
#
# Položky řádku v movie.tsv:
#   1. identifikátor filmu
#   2. název filmu
#   3. rok vydání
#   4. délka v minutách
#
# Položky řádku v person.tsv:
#   1. identifikátor osoby
#   2. jméno osoby
#   3. rok narození
#
# Položky řádku v director.tsv:
#   1. identifikátor filmu
#   2. identifikátor osoby
#
# Úkoly:
#   1. Najděte všechny osoby narozené v zadaném roce.
#   2. Jaké filmy režíroval zadaný režisér?
#   3. Které filmy mají více jak jednoho režiséra?
