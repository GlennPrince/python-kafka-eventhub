import json
from typing import List
import logging

import azure.functions as func


def main(events: List[func.EventHubEvent], doc: func.Out[func.Document]):
    for event in events:
        logging.info('Python EventHub trigger processed an event: %s',
                        event.get_body().decode('utf-8'))

        event_body = json.loads(event.get_body().decode('utf-8'))
        
        origin = { 
            "id": event_body["id"], 
            "airport": event_body["flight"]["origin"]["airport"],
            "iata": event_body["flight"]["origin"]["iata"],
            "icao": event_body["flight"]["origin"]["icao"],
            "city": event_body["flight"]["origin"]["city"],
            "state": event_body["flight"]["origin"]["state"],
            "country": event_body["flight"]["origin"]["country"],
        }

        doc.set(func.Document.from_json(json.dumps(origin)))