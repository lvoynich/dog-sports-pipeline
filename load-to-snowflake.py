import snowflake.connector
import pandas as pd
from cryptography.hazmat.primitives import serialization

# 1. Load and decrypt your private key file
with open("/Users/lanavoynich/desktop/projects/dog-sports-pipeline/rsa_key.p8", "rb") as key_file:
    p_key = serialization.load_pem_private_key(
        key_file.read(),
        password=b"runtyjake" # Put a 'b' before string for bytes
    )

pkb = p_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# 2. Establish secure connection using the key pair
ctx = snowflake.connector.connect(
    user='lvoynich',
    account='IWDJGWI-JD63133', # e.g., 'yv21543.us-east-1'
    private_key=pkb,
    warehouse='DOG_SPORTS_WH',
    database='DOG_SPORTS_DB',
    schema='RAW'
)
cs = ctx.cursor()

# 3. Create your raw data rows (Mock trial entries)
data = {
    'trial_id':[1, 2, 3],
    'dog_name': ['Ranger', 'Ranger', 'Bella'],
    'sport_type': ['Agility', 'Agility', 'Scent Work'],
    'class_level': ['Novice', 'Novice', 'Novice'],
    'score': [100.00, 85.50, 95.00],
    'is_qualified': [True, False, True],
    'entry_fee_usd': [35.00, 35.00, 25.00],
    'trial_date': ['2026-08-20', '2026-08-27', '2026-08-29']
}
df = pd.DataFrame(data)

# 4. Bulk insert rows into your Snowflake raw schema
rows = [tuple(x) for x in df.to_numpy()]
insert_query = """
    INSERT INTO dog_sports_db.raw.trial_logs 
    (trial_id, dog_name, sport_type, class_level, score, is_qualified, entry_fee_usd, trial_date)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
cs.executemany(insert_query, rows)

ctx.commit()
cs.close()
ctx.close()
print("🎉 Success! 3 rows successfully streamed to Snowflake RAW.trial_logs.")
