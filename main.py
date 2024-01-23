import psycopg2
from matplotlib import pyplot as plt
from connection import db

QUERY_1 = "SELECT * FROM PoemsCountByAuthor;"
QUERY_2 = "SELECT * FROM PoemsCountByGenre;"
QUERY_3 = "SELECT * FROM PoemsCountByAuthorWithGenreLove;"

vis_1, vis_2, vis_3 = [], [], []

with psycopg2.connect(**db) as conn:

    for l, q in zip([vis_1, vis_2, vis_3], [QUERY_1, QUERY_2, QUERY_3]):
        with conn.cursor() as cur:
            cur.execute(q)
            l.extend(cur.fetchall())

def q1():

    fig, ax = plt.subplots()
    authors = [author for author, _ in vis_1]
    counts = [count for _, count in vis_1]
    ax.set_title('Кількість віршів від автора')
    ax.bar(authors, counts)
    fig.savefig('q1.png')


def q2():
    fig, ax = plt.subplots()
    genres = [genre for genre, _ in vis_2]
    counts = [count for _, count in vis_2]

    ax.set_title('Розподіл віршів за жанром')
    ax.pie(counts, labels=genres, autopct='%1.1f%%')
    fig.savefig('q2.png')


def q3():
    fig, ax = plt.subplots()

    authors = [author for author, _ in vis_3]
    counts = [count for _, count in vis_3]

    ax.set_title('Кількість віршів від автора з жанром "Love"')
    ax.bar(authors, counts)

    fig.savefig('q3.png')

q1()
q2()
q3()

