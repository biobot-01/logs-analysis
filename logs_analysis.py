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
    """Fetch the top three articles and print out the results"""
    # SQL query to execute
    sql = """SELECT articles.title, COUNT(log.path) AS views
        FROM articles, log
        WHERE articles.slug = SUBSTR(log.path, 10)
        AND log.status LIKE '2%'
        GROUP BY articles.title
        ORDER BY views DESC
        LIMIT 3;"""
    # Connect to db
    conn, cur = connect_db()
    # Fetch results
    results = get_results_from_query(cur, sql)
    # Disconnect from db
    disconnect_db(conn, cur)
    # Print out the results
    for result in results:
        print("\t\"{}\" - {} views".format(*result))


def top_authors():
    """Fetch the top authors and print out the results"""
    # SQL query to execute
    sql = """SELECT authors.name, COUNT(log.path) AS views
        FROM authors, articles, log
        WHERE authors.id = articles.author
        AND articles.slug = SUBSTR(log.path, 10)
        AND log.status LIKE '2%'
        GROUP BY authors.name
        ORDER BY views DESC;"""
    # Connect to db
    conn, cur = connect_db()
    # Fetch results
    results = get_results_from_query(cur, sql)
    # Disconnect from db
    disconnect_db(conn, cur)
    # Prin out the results
    for result in results:
        print("\t{} - {} views".format(*result))


def requests_to_errors():
    """Fetch requests where more than 1% lead to errors
    and print out the results"""
    # SQL query to execute
    sql = """SELECT total.date,
        ROUND((1.0*errors.count/total.count) * 100, 1) AS percent
        FROM (SELECT to_char(time, 'FMMonth FMDD, YYYY') AS date,
            COUNT(*) AS count
            FROM log
            GROUP BY date) AS total,
            (SELECT to_char(time, 'FMMonth FMDD, YYYY') AS date,
            COUNT(*) AS count
            FROM log
            WHERE status NOT LIKE '2%'
            GROUP BY date) AS errors
        WHERE total.date = errors.date
        AND ROUND((1.0*errors.count/total.count) * 100) > 1.0;"""
    # Connect to db
    conn, cur = connect_db()
    # Fetch results
    results = get_results_from_query(cur, sql)
    # Disconnect from db
    disconnect_db(conn, cur)
    # Prin out the results
    for result in results:
        print("\t{} - {}% errors".format(*result))


def main():
    if connect_db():
        print("\n  Most popular three aricles of all time\n")
        top_three_articles()
        print("\n  Most popular article authors of all time\n")
        top_authors()
        print("\n  Days on which more than 1% of requests lead to errors\n")
        requests_to_errors()


if __name__ == '__main__':
    main()
