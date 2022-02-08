import json
from typing import List
import logging

import azure.functions as func


def main(events: List[func.EventHubEvent], doc: func.Out[func.Document]):
    for event in events:
        logging.info('Python EventHub trigger processed an event: %s',
                        event.get_body().decode('utf-8'))

        event_body = json.loads(event.get_body().decode('utf-8'))
        
        customer = { 
            "customer_name": event_body["customer_name"], 
            "phoneNumber": event_body["phoneNumber"],
            "city": event_body["city"],
            "country": event_body["country"],
        }

        doc.set(func.Document.from_json(json.dumps(customer)))