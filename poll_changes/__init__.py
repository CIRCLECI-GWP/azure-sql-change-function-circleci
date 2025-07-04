import json
import logging

def main(changes: str) -> None:
    try:
        logging.info("⚡ SQL Trigger fired!")
        logging.debug(f"Raw data: {changes}")
        
        rows = json.loads(changes)
        for row in rows:
            logging.info(row)
            logging.info(f"✅ SaleID={row.get('Id')}, CarID={row.get('CarId')}")
    except Exception as e:
        logging.error("❌ Error processing SQL changes")
        logging.error(str(e))
