import logging
import azure.functions as func

def main(changes: func.SqlRowList) -> None:
    logging.info(f"[Sales] {len(changes)} change(s) detected.")
    for row in changes:
        sale_id = row.get("Id")
        sale_date = row.get("SaleDate")
        logging.info(f"SaleID={sale_id}, SaleDate={sale_date}")