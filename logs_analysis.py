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


if __name__ == '__main__':
    main()
