from binance.client import Client
import os
from dotenv import load_dotenv
import logging
import time

load_dotenv()

def get_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_SECRET_KEY")

    if not api_key or not api_secret:
        raise ValueError("API key or Secret not found")

    client = Client(api_key, api_secret, testnet=True)

    # Base URL
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    # Sync time with server
    server_time = client.get_server_time()
    client.timestamp_offset = server_time["serverTime"] - int(time.time() * 1000)

    logging.info("Client initialized successfully")
    return client