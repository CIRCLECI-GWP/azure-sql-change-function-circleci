import logging
import traceback
import azure.functions as func

def main(changes: func.SqlRowList) -> None:
    try:
        logging.info(f"[Sales] {len(changes)} change(s) detected.")
        for row in changes:
            logging.info(f"Row keys: {row.keys()}")
            logging.info(f"Full row data: {row}")

            sale_id = row.get("Id")  # This might be wrong if the field is actually "ID" or "id"
            sale_date = row.get("SaleDate")

            logging.info(f"SaleID={sale_id}, SaleDate={sale_date}")

    except Exception as e:
        logging.error("❌ An error occurred while processing SQL changes.")
        logging.error(f"Exception: {str(e)}")
        logging.error("Stack Trace:\n" + traceback.format_exc())
