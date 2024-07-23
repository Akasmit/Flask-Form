import pandas as pd
from sqlalchemy import create_engine
import os
# from docx import Document
# from docx.shared import Pt
import re

def connect_to_database_alchemy():
    """Establishes a connection to the MySQL database using SQLAlchemy."""
    db_url = (
        f"mysql+mysqlconnector://"
        f"{os.getenv('DB_USER', 'tlubben')}:"
        f"{os.getenv('DB_PASSWORD', 'VizualLead21!')}@"
        f"{os.getenv('DB_HOST', 'vzleadgen.cma1wzfub9dh.us-west-2.rds.amazonaws.com')}/"
        f"{os.getenv('DB_NAME', 'vizleads')}"
    )
    engine = create_engine(db_url)
    return engine

def fetch_data(linkedin_id):
    """Fetches data from the MySQL database for the specified LinkedIn ID."""
    engine = connect_to_database_alchemy()
    query_complete = f"""
SELECT
     SUBSTRING_INDEX(SUBSTRING_INDEX(`prospects_enriched`.`personal_linkedin_url`, '/', -2), '/', 1) AS "Linkedin ID",
    `prospects_enriched`.`full_name` as "Full Name",
    `prospects_enriched`.`original_title` as "Job Title",
    `pd`.`Department`  as "Department (AI)",
    `prospects_enriched`.`company` as "Company Name",
    `prospects_enriched`.`industry` as "Linkedin Industry",
    `ind`.`industry1` as "Lvl 1 Industry (AI)",
    `ind`.`industry2` as "Lvl 2 Industry (AI)"
FROM `vizleads`.`prospects_enriched`
LEFT JOIN `vzid_companyid` `ids` ON (`vizleads`.`prospects_enriched`.`vzid` = `ids`.`vzid`)
LEFT JOIN `company_enriched_ai_industry` `ind` ON (`ind`.`company_id` = `ids`.`company_id`)
LEFT JOIN `prospects_department` `pd` ON (`vizleads`.`prospects_enriched`.`vzid` = `pd`.`vzid`)
WHERE SUBSTRING_INDEX(SUBSTRING_INDEX(`prospects_enriched`.`personal_linkedin_url`, '/', -2), '/', 1) = "{linkedin_id}"
    """
    # print(f"Executing query: {query_complete}")
    df_complete = pd.read_sql(query_complete, engine)
    print("DataFrame fetched:", df_complete)
    engine.dispose()
    return df_complete


def get_data(linkedin_id):
    df_complete = fetch_data(linkedin_id)
    # print(df_complete)
    # document = create_document(linkedin_id, df_complete)

    output_dir = "Lead Messages"
    os.makedirs(output_dir, exist_ok=True)

    # file_path = os.path.join(output_dir, f"{linkedin_id}_profile.docx")
    # document.save(file_path)
    # print(f"Output written to {file_path}")
    return df_complete

def main():
    return get_data(linkedin_id='')

# -rubyjiang



