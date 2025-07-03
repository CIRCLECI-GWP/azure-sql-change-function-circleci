import logging
import traceback
import azure.functions as func

def main(changes: func.SqlRowList) -> None:
    try:
        logging.info(f"[SQL Trigger] Function called. Detected {len(changes)} change(s) in Sales table.")

        for row in changes:
            try:
                logging.debug(f"Row keys: {row.keys()}")
                logging.debug(f"Full row data: {row}")

                sale_id = row.get("Id") or row.get("ID")
                car_id = row.get("CarId") or row.get("CARID")
                salesman_id = row.get("SalesmanId") or row.get("SALESMANID")
                sale_date = row.get("SaleDate") or row.get("SALEDATE")

                logging.info(f"✔ Change: SaleID={sale_id}, CarID={car_id}, SalesmanID={salesman_id}, SaleDate={sale_date}")

            except Exception as row_error:
                logging.error("❌ Error while processing an individual row.")
                logging.error(f"Exception: {str(row_error)}")
                logging.error(traceback.format_exc())

    except Exception as e:
        logging.error("🔥 An error occurred in the SQL trigger function.")
        logging.error(f"Exception: {str(e)}")
        logging.error("Stack trace:\n" + traceback.format_exc())
