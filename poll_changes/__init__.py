import json
import logging
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="mytriggerfn")
@app.sql_trigger(arg_name="todo",
                        table_name="Sales",
                        connection_string_setting="SQLCONNSTR_SQL_CONNECTION_STRING")
def todo_trigger(todo: str) -> None:
    logging.info("SQL Changes: %s", json.loads(todo))