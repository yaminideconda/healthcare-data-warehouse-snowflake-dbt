# Healthcare Data Warehouse – Snowflake & dbt Project

This project demonstrates how to build a **modern data warehouse** on **Snowflake** using **dbt (Data Build Tool)** for data transformation, modeling, and documentation.  
It follows a layered architecture with separate schemas for raw, transformed, and analytics-ready data.

---

## 📁 Project Structure

healthcare-data-warehouse-snowflake-dbt/
│
├── data/ # Raw CSV files (patients, claims, providers, conditions)
│ ├── patients.csv
│ ├── claims.csv
│ ├── providers.csv
│ └── conditions.csv
│
├── healthcare_project/ # Main dbt project
│ ├── models/ # SQL models for staging & transformation
│ │ ├── staging/
│ │ │ └── stg_claims.sql
│ │ ├── marts/
│ │ └── schema.yml
│ ├── dbt_project.yml # dbt project configuration
│ └── README.md
│
├── scripts/ # Optional helper scripts (SQL, Python)
├── venv/ # Python virtual environment (ignored in Git)
└── .gitignore # Files & folders excluded from version control

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yaminideconda/healthcare-data-warehouse-snowflake-dbt.git
cd healthcare-data-warehouse-snowflake-dbt
2. Create a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
3. Install dbt for Snowflake
bash
Copy code
pip install dbt-snowflake
4. Configure Snowflake Connection
Edit (or create) a file named profiles.yml under:

makefile
Copy code
C:\Users\<your-username>\.dbt\profiles.yml
Example configuration:

yaml
Copy code
healthcare_project:
  outputs:
    dev:
      type: snowflake
      account: KSOAIUG-TG79516
      user: YAMINI
      password: <your_password>
      role: ACCOUNTADMIN
      warehouse: COMPUTE_WH
      database: HEALTHCARE_DB
      schema: TRANSFORMED
  target: dev
🧠 How It Works
Raw Layer (RAW schema):
Contains source tables like PATIENTS, CLAIMS, PROVIDERS, and CONDITIONS.

Staging Layer (TRANSFORMED schema):
dbt models clean and standardize raw data.
Example:

sql
Copy code
SELECT
    CLAIM_ID,
    PATIENT_ID,
    PROVIDER_ID,
    AMOUNT,
    CLAIM_DATE,
    UPPER(STATUS) AS CLAIM_STATUS
FROM "HEALTHCARE_DB"."RAW"."CLAIMS";
Analytics Layer (MARTS schema):
Future models can join across staging tables to produce analytics-ready datasets.

🚀 Run the Project
bash
Copy code
dbt debug        # Verify connection
dbt run          # Execute models and create views/tables in Snowflake
dbt test         # Run data quality tests
dbt docs serve   # Launch interactive dbt documentation site
Then open the local URL shown in the terminal (usually http://127.0.0.1:8080).

✅ Example Output
After running dbt run, you’ll see new views in Snowflake under:

nginx
Copy code
HEALTHCARE_DB → TRANSFORMED → Tables/Views
Example: STG_CLAIMS

🧩 Tools Used
Snowflake – Cloud Data Warehouse

dbt (Data Build Tool) – Data transformation, lineage, and testing

Python – Virtual environment & dependency management

Git & GitHub – Version control and project hosting

📄 License
This project is for educational and demonstration purposes.
Feel free to fork and customize for your own data warehouse projects.
