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

# Find sessions with actual user messages (non-checkpoint-writer children)
# Filter to sessions with directory containing "Desktop" (user's main workspace)
sessions = query("""
    SELECT id, title, directory, time_created 
    FROM session 
    WHERE parent_id IS NULL 
    ORDER BY time_created DESC 
    LIMIT 15
""")

print("=== NON-CHILD SESSIONS ===")
for s in sessions:
    ts = s['time_created'] / 1000
    from datetime import datetime
    dt = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M')
    print(f"  {s['id']} | {dt} | {s['title'][:60]} | {s['directory']}")

# For each substantive session, get user messages to find rules/preferences
target_sessions = [
    'ses_0755d8a69ffeiflGlWdQIQhx7y',  # Figma test task
    'ses_0bbee5cb2ffe3RUMUgegcZhkhl',  # Red Alert 2
    'ses_0ec67949affePEX7jfFaXZ9rRS',  # Portfolio site
    'ses_0efd51ea9ffeuYENvPBY4QZCVf',  # Manor Lords
    'ses_0f0adcc9bffemX3MKKmqXh8eHp',  # RuView install
]

for sid in target_sessions:
    print(f"\n=== USER MESSAGES: {sid} ===")
    rows = query(f"""
        SELECT m.id, json_extract(m.data, '$.role') as role, p.data as part_data
        FROM message m
        JOIN part p ON p.message_id = m.id
        WHERE m.session_id = '{sid}'
          AND json_extract(m.data, '$.role') = 'user'
        ORDER BY m.time_created
        LIMIT 10
    """)
    for r in rows:
        try:
            pd = json.loads(r['part_data'])
            if pd.get('type') == 'text':
                text = pd.get('text', '')[:200]
                print(f"  [{r['id'][:20]}] {text}")
        except:
            pass
