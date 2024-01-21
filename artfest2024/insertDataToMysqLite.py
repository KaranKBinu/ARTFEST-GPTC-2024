# import sqlite3
# import json
# # Connect to the SQLite database (create a new database if not exists)
# with sqlite3.connect('db.sqlite3') as conn:
#     cursor = conn.cursor()

#     # Create a table if not exists
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS artfest2024_studentdetails (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             student_name TEXT,
#             Gender TEXT,
#             admn_no INTEGER,
#             branch TEXT,
#             sem TEXT,
#             house TEXT
#         )
#     ''')

#     # Commit the changes
#     conn.commit()

#     # Read the data from the file and insert into the database
#     with open('out3.json', 'r') as file:
#         try:
#             # Assuming the data is stored in a valid JSON array
#             student_data_list = json.load(file)

#             for student_data in student_data_list:
#                 cursor.execute('''
#                     INSERT INTO artfest2024_studentdetails (student_name, Gender, admn_no, branch, sem, house)
#                     VALUES (?, ?, ?, ?, ?, ?)
#                 ''', (student_data['student_name'], student_data['Gender'], student_data['admn_no'],student_data['branch'], student_data['sem'],student_data['house']))
#                 print("Insertion Success : ",student_data['student_name'])
#         except json.JSONDecodeError as e:
#             print(f"Error decoding JSON: {e}")




# #     # Commit the changes and close the connection
# #     conn.commit()

# #     # cursor.execute('SELECT * FROM students;')
# #     # rows = cursor.fetchall()
# #     # print("\nInserted Data:")
# #     # for row in rows:
# #     #     print(row)