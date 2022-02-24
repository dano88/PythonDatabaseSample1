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

  # Print rows
  print("{:<12}{:<14}{:>10}{:>10}  {:<1}".format( \
    "ID", "Bio Type", "Regn Start", "Regn End", "Description (truncated)"))
  for row in dbResult:
    print("{:<12}{:<14}{:>10}{:>10}  {:<1}".format( \
      row[0], row[1], row[4], row[5], row[9][24:66]))
  print("Rows in cursor:", dbCursor.rowcount)
  print()

#-----------------------------------------------------------
# printCursorUnformatted
#-----------------------------------------------------------
def printCursorUnformatted(inCursor):

  # Retrieve rows
  dbResult = inCursor.fetchall()

  # Print rows
  for row in dbResult:
    print(row)
  print("Rows in cursor:", dbCursor.rowcount)
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

# Attempt to connect to database
try:
  dbConnection = connect(
    host = dbHost,
    user = dbUser,
    database = db
  )
  print("Connected to database '", db, "'.", sep="")
  print()

# Handle connection error
except Error as e:
  print("Error connecting to database '", db, "'.", sep="")
  print("Error message:", e)
  print()
  os._exit(os.X_OK)

# Create cursor object
dbCursor = dbConnection.cursor()

# Show gene table attributes
print ("Gene Table Attributes")
dbCursor.execute("desc gene")
printCursorUnformatted(dbCursor)

# Run gene table query unformatted
print ("Gene Table Query (unformatted, 'select * from gene limit 5')")
dbCursor.execute("select * from gene limit 5")
printCursorUnformatted(dbCursor)

# Run gene table query formatted
print ("Gene Table Query (formatted, 'select * from gene limit 25')")
dbCursor.execute("select * from gene limit 25")
printCursorFormatted(dbCursor)

# Close objects
dbCursor.close()
dbConnection.close()

# Show application close
print ("End of Gene Query")
