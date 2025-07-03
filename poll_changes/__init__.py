import logging
import azure.functions as func

def main(changes: func.SqlRowList) -> None:
    logging.warning("⚡ Function was triggered successfully")
