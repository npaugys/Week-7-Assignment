#I attempted the Intermediate level for this assignment
'''
Task added with ID: 1
Task added with ID: 2
Task added with ID: 3
Task added with ID: 4
Task added with ID: 5
Task added with ID: 6

=== Pending Tasks ===
ID   Title                          Priority   Status       Due Date
---  ----------------------------  --------  ----------  ----------
1    Finish project report          High       Pending      2024-06-30  
6    Client feedback                High       Pending      2024-07-01  
3    Team meeting                   Low        Pending      2024-06-25  
5    Update documentation           Low        Pending      2024-07-10  
4    Code review                    Medium     Pending      2024-06-28  
2    Prepare presentation           Medium     Pending      2024-07-05  

Task status updated successfully.

Task deleted successfully.
ID   Title                          Priority   Status       Due Date
---  ----------------------------  --------  ----------  ----------
1    Finish project report          High       Pending      2024-06-30  
6    Client feedback                High       Pending      2024-07-01  
3    Team meeting                   Low        In Progress  2024-06-25  
5    Update documentation           Low        Pending      2024-07-10  
4    Code review                    Medium     Pending      2024-06-28 

------

Task added with ID: 7
Task added with ID: 8
Task added with ID: 9
Task added with ID: 10
Task added with ID: 11
Task added with ID: 12

=== Pending Tasks ===
ID   Title                          Priority   Status       Due Date
---  ----------------------------  --------  ----------  ----------
1    Finish project report          High       Pending      2024-06-30  
7    Finish project report          High       Pending      2024-06-30  
6    Client feedback                High       Pending      2024-07-01  
12   Client feedback                High       Pending      2024-07-01  
3    Team meeting                   Low        In Progress  2024-06-25  
9    Team meeting                   Low        Pending      2024-06-25  
5    Update documentation           Low        Pending      2024-07-10  
11   Update documentation           Low        Pending      2024-07-10  
4    Code review                    Medium     Pending      2024-06-28  
10   Code review                    Medium     Pending      2024-06-28  
8    Prepare presentation           Medium     Pending      2024-07-05  

Task status updated successfully.

Task not found or failed to delete.

ID   Title                          Priority   Status       Due Date
---  ----------------------------  --------  ----------  ----------
1    Finish project report          High       Pending      2024-06-30  
7    Finish project report          High       Pending      2024-06-30  
6    Client feedback                High       Pending      2024-07-01  
12   Client feedback                High       Pending      2024-07-01  
3    Team meeting                   Low        In Progress  2024-06-25  
9    Team meeting                   Low        Pending      2024-06-25  
5    Update documentation           Low        Pending      2024-07-10  
11   Update documentation           Low        Pending      2024-07-10  
4    Code review                    Medium     Pending      2024-06-28  
10   Code review                    Medium     Pending      2024-06-28  
8    Prepare presentation           Medium     Pending      2024-07-05  

-------

Task added with ID: 13
Task added with ID: 14
Task added with ID: 15
Task added with ID: 16
Task added with ID: 17
Task added with ID: 18

=== Pending Tasks ===
ID   Title                          Priority   Status       Due Date
---  ----------------------------  --------  ----------  ----------
1    Finish project report          High       Pending      2024-06-30  
7    Finish project report          High       Pending      2024-06-30  
13   Finish project report          High       Pending      2024-06-30  
6    Client feedback                High       Pending      2024-07-01  
12   Client feedback                High       Pending      2024-07-01  
18   Client feedback                High       Pending      2024-07-01  
3    Team meeting                   Low        In Progress  2024-06-25  
9    Team meeting                   Low        Pending      2024-06-25  
15   Team meeting                   Low        Pending      2024-06-25  
5    Update documentation           Low        Pending      2024-07-10  
11   Update documentation           Low        Pending      2024-07-10  
17   Update documentation           Low        Pending      2024-07-10  
4    Code review                    Medium     Pending      2024-06-28  
10   Code review                    Medium     Pending      2024-06-28  
16   Code review                    Medium     Pending      2024-06-28  
8    Prepare presentation           Medium     Pending      2024-07-05  
14   Prepare presentation           Medium     Pending      2024-07-05  

Task status updated successfully.

Task not found or failed to delete.

ID   Title                          Priority   Status       Due Date
---  ----------------------------  --------  ----------  ----------
1    Finish project report          High       Pending      2024-06-30  
7    Finish project report          High       Pending      2024-06-30  
13   Finish project report          High       Pending      2024-06-30  
6    Client feedback                High       Pending      2024-07-01  
12   Client feedback                High       In Progress  2024-07-01  
18   Client feedback                High       Pending      2024-07-01  
3    Team meeting                   Low        In Progress  2024-06-25  
9    Team meeting                   Low        Pending      2024-06-25  
15   Team meeting                   Low        Pending      2024-06-25  
5    Update documentation           Low        Pending      2024-07-10  
11   Update documentation           Low        Pending      2024-07-10  
17   Update documentation           Low        Pending      2024-07-10  
4    Code review                    Medium     Pending      2024-06-28  
10   Code review                    Medium     Pending      2024-06-28  
16   Code review                    Medium     Pending      2024-06-28  
8    Prepare presentation           Medium     Pending      2024-07-05  
14   Prepare presentation           Medium     Pending      2024-07-05  

------

see test_delete_all(conn)

cursor.execute(''''DELETE FROM tasks'''')
    conn.commit()
    display_tasks(get_all_tasks(conn))

No tasks found.

------

INTERMEDIATE

Project added with ID: 1
Project added with ID: 2

Task added with ID: 1
Task added with ID: 2
Task added with ID: 3
Task added with ID: 4
Task added with ID: 5
Task added with ID: 6
=== All Tasks with Project ===
ID   Title                          Priority   Status       Due Date
Project
---  ----------------------------  --------  ----------  ----------
-------------
6    Client feedback                High       Pending      2026-10-01
(No Project)

1    Finish project report          High       Pending      2026-10-30
History paper

5    Update documentation           Low        Pending      2026-10-10
Programming assignment

3    Team meeting                   Low        Pending      2026-10-25
Programming assignment

2    Prepare presentation           Medium     Pending      2026-10-05
History paper

4    Code review                    Medium     Pending      2026-10-28
Programming assignment


=== Project Summary for Project ID 2 ===
Status: Pending, Count: 3

=== Search Results for Keyword 'Review' ===
Task ID: 5 | Title: Update documentation | Description: Review and update project documentation
Task ID: 4 | Title: Code review | Description: Review code submitted by team members

Successfully exported 6 rows to 'tasks_export.csv'.

------

=== All Tasks with Project ===
ID   Title                          Priority   Status       Due Date
Project
---  ----------------------------  --------  ----------  ----------
-------------
6    Client feedback                High       Pending      2026-10-01
(No Project)

1    Finish project report          High       Pending      2026-10-30
History paper

5    Update documentation           Low        Pending      2026-10-10
Programming assignment

3    Team meeting                   Low        Pending      2026-10-25
Programming assignment

2    Prepare presentation           Medium     Pending      2026-10-05
History paper

4    Code review                    Medium     Done         2026-10-28
Programming assignment


=== Project Summary for Project ID 2 ===
Status: Done, Count: 1
Status: Pending, Count: 2

------

=== Search Results for Keyword 'gibberish' ===
No tasks found.

------

ID,Title,Description,Priority,Status,Due Date,Project Name
6,Client feedback,Incorporate feedback received from the client,High,Pending,2026-10-01,
12,Client feedback,Incorporate feedback received from the client,High,Pending,2026-10-01,
18,Client feedback,Incorporate feedback received from the client,High,Pending,2026-10-01,
1,Finish project report,Complete the final report for the project,High,Pending,2026-10-30,History paper
7,Finish project report,Complete the final report for the project,High,Pending,2026-10-30,History paper
13,Finish project report,Complete the final report for the project,High,Pending,2026-10-30,History paper
5,Update documentation,Review and update project documentation,Low,Pending,2026-10-10,Programming assignment
11,Update documentation,Review and update project documentation,Low,Pending,2026-10-10,Programming assignment
17,Update documentation,Review and update project documentation,Low,Pending,2026-10-10,Programming assignment
3,Team meeting,Discuss project progress with the team,Low,Pending,2026-10-25,Programming assignment
9,Team meeting,Discuss project progress with the team,Low,Pending,2026-10-25,Programming assignment
15,Team meeting,Discuss project progress with the team,Low,Pending,2026-10-25,Programming assignment
2,Prepare presentation,Create slides for the upcoming presentation,Medium,Pending,2026-10-05,History paper
8,Prepare presentation,Create slides for the upcoming presentation,Medium,Pending,2026-10-05,History paper
14,Prepare presentation,Create slides for the upcoming presentation,Medium,Pending,2026-10-05,History paper
4,Code review,Review code submitted by team members,Medium,Done,2026-10-28,Programming assignment
10,Code review,Review code submitted by team members,Medium,Done,2026-10-28,Programming assignment
16,Code review,Review code submitted by team members,Medium,Done,2026-10-28,Programming assignment

'''

