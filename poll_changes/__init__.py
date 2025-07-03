import json
import logging
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="mytriggerfn")
@app.sql_trigger(
    arg_name="todo",
    table_name="Sales",
    connection_string_setting="SQL_CONNECTION_STRING"
)
def todo_trigger(todo: str) -> None:
    try:
        logging.info("⚡ SQL Trigger Fired")
        logging.debug(f"Raw payload: {todo}")

        changes = json.loads(todo)
        for row in changes:
            logging.info(f"✔ Change: SaleID={row.get('Id')}, CarID={row.get('CarId')}, SalesmanID={row.get('SalesmanId')}, SaleDate={row.get('SaleDate')}")
    except Exception as e:
        logging.error("❌ Error while processing SQL changes")
        logging.error(str(e))
