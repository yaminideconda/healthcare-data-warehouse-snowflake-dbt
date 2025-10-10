# 🏥 Healthcare Data Warehouse – Snowflake & dbt Project

This project builds a **modern healthcare data warehouse** using **Snowflake** for storage and **dbt (Data Build Tool)** for data transformation and modeling.  
It demonstrates how to design a scalable architecture that integrates raw healthcare data, transforms it into clean, analytics-ready datasets, and supports data visualization and analysis.

---

## 🎯 Objectives

- Design a cloud-based data warehouse on Snowflake.  
- Transform raw healthcare data into structured, analytics-ready layers using dbt.  
- Implement modular SQL models for better maintainability and scalability.  
- Automate documentation and testing using dbt’s built-in features.  
- Prepare data for visualization in BI tools such as Power BI or Tableau.

---

## 📊 Data Layers (Architecture)

| Layer | Schema | Description |
|-------|---------|-------------|
| Raw | `HEALTHCARE_DB.RAW` | Stores raw ingested CSV data (Patients, Claims, Providers, Conditions). |
| Staging | `HEALTHCARE_DB.TRANSFORMED` | Cleans, standardizes, and formats raw tables using dbt models. |
| Marts | `HEALTHCARE_DB.MARTS` | (Future enhancement) Combines staging data for analytics and reporting. |

---

## 📈 Example KPIs

- Total Patients by City / State  
- Average Claim Amount per Provider  
- Claim Approval Rate (%)  
- Top Diagnosed Conditions by Severity  
- Patient Demographics (Age, Gender)  

---

## 🧩 Key dbt Models

| Model | Description |
|--------|--------------|
| `stg_claims.sql` | Cleans and standardizes claim data from the RAW layer. |
| `stg_patients.sql` | Formats and enriches patient details. |
| `stg_providers.sql` | Normalizes provider data for joins. |
| `schema.yml` | Defines documentation and testing for dbt models. |

Example `stg_claims.sql` model:
```sql
SELECT
    CLAIM_ID,
    PATIENT_ID,
    PROVIDER_ID,
    AMOUNT,
    CLAIM_DATE,
    UPPER(STATUS) AS CLAIM_STATUS
FROM "HEALTHCARE_DB"."RAW"."CLAIMS";
🧰 Tools & Technologies
Snowflake – Cloud Data Warehouse

dbt (Data Build Tool) – Data modeling, testing, and documentation

Python (venv) – Virtual environment for dependency management

Git & GitHub – Version control and collaboration

Power BI / Tableau (optional) – Dashboard visualization

⚙️ Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/yaminideconda/healthcare-data-warehouse-snowflake-dbt.git
cd healthcare-data-warehouse-snowflake-dbt
2. Create and Activate a Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate      # (Windows)
# OR
source venv/bin/activate   # (Mac/Linux)
3. Install dbt for Snowflake
bash
Copy code
pip install dbt-snowflake
4. Configure Snowflake Connection
Create or edit your profiles.yml file located at:

makefile
Copy code
C:\Users\<your-username>\.dbt\profiles.yml
Example:

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
🚀 Run dbt Commands
bash
Copy code
dbt debug        # Test connection to Snowflake
dbt run          # Build all dbt models
dbt test         # Run tests defined in schema.yml
dbt docs generate
dbt docs serve   # Launch interactive documentation in your browser
After running, you’ll see models in Snowflake under:

nginx
Copy code
HEALTHCARE_DB → TRANSFORMED → Views
🗂️ File Structure
graphql
Copy code
healthcare-data-warehouse-snowflake-dbt/
│
├── data/                         # Raw CSV data files
│   ├── claims.csv
│   ├── patients.csv
│   ├── providers.csv
│   └── conditions.csv
│
├── healthcare_project/           # Main dbt project
│   ├── models/
│   │   ├── staging/
│   │   │   └── stg_claims.sql
│   │   └── schema.yml
│   ├── macros/
│   ├── seeds/
│   └── dbt_project.yml
│
└── scripts/                      # Optional setup scripts
💡 Future Enhancements
Add incremental models for handling large data loads.

Create data marts for Claims, Patients, and Provider analytics.

Integrate Power BI dashboard for end-to-end reporting.

Add data quality tests and CI/CD automation using GitHub Actions.

🧾 Author
Yamini Deconda
Data Engineer | Snowflake Developer | dbt Practitioner
