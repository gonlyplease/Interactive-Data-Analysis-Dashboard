import os
from langchain_experimental.sql import SQLDatabaseChain
from langchain.chains.sql_database.query import SQLInput
from langchain.chains.sql_database.query import SQLInputWithTables
from langchain_community.utilities.sql_database import SQLDatabase
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from langchain_openai import OpenAI
import sqlite3


# Use python-dotenv in your Python script to load the environment variables:
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Now you can access the environment variable just like before
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
LANGSMITH_API_KEY = os.environ.get("LANGSMITH_API_KEY")
LANGSMITH_TRACING = os.environ.get("LANGSMITH_TRACING")


def nl_to_sql(nl_query, database_uri):
    input_db = SQLDatabase.from_uri(database_uri)
    llm_1 = OpenAI(temperature=0)
    db_agent = SQLDatabaseChain(
        llm=llm_1, database=input_db, verbose=True, return_sql=True
    )

    sql_querry = db_agent.run(
        nl_query
    )  # e.g. 'Whats the total gross income per branch?'

    return sql_querry


"""Make it better with
provide a database description for your specific use case.
provide descriptions of fields in the db.
hardcoding a few examples of questions and their corresponding SQL queries in the prompt."""


data_dict = {
    "Invoice ID": "Computer generated sales slip invoice identification number",
    "Branch": "Branch of supercenter (3 branches are available identified by A, B and C)",
    "City": "Location of supercenters",
    "Customer Type": "Type of customers, recorded by Members for customers using member card and Normal for without member card",
    "Gender": "Gender of customer",
    "Product Line": "General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel",
    "Unit Price": "Price of each product in $",
    "Quantity": "Number of products purchased by customer",
    "Tax": "5% tax fee for customer buying",
    "Total": "Total price including tax",
    "Date": "Date of purchase (Record available from January 2019 to March 2019)",
    "Time": "Purchase time (10am to 9pm)",
    "Payment": "Payment used by customer for purchase (3 methods are available: Cash, Credit card and Ewallet)",
    "COGS": "Cost of goods sold",
    "Gross Margin Percentage": "Gross margin percentage",
    "Gross Income": "Gross income",
    "Rating": "Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)",
}
