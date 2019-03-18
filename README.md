# Logs Analysis Reporting Tool
A reporting tool that will use information from the database to discover what kind of articles the site's readers like.

## Table of Contents

1. [Project Overview] (#project-overview)
1. [Requirements] (#requirements)
1. [Project Contents] (#project-contents)
1. [Project Setup] (#project-setup)

## Project Overview

The database contains newspaper articles, as well as the web server log for the site. Using that information, the code will answer questions about the site's user activity.

The program runs from the command line and does not require any input from the user. It will connect to the database, use SQL queries to analyse the log data, and print out the answers to some questions.

This project was made without using Vagrant and VirtualBox, and developed on Ubuntu 18.04.

## Requirements

In order to run this program, you will need to have the following:

* Python > 3.6
* psycopg2 > 2.7
* PostgreSQL > 10

## Project Contents

The repo has the following files:

* `logs_analysis.py` - Python command line program
* `logs-analysis.txt` - File, plain text, of the expected output
* `requirements.txt` - Python dependencies
* `README.md` - This file

## Project Setup

1. Download the data file, [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), and extract it
1. Open newsdata.sql file and find and replace user vagrant with your postgresql user
1. Load the site's data into your local database, `$ psql -d news -f newsdata.sql`
1. Clone this repo, [logs-analysis](https://github/biobot-01/logs-analysis)
1. Activate Python [venv](https://docs.python.org/3.6/library/venv.html), `$ source path/to/venv/bin/activate`
1. Run the requirements.txt file, `$ pip install -r requirements.txt`
1. Run the program `$ python path/to/logs_analysis.py`
1. View logs-analyse.txt for expected output results
