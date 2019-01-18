import sqlite3
import sys

print(sys.argv) 

loot_db ="loot.db"


class Lootbag():

  def get_gifts(self):
    with sqlite3.connect(loot_db) as conn:
      cursor = conn.cursor()

    for row in cursor.execute("SELECT * FROM Gifts"):
      print(row)

  # ==== LIST (ls) functions

  def get_children_with_gifts(self):
    with sqlite3.connect(loot_db) as conn:
      cursor = conn.cursor()

    for row in cursor.execute("""SELECT c.Name 
                                FROM Children c
                                JOIN Gifts g ON c.Child_ID = g.Child_ID
                                Group BY c.name"""):
      print(row)


  def get_child_gifts(self, child):
    with sqlite3.connect(loot_db) as conn:
      cursor = conn.cursor()
    
    for row in cursor.execute(f"""
                              SELECT g.Name as "Gift Name"
                              FROM Gifts g
                              JOIN Children c ON g.Child_ID = c.Child_ID
                              WHERE c.Name = "{child}"
                              """):
                              print(row)


  # adds a child to database
  def add_child(self, child):
    with sqlite3.connect(loot_db) as conn:
      cursor = conn.cursor()

      try:
        cursor.execute(
          '''
          INSERT INTO Children
          VAlUES(?,?,?)
          ''', (None, child, 1)
        )
      except sqlite3.OperationalError as err:
        print("oops", err)


  # get child id from name
  def get_child_id(self, child):
    with sqlite3.connect(loot_db) as conn:
      cursor = conn.cursor()
      
    
      for row in cursor.execute(f"""SELECT Children.Child_ID
                                    FROM Children 
                                    WHERE Children.Name = '{child}'
                                    """):
        print(int(row[0]))
        return int(row[0])



  # ========== add gift function
  def add_gifts(self, gift, child):
    if self.get_child_id(child) is None:
      self.add_child(child)
      child_ID = self.get_child_id(child)

      with sqlite3.connect(loot_db) as conn:
        cursor = conn.cursor()  

        try:
          cursor.execute(
            '''
            INSERT INTO Gifts
            VAlUES(?,?,?,?)
            ''', (None, gift, 0, child_ID)
          )
        except sqlite3.OperationalError as err:
          print("oops", err)
    else:
     
      child_ID =self.get_child_id(child)

      with sqlite3.connect(loot_db) as conn:
        cursor = conn.cursor()  

        try:
          cursor.execute(
            '''
            INSERT INTO Gifts
            VAlUES(?,?,?,?)
            ''', (None, gift, 0, child_ID)
          )
        except sqlite3.OperationalError as err:
          print("oops", err)


  # ============= remove gift function
  def delete_gift(self, child, gift):
    child_ID = self.get_child_id(child)
    with sqlite3.connect(loot_db) as conn:
      cursor = conn.cursor()

      for row in cursor.execute(f"""DELETE FROM Gifts 
                                    WHERE Gifts.name = '{gift}'   
                                    And Gifts.Child_ID = {child_ID};"""):
        print(row)

  #  ============= delivered gift function
  def delivered_gift(self, child):
    child_ID = self.get_child_id(child)
    with sqlite3.connect(loot_db) as conn:
      cursor = conn.cursor()

      for row in cursor.execute(f"""
                                UPDATE Gifts
                                SET Delivered = 1
                                WHERE Gifts.Child_ID = {child_ID};
                                """):
              
        print(row)

  # ============request handler fx
  def request_handler(self, query, second_arg, third_arg):
    if query == "add":
      self.add_gifts(second_arg, third_arg)
    elif query == "ls":
      if second_arg == "":
        self.get_children_with_gifts()
      else:
        self.get_child_gifts(second_arg)
    elif query == "remove":
      self.delete_gift(second_arg, third_arg)
    elif query =="delivered":
      self.delivered_gift(second_arg)

santas_bag = Lootbag()                      

if __name__ == "__main__":
  santas_bag.request_handler(sys.argv[1], sys.argv[2], sys.argv[3])
  santas_bag.get_gifts()
 