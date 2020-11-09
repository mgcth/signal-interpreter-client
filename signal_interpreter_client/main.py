# main.py Lec1 Afzalas-2
import argparse
from server_communication_handler import post_message


signal = "signal"
parser = argparse.ArgumentParser()   # object
parser.add_argument("--signal", required=True, help='python main.py --signal "your message"')
args = parser.parse_args()

payload = {
    signal: args.signal
}

post_message("http://127.0.0.1:5000", payload)
