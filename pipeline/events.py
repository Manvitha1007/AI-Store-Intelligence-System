import json

event = {
    "event_type": "customer_entered",
    "camera": "CAM3",
    "visitor_count": 71
}

with open("events.json", "w") as f:
    json.dump(event, f, indent=4)

print("Event file created")