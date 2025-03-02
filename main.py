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

#Level 3
"""
Goal: Given a party size, return all tables that can seat that many people and are free.
Results in the tables that allow that many free seating
"""
def tables_for_size(tables, party_size):
  available_tables = [] #empty list for IDs

  for table in tables:
    if table["occipied"] == False and table["capacity"] >= party_size:#see if free and fits people
      available_tables.append(table["table_id"])#add table ID to list
      
  return available_tables


# Level 4
"""
Goal: Some restaurants can combine two adjacent tables if one table alone isn’t big enough.
If a single table can’t seat the group, check if two adjacent tables combined have enough capacity.
Output: A list of all table combinations (single or adjacent pairs) that can seat the party.

"""

def table_with_combos(tables, party_size):
  valid_combos = [] #list
  #go through the tables in the list
  for i in range(len(tables)):
    table = tables[i]

    if table["capacity"] >= party_size and table["occupied"] == False:
      valid_combos.append([table["table_id"]]) #current table seat party size

    if i < len(tables) - 1:
      next_one = tables[i+1]
      if table["capacity"] + next_one["capacity"] >= party_size:
        if table["occupied"] == False and next_one["occupied"] == False: # check if both free
          valid_combos.append([table["table_id"], next_one["table_id"]])

  #give the list
  return valid_combos



