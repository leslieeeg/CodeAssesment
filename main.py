# Level 1 
"""
Goal: List all tables that are currently free (‘o’ in the chosen timeslot)
Output: A list of table IDs (or the entire table object) representing free tables.
Results a list of the free tables
"""

def list_free_tables(tables):
  #set up an empty list
  free_tables = []
  for table in tables:
    if table["occupied"] == False:
      # add those tables 
      free_tables.append(table["table_id"])

  return free_tables
  