import sqlite3

#BASE
def create_connection():
    try:
        conn = sqlite3.connect('tasks.db')
        return conn
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
        return None

def setup_database(conn):
    cursor = conn.cursor()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT DEFAULT 'Medium',
            status TEXT DEFAULT 'Pending',
            due_date TEXT,
            project_id INTEGER)'''
        )
        conn.commit()
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")

def add_task(conn, title, description, priority, status, due_date):
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO tasks (title, description, priority, status, due_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, description, priority, status, due_date))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        return None

def get_all_tasks(conn):
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT * FROM tasks ORDER BY priority, due_date''')
        return cursor.fetchall()
    except sqlite3.Error as e:
        return []

def get_tasks_by_status(conn, status):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM tasks WHERE status = ? ORDER BY priority, due_date''', (status,))
    return cursor.fetchall()

def update_task_status(conn, task_id, new_status):
    cursor = conn.cursor()
    cursor.execute('''UPDATE tasks SET status = ? WHERE id = ?''', (new_status, task_id))
    conn.commit()
    if cursor.rowcount > 0:
        return True
    return False

def delete_task(conn, task_id):
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM tasks WHERE id = ?''', (task_id,))
    conn.commit()
    if cursor.rowcount > 0:
        return True
    return False

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print(f"{'ID':<4} {'Title':<30} {'Priority':<10} {'Status':<12} {'Due Date'}")
    print(f"{'-'*3}  {'-'*28}  {'-'*8}  {'-'*10}  {'-'*10}")
    for task in tasks:
        print(f"{task[0]:<4} {task[1]:<30} {task[3]:<10} {task[4]:<12} {task[5]:<12}")

