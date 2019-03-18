#!/usr/bin/env python3
"""Reporting tool that prints out reports based on data in a database"""
# Questions this tool should answer:
# 1. What are the most popular three articles of all time?
# 2. Who are the most popular article authors of all time?
# 3. On which days did more than 1% of requests lead to errors?

import psycopg2

# Constant variables
DBNAME = 'news'


def get_query_from_db(sql):
    # Connect to a database
    conn = psycopg2.connect(dbname=DBNAME)
    # Open cursor to perform database operations
    cur = conn.cursor()
    # Execute sql command
    cur.execute(sql)
    # Obtain data as python objects
    results = cur.fetchall()
    # Close communication with the database
    cur.close()
    conn.close()
    # Return python objects
    return results


if __name__ == '__main__':
    main()
