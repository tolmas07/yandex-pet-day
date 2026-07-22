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

# Get user messages from the Figma session and the virus session
for sid in ['ses_0755d8a69ffeiflGlWdQIQhx7y', 'ses_0bbf8a3bdffeagJ3wfqVtBF2Rm', 'ses_0bbee5cb2ffe3RUMUgegcZhkhl']:
    print(f"\n=== ALL MESSAGES: {sid} ===")
    rows = query(f"""
        SELECT m.id, json_extract(m.data, '$.role') as role, 
               substr(m.data, 1, 200) as msg_preview
        FROM message m
        WHERE m.session_id = '{sid}'
        ORDER BY m.time_created
        LIMIT 15
    """)
    for r in rows:
        print(f"  [{r['role']}] {r['msg_preview'][:150]}")

# Look for assistant tool calls that created/modified files in key sessions
print("\n=== FILE WRITES IN PORTFOLIO SESSION ===")
rows = query(f"""
    SELECT json_extract(p.data, '$.tool') as tool, 
           substr(json_extract(json_extract(p.data, '$.state'), '$.input'), 1, 300) as input_preview
    FROM part p
    JOIN message m ON p.message_id = m.id
    WHERE m.session_id = 'ses_0ec67949affePEX7jfFaXZ9rRS'
      AND json_extract(p.data, '$.type') = 'tool'
      AND json_extract(p.data, '$.tool') IN ('write', 'edit', 'bash')
    ORDER BY m.time_created
    LIMIT 20
""")
for r in rows:
    print(f"  [{r['tool']}] {r['input_preview'][:200]}")

# Check for user preferences/rules across sessions
print("\n=== SEARCHING FOR USER RULES/PREFERENCES ===")
for keyword in ['всегда', 'никогда', 'запомни', 'правило', 'не надо', 'не нужно', 'просто', 'только']:
    rows = query(f"""
        SELECT m.session_id, substr(json_extract(p.data, '$.text'), 1, 200) as text
        FROM part p
        JOIN message m ON p.message_id = m.id
        WHERE json_extract(m.data, '$.role') = 'user'
          AND json_extract(p.data, '$.type') = 'text'
          AND json_extract(p.data, '$.text') LIKE '%{keyword}%'
        LIMIT 3
    """)
    if rows:
        print(f"\n  Keyword '{keyword}':")
        for r in rows:
            print(f"    [{r['session_id'][:15]}] {r['text'][:150]}")