def test_delete_all(conn):
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM tasks''')
    conn.commit()
    display_tasks(get_all_tasks(conn))

#INTERMEDIATE
class TaskManager:
    def __init__(self, conn):
        try:
            self.conn = create_connection()
            self.conn.execute('''PRAGMA foreign_keys = ON''')
            self._setup_tables()
        except sqlite3.Error as e:
            self.conn = None

    def _setup_tables(self):
        cursor = self.conn.cursor()
        setup_database(self.conn)
        cursor.execute('''CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            status TEXT DEFAULT 'Active',
            due_date TEXT)'''
        )
        self.conn.commit()

    def add_project(self, name, description, due_date):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO projects (name, description, due_date)
            VALUES (?, ?, ?)
        ''', (name, description, due_date))
        self.conn.commit()
        return cursor.lastrowid

    def get_all_projects(self):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM projects ORDER BY name''')
        return cursor.fetchall()

    def add_task(self, title, description, priority, status, due_date, project_id=None):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO tasks (title, description, priority, status, due_date, project_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (title, description, priority, status, due_date, project_id))
        self.conn.commit()
        return cursor.lastrowid

    def get_project_tasks(self, project_id):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM tasks WHERE project_id = ? ORDER BY priority, due_date''', (project_id,))
        return cursor.fetchall()

    def get_tasks_with_project_name(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT t.id, t.title, t.description, t.priority, t.status, t.due_date, p.name
            FROM tasks AS t
            LEFT JOIN projects AS p ON t.project_id = p.id
            ORDER BY t.priority, t.due_date
        ''')
        return cursor.fetchall()

    def get_project_summary(self, project_id):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT status, COUNT(*) 
            FROM tasks 
            WHERE project_id = ? 
            GROUP BY status
            ''', (project_id,)
        )
        return cursor.fetchall()

    def search_tasks(self, keyword):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM tasks 
            WHERE title LIKE ? OR description LIKE ? 
            ORDER BY priority, due_date
        ''', (f'%{keyword}%', f'%{keyword}%'))
        return cursor.fetchall()

    def update_task_status(self, task_id, new_status):
        cursor = self.conn.cursor()
        cursor.execute('''UPDATE tasks SET status = ? WHERE id = ?''', (new_status, task_id))
        self.conn.commit()
        if cursor.rowcount > 0:
            return True
        return False

    #needed AI help with this function 
    def export_to_csv(self, filename):
        import csv
        tasks = self.get_tasks_with_project_name()
        row_count = 0
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Title', 'Description', 'Priority', 'Status', 'Due Date', 'Project Name'])
            for task in tasks:
                row = list(task)
                row[6] = row[6] if row[6] is not None else '(No Project)'
                writer.writerow(task)
                row_count += 1
        return row_count

    def close(self):
        self.conn.close()
    
if __name__ == '__main__':
    #BASE
    #remove docstring for BASE functionality
    '''conn = create_connection()
    cursor = conn.cursor()
    if conn == None:
        quit()
    
    setup_database(conn)
    print(f"Task added with ID: {add_task(conn, 'Finish project report', 'Complete the final report for the project', 'High', 'Pending', '2024-06-30')}")
    print(f"Task added with ID: {add_task(conn, 'Prepare presentation', 'Create slides for the upcoming presentation', 'Medium', 'Pending', '2024-07-05')}")
    print(f"Task added with ID: {add_task(conn, 'Team meeting', 'Discuss project progress with the team', 'Low', 'Pending', '2024-06-25')}")
    print(f"Task added with ID: {add_task(conn, 'Code review', 'Review code submitted by team members', 'Medium', 'Pending', '2024-06-28')}")
    print(f"Task added with ID: {add_task(conn, 'Update documentation', 'Revise and update project documentation', 'Low', 'Pending', '2024-07-10')}")
    print(f"Task added with ID: {add_task(conn, 'Client feedback', 'Incorporate feedback received from the client', 'High', 'Pending', '2024-07-01')}")

    print("\n=== Pending Tasks ===")
    display_tasks(get_all_tasks(conn))

    if update_task_status(conn, 12, 'In Progress') == True:
        print("\nTask status updated successfully.")
    else:
        print("\nTask not found or failed to update.")

    if delete_task(conn, 2) == True:
        print("\nTask deleted successfully.\n")
    else:
        print("\nTask not found or failed to delete.\n")

    #Used for base case testing of returning empty list of tasks after deleting all tasks from the database
    #test_delete_all(conn)

    conn.close()'''
    
    #INTERMEDIATE
    tm = TaskManager("tasks.db")
    if tm.conn == None:
        print("Failed to connect to database.")
        quit()
    
    proj_1 = tm.add_project("History paper", "World War I axis forces", "2026-10-15")
    proj_2 = tm.add_project("Programming assignment", "personal task manager", "2026-10-11")
    print(f"Project added with ID: {proj_1}")
    print(f"Project added with ID: {proj_2}")

    print(f"\nTask added with ID: {tm.add_task('Finish project report', 'Complete the final report for the project', 'High', 'Pending', '2026-10-30', proj_1)}")
    print(f"Task added with ID: {tm.add_task('Prepare presentation', 'Create slides for the upcoming presentation', 'Medium', 'Pending', '2026-10-05', proj_1)}")
    print(f"Task added with ID: {tm.add_task('Team meeting', 'Discuss project progress with the team', 'Low', 'Pending', '2026-10-25', proj_2)}")
    print(f"Task added with ID: {tm.add_task('Code review', 'Review code submitted by team members', 'Medium', 'Done', '2026-10-28', proj_2)}")
    print(f"Task added with ID: {tm.add_task('Update documentation', 'Review and update project documentation', 'Low', 'Pending', '2026-10-10', proj_2)}")
    print(f"Task added with ID: {tm.add_task('Client feedback', 'Incorporate feedback received from the client', 'High', 'Pending', '2026-10-01', None)}")

    print("\n=== All Tasks with Project ===")
    print(f"{'ID':<4} {'Title':<30} {'Priority':<10} {'Status':<12} {'Due Date'}")
    print(f"{'Project'}")
    print(f"{'-'*3}  {'-'*28}  {'-'*8}  {'-'*10}  {'-'*10}")
    print(f"{'-'*13}")

    tasks_with_projects = tm.get_tasks_with_project_name()
    for task in tasks_with_projects:
        t_id, title, desc, priority, status, due_date, proj_name = task
        proj_display = proj_name if proj_name else "(No Project)"
        
        # Print first line: ID, Title, Priority, Status, Due Date
        print(f"{str(t_id):<4} {title:<30} {priority:<10} {status:<12} {due_date}")
        # Print second line: Project name on its own row underneath
        print(f"{proj_display}\n")
    
    print(f"\n=== Project Summary for Project ID {proj_2} ===")
    summary = tm.get_project_summary(proj_2)
    for status_val, count_val in summary:
        print(f"Status: {status_val}, Count: {count_val}")
    
    keyword = "gibberish"
    print(f"\n=== Search Results for Keyword '{keyword}' ===")
    search_results = tm.search_tasks(keyword)
    for task in search_results:
        print(f"Task ID: {task[0]} | Title: {task[1]} | Description: {task[2]}")
    if len(search_results) == 0:
        print("No tasks found.")

    exported_rows = tm.export_to_csv("tasks_export.csv")
    print(f"\nSuccessfully exported {exported_rows} rows to 'tasks_export.csv'.")
    
    tm.close()