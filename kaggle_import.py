import csv
from connection import db
import psycopg2

dataset = 'all.csv'

rows = []

with open(dataset, newline='') as f:
    reader = csv.DictReader(f)
    rows.extend(reader)

authors = set(i['author'] for i in rows)
genres = set(i['type'] for i in rows)

authors = list(authors)
genres = list(genres)

query = ''

query += 'INSERT INTO Authors(author_id, author_name) VALUES\n'
query += ",\n".join([f"({i}, '{author}')" for i, author in enumerate(authors)])
query += ';\n\n'

query += 'INSERT INTO Genres(genre_id, genre_name) VALUES\n'
query += ",\n".join([f"({i}, '{genre}')" for i, genre in enumerate(genres)])
query += ';\n\n'

def get_rows(rows):
    for row in rows:

        author = row['author']
        name = row['poem name']
        genre = row['type']

        yield author, name, genre

poems = []
manytomany = []
i = 0
for author, name, genre in get_rows(rows):

    author_id = authors.index(author)
    genre_id = genres.index(genre)
    name = name.replace("'", "''")
    poems.append(f"({i}, '{name}', {genre_id})")
    manytomany.append(f"({i}, {author_id}, {i})")
    i += 1

query += "INSERT INTO Poems(poem_id, poem_name, genre_id) VALUES\n"
query += ",\n".join(poems) + ";\n\n"

query += "INSERT INTO PoemsAuthors(authors_id, author_id, poem_id) VALUES\n"
query += ",\n".join(manytomany) + ";\n\n"


with psycopg2.connect(**db) as conn:

    truncate = True
    if truncate:
        with conn.cursor() as cur:
            cur.execute("""
                TRUNCATE TABLE PoemsAuthors, Poems, Authors, Genres;
                        """)

    with conn.cursor() as cur:
        cur.execute(query)
