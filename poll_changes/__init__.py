import logging
import azure.functions as func

def main(changes: str) -> None:
    logging.warning("⚡ Function was triggered successfully")
