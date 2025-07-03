import logging
import json
import azure.functions as func

def main(changes: func.SqlRowList) -> None:
    try:
        logging.info(f"✅ SQL Trigger fired: {len(changes)} row(s) detected.")
        for row in changes:
            logging.info(f"Change row: {row}")
    except Exception as e:
        logging.error(f"❌ Error processing SQL changes: {str(e)}")
