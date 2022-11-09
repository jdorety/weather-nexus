from dotenv import load_dotenv
from os import environ
from helpers import make_tx, send_readings

load_dotenv()

key = environ.get('api-key')
ledger_url = environ.get('ledger-url')

tx = make_tx(14.82, 22.0, 1.422)

response = send_readings(ledger_url, key, tx)
print(response)