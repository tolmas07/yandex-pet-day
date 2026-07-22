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

# Get assistant text responses from Figma session
print("=== ASSISTANT TEXT: ses_0755d8a69ffeiflGlWdQIQhx7y ===")
rows = query(f"""
    SELECT substr(json_extract(p.data, '$.text'), 1, 500) as text
    FROM part p
    JOIN message m ON p.message_id = m.id
    WHERE m.session_id = 'ses_0755d8a69ffeiflGlWdQIQhx7y'
      AND json_extract(m.data, '$.role') = 'assistant'
      AND json_extract(p.data, '$.type') = 'text'
    ORDER BY m.time_created
""")
for r in rows:
    if r['text']:
        print(f"  {r['text'][:300]}")
        print()

# Get assistant text from virus session
print("\n=== ASSISTANT TEXT: ses_0bbf8a3bdffeagJ3wfqVtBF2Rm ===")
rows = query(f"""
    SELECT substr(json_extract(p.data, '$.text'), 1, 500) as text
    FROM part p
    JOIN message m ON p.message_id = m.id
    WHERE m.session_id = 'ses_0bbf8a3bdffeagJ3wfqVtBF2Rm'
      AND json_extract(m.data, '$.role') = 'assistant'
      AND json_extract(p.data, '$.type') = 'text'
    ORDER BY m.time_created
""")
for r in rows:
    if r['text']:
        print(f"  {r['text'][:300]}")
        print()

# Get assistant text from Red Alert 2 session
print("\n=== ASSISTANT TEXT: ses_0bbee5cb2ffe3RUMUgegcZhkhl ===")
rows = query(f"""
    SELECT substr(json_extract(p.data, '$.text'), 1, 500) as text
    FROM part p
    JOIN message m ON p.message_id = m.id
    WHERE m.session_id = 'ses_0bbee5cb2ffe3RUMUgegcZhkhl'
      AND json_extract(m.data, '$.role') = 'assistant'
      AND json_extract(p.data, '$.type') = 'text'
    ORDER BY m.time_created
""")
for r in rows:
    if r['text']:
        print(f"  {r['text'][:300]}")
        print()

# Check what files exist in the test directory
print("\n=== FILES IN TEST DIR ===")
import os
test_dir = r'C:\Users\Tolmas\Desktop\test'
for f in os.listdir(test_dir):
    fp = os.path.join(test_dir, f)
    size = os.path.getsize(fp) if os.path.isfile(fp) else 0
    print(f"  {f} ({size} bytes)")
