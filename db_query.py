import sqlite3
import json

DB_PATH = r'C:\Users\Tolmas\.local\share\mimocode\mimocode.db'

def query(sql):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return rows

# 1. List tables
print("=== TABLES ===")
for r in query("SELECT name FROM sqlite_master WHERE type='table'"):
    print(r[0])

# 2. Schema for key tables
for table in ['session', 'message', 'part', 'task', 'task_event']:
    print(f"\n=== SCHEMA: {table} ===")
    try:
        for r in query(f"PRAGMA table_info({table})"):
            print(f"  {r[1]} ({r[2]})")
    except:
        print("  (table not found)")

# 3. Recent sessions
print("\n=== RECENT SESSIONS (last 20) ===")
try:
    for r in query("SELECT * FROM session ORDER BY rowid DESC LIMIT 20"):
        print(dict(r))
except Exception as e:
    print(f"Error: {e}")
