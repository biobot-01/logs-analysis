#!/usr/bin/env python3
"""Reporting tool that prints out reports based on data in a database"""
# Questions this tool should answer:
# 1. What are the most popular three articles of all time?
# 2. Who are the most popular article authors of all time?
# 3. On which days did more than 1% of requests lead to errors?

import psycopg2


def connect_db(dbname="news"):
    """Connect to database and return connection and cursor instance"""
    try:
        # Connect to a database
        conn = psycopg2.connect(dbname=dbname)
        # Open cursor to perform database operations
        cur = conn.cursor()
        # Return connection and cursor instances
        return conn, cur
    except psycopg2.DatabaseError:
        print("Unable to connect to database")


def disconnect_db(conn, cur):
    """Close communication with the database"""
    cur.close()
    conn.close()


def get_results_from_query(cur, sql):
    """Execute sql query and return the results as python objects"""
    # Execute sql command
    cur.execute(sql)
    # Obtain data as python objects
    results = cur.fetchall()
    # Return python objects
    return results


def top_three_articles():
    sql = """select articles.title, count(log.path) as views
        from articles, log
        where articles.slug = substr(log.path, 10)
        and log.status like '2%'
        group by articles.title
        order by views desc
        limit 3;"""

    conn, cur = connect_db()
    results = get_results_from_query(cur, sql)
    disconnect_db(conn, cur)

    for result in results:
        print("\"{}\" - {} views".format(*result))


if __name__ == '__main__':
    main()
