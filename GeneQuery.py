#===========================================================
#
# Title:      Gene Query
# Author:     Dan Ouellette
# Description:
#   This Python application connects to public MySQL
# database 'Ensembl/homo_sapiens_core_104_38' and performs
# queries on table 'gene'.
#
#===========================================================
  
#-----------------------------------------------------------
# Imports
#-----------------------------------------------------------
from mysql.connector import connect, Error
import os

#-----------------------------------------------------------
# printCursorFormatted
#-----------------------------------------------------------
def printCursorFormatted(inCursor):

  # Retrieve rows
  dbResult = inCursor.fetchall()

  # Loop to print rows
  print("{:<12}{:<14}{:>10}{:>10}  {:<1}".format( \
    "ID", "Bio Type", "Regn Start", "Regn End", \
    "Description (truncated)"))
  for row in dbResult:
    print("{:<12}{:<14}{:>10}{:>10}  {:<1}".format( \
      row[0], row[1], row[2], row[3], row[4][24:66]))
  print("Rows in result:", dbCursor.rowcount)
  print()

#-----------------------------------------------------------
# printCursorUnformatted
#-----------------------------------------------------------
def printCursorUnformatted(inCursor):

  # Retrieve rows
  dbResult = inCursor.fetchall()

  # Loop to print rows
  for row in dbResult:
    print(row)
  print("Rows in result:", dbCursor.rowcount)
  print()
    
#-----------------------------------------------------------
# Main
#-----------------------------------------------------------

# Set variables
dbHost = "useastdb.ensembl.org"
dbUser = "anonymous"
db = "homo_sapiens_core_104_38"

# Show application header
print ("Welcome to Gene Query")
print ("---------------------\n")

# Attempt to interact with database
try:

  # Connect to database
  dbConnection = connect(
    host = dbHost,
    user = dbUser,
    database = db
  )
  print("Connected to database '", db, "'.", sep="")
  print()

  # Create cursor object
  dbCursor = dbConnection.cursor()

  # Show gene table attributes
  print ("Gene Table Attributes")
  dbCursor.execute("desc gene")
  printCursorUnformatted(dbCursor)

  # Run gene table query unformatted
  print ("Gene Table Query (5 fields and 5 rows selected, " + \
    "unformatted output)")
  dbCursor.execute( \
    "select gene_id, biotype, seq_region_start, " + \
    "seq_region_end, description from gene limit 5")
  printCursorUnformatted(dbCursor)

  # Run gene table query formatted
  print ("Gene Table Query (5 fields and 25 rows selected, " + \
    "formatted output)")
  dbCursor.execute( \
    "select gene_id, biotype, seq_region_start, " + \
    "seq_region_end, description from gene limit 25")
  printCursorFormatted(dbCursor)

  # Close objects
  dbCursor.close()
  dbConnection.close()

# Handle connection error
except Error as e:
  print("Error interacting with database '", db, "'.", sep="")
  print("Error message:", e)
  print()

# Show application close
print ("End of Gene Query")
