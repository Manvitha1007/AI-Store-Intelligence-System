import json
from datetime import datetime

events = [
    {
        "timestamp": datetime.now().isoformat(),
        "event_type": "customer_entered",
        "visitor_id": 1,
        "camera": "CAM3"
    },
    {
        "timestamp": datetime.now().isoformat(),
        "event_type": "zone_entered",
        "visitor_id": 1,
        "camera": "CAM1",
        "zone": "Cosmetics"
    },
    {
        "timestamp": datetime.now().isoformat(),
        "event_type": "billing_started",
        "visitor_id": 1,
        "camera": "CAM5"
    }
]

with open("events.jsonl", "w") as f:
    for event in events:
        f.write(json.dumps(event) + "\n")

print("Event log created")
