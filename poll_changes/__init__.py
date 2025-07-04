import json
import logging

def main(changes: str) -> None:
    try:
        logging.info("SQL Trigger fired!")
        logging.info(f"Raw change payload: {changes}")

        rows = json.loads(changes)
        logging.info(f"🔄 Number of changes: {len(rows)}")

        for row in rows:
            op = row.get("Operation")
            item = row.get("Item", {})

            sale_id = item.get("Id")
            car_id = item.get("CarId")
            salesman_id = item.get("SalesmanId")
            sale_date = item.get("SaleDate")

            # Translate operation type
            operation_map = {0: "INSERT", 1: "UPDATE", 2: "DELETE"}
            op_type = operation_map.get(op, f"Unknown ({op})")

            logging.info(f"{op_type} -> SaleID={sale_id}, CarID={car_id}, SalesmanID={salesman_id}, SaleDate={sale_date}")

    except Exception as e:
        logging.error("An error occurred while processing SQL changes.")
        logging.error(f"Exception: {str(e)}", exc_info=True)