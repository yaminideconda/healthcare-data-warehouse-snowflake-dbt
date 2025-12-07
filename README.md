# 🏥 Healthcare Data Warehouse (Snowflake + dbt)

This project builds a modern healthcare data warehouse using **Snowflake** for storage and **dbt (Data Build Tool)** for data transformation and modeling.  

It shows how to take raw healthcare data, load it into Snowflake, model it into clean, analytics-ready tables, and prepare it for dashboards in tools like Power BI or Tableau.

---

## 🎯 Objectives

- Design a cloud data warehouse in **Snowflake**.
- Transform raw healthcare data into structured, analytics-ready layers using **dbt**.
- Use modular SQL models for maintainable and scalable transformations.
- Add tests and documentation with dbt’s built-in features.
- Prepare curated tables for BI and reporting.

---

## 🏗️ Data Architecture

| Layer   | Schema                    | Description                                                                 |
|--------|---------------------------|-----------------------------------------------------------------------------|
| Raw    | `HEALTHCARE_DB.RAW`       | Stores raw ingested CSV data (patients, claims, providers, conditions).    |
| Staging| `HEALTHCARE_DB.TRANSFORMED` | Cleans, standardizes and formats raw tables using dbt models.              |
| Marts  | `HEALTHCARE_DB.MARTS`     | (Planned) Business-friendly tables for analytics and reporting.            |

---

## 📊 Example KPIs

- Total patients by city and state  
- Average claim amount per provider  
- Claim approval rate  
- Top diagnosed conditions by severity  
- Patient demographics by age and gender  

These KPIs can be surfaced through BI tools using the curated tables in Snowflake.

---

## 🧩 Key dbt Models

| Model             | Description                                              |
|------------------|----------------------------------------------------------|
| `stg_claims.sql`   | Cleans and standardizes claim data from the RAW layer.  |
| `stg_patients.sql` | Formats and enriches patient details.                   |
| `stg_providers.sql`| Normalizes provider data for joins and reporting.       |
| `schema.yml`       | Defines tests and documentation for dbt models.         |

Example `stg_claims.sql`:

```sql
SELECT
    CLAIM_ID,
    PATIENT_ID,
    PROVIDER_ID,
    AMOUNT,
    CLAIM_DATE,
    UPPER(STATUS) AS CLAIM_STATUS
FROM "HEALTHCARE_DB"."RAW"."CLAIMS";
🧰 Tools and Technologies
Snowflake – Cloud data warehouse

dbt (Data Build Tool) – Data modeling, testing and documentation

Python – Virtual environment and dependency management

Git & GitHub – Version control

Power BI / Tableau (optional) – Dashboard and reporting layer

🗂️ Project Structure

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
│   │   │   ├── stg_claims.sql
│   │   │   ├── stg_patients.sql
│   │   │   └── stg_providers.sql
│   │   └── schema.yml
│   ├── macros/
│   ├── seeds/
│   └── dbt_project.yml
│
└── scripts/                      # Optional setup / helper scripts
⚙️ Getting Started
1. Clone the repository

git clone https://github.com/yaminideconda/healthcare-data-warehouse-snowflake-dbt.git
cd healthcare-data-warehouse-snowflake-dbt
2. Create and activate a virtual environment

python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
3. Install dbt for Snowflake

pip install dbt-snowflake
4. Configure Snowflake connection
Create or edit your profiles.yml file, typically located at:

Windows: C:\Users\<your-username>\.dbt\profiles.yml

Mac / Linux: /Users/<your-username>/.dbt/profiles.yml

Example profile:

healthcare_project:
  outputs:
    dev:
      type: snowflake
      account: <YOUR_ACCOUNT>
      user: <YOUR_USERNAME>
      password: <YOUR_PASSWORD>
      role: <YOUR_ROLE>
      warehouse: COMPUTE_WH
      database: HEALTHCARE_DB
      schema: TRANSFORMED
  target: dev
Replace the placeholders with your own Snowflake credentials.

🚀 Running dbt
From the healthcare_project directory:

dbt debug          # Test connection to Snowflake
dbt run            # Build all dbt models
dbt test           # Run tests defined in schema.yml
dbt docs generate  # Generate documentation site
dbt docs serve     # Serve docs locally in your browser
After running dbt run, you should see models created in Snowflake under:

HEALTHCARE_DB → TRANSFORMED → views / tables

💡 Future Enhancements
Add incremental models for large datasets

Build dedicated marts for claims, patients, and provider analytics

Integrate a Power BI or Tableau dashboard for end-to-end reporting

Add more data quality tests and set up CI/CD with GitHub Actions

🧾 Author
Yamini Deconda
Data Engineer · Snowflake Developer · dbt Practitioner
