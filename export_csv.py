from connection import db
import psycopg2
import csv

with psycopg2.connect(**db) as conn:

    def genres():
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Genres;")

            result = []

            data = cur.fetchall()
            
            for genre_id, genre_name in data:
                result.append({
                    'genre_id': genre_id,
                    'genre_name': genre_name,
                })
            
            with open('genres.csv', 'w') as f:
                w = csv.DictWriter(f, ['genre_id', 'genre_name'])
                w.writeheader()
                w.writerows(result)

    def authors():
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Authors;")

            result = []

            data = cur.fetchall()
            
            for author_id, author_name in data:
                result.append({
                    'author_id': author_id,
                    'author_name': author_name,
                })
            
            with open('genres.csv', 'w') as f:
                w = csv.DictWriter(f, ['author_id', 'author_name'])
                w.writeheader()
                w.writerows(result)

    def poems():
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Poems;")

            result = []

            data = cur.fetchall()
            
            for poem_id, poem_name, genre_id in data:
                result.append({
                    'poem_id': poem_id,
                    'poem_name': poem_name,
                    'genre_id': genre_id
                })
            
            with open('poems.csv', 'w') as f:
                w = csv.DictWriter(f, ['poem_id', 'poem_name', 'genre_id'])
                w.writeheader()
                w.writerows(result)

    def poemsauthors():
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM PoemsAuthors;")

            result = []

            data = cur.fetchall()
            
            for authors_id, author_id, poem_id in data:
                result.append({
                    'authors_id': authors_id,
                    'author_id': author_id,
                    'poem_id': poem_id,
                })
            
            with open('poemsauthors.csv', 'w') as f:
                w = csv.DictWriter(f, ['authors_id', 'author_id', 'poem_id'])
                w.writeheader()
                w.writerows(result)


    genres()
    authors()
    poems()
    poemsauthors()
    
