import pandas as pd
import snowflake.connector

# --- STEP 1: Connect to Snowflake ---
conn = snowflake.connector.connect(
    user="YAMINI",
    password="Akulmini@120713",
    account="KSOAIUG-TG79516",
    warehouse="COMPUTE_WH",
    database="HEALTHCARE_DB",
    schema="RAW",
    role="ACCOUNTADMIN"
)

cursor = conn.cursor()

# --- STEP 2: Function to load a CSV into a Snowflake table ---
def load_csv_to_snowflake(file_path, table_name):
    print(f"\nLoading {file_path} into {table_name}...")
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        values = tuple(row)
        placeholders = ', '.join(['%s'] * len(row))
        columns = ', '.join(df.columns)
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(query, values)
    conn.commit()
    print(f"✅ Successfully loaded {len(df)} records into {table_name}")

# --- STEP 3: Load each CSV into the correct table ---
load_csv_to_snowflake('data/patients.csv', 'RAW.PATIENTS')
load_csv_to_snowflake('data/providers.csv', 'RAW.PROVIDERS')
load_csv_to_snowflake('data/claims.csv', 'RAW.CLAIMS')
load_csv_to_snowflake('data/conditions.csv', 'RAW.CONDITIONS')

# --- STEP 4: Verify the data ---
cursor.execute("SELECT COUNT(*) FROM RAW.PATIENTS")
print("Total Patients:", cursor.fetchone()[0])

cursor.close()
conn.close()
print("\n✅ All done! Data successfully loaded into Snowflake.")
