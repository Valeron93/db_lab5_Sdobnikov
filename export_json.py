from connection import db
import psycopg2
import json

with psycopg2.connect(**db) as conn:

    j = {}

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
            
            return result

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
            
            return result
            

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
            
            return result


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
            return result


    j['genres'] = genres()
    j['authors'] = authors()
    j['poems'] = poems()
    j['poemsauthors'] = poemsauthors()

    with open('export.json', 'w') as f:
        json.dump(j, f, indent=4)
    
