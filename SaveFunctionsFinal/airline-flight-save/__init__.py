import json
from typing import List
import logging

import azure.functions as func


def main(events: List[func.EventHubEvent], doc: func.Out[func.Document]):
    for event in events:
        logging.info('Python EventHub trigger processed an event: %s',
                        event.get_body().decode('utf-8'))

        event_body = json.loads(event.get_body().decode('utf-8'))
        
        flight = { 
            "id": event_body["id"], 
            "airline": event_body["flight"]["airline"],
            "stops": event_body["flight"]["stops"],
            "price": event_body["flight"]["price"]
        }

        doc.set(func.Document.from_json(json.dumps(flight)))