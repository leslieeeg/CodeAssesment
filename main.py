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

# Level 2
"""
Goal: Given a party size (e.g., 2, 3, 4 people), find one table that can seat at least that many people (i.e., capacity >= party_size) and is free.
Output: Return a single table (or table ID) that fits the requirement.
Results in a table ID that fits what user wants
"""
def one_for size(tables, psize):
  for table in tables:
    #see if not in use
    if table["occupied"] == False and table["capacity"] >= party_size:
      return table["table_id"] #conditions met then table ID returned

return None


  
