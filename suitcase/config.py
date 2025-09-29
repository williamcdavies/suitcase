import json

from pathlib import Path

CONFIG_JSON     = Path(__file__).parent.parent / "config.json"

def init():
        obj     = {
                        "filters": [
                                ".kml", 
                                ".txt", 
                                ".zip"
                        ]
                }
        data    = json.dumps(obj, indent=8)
        
        CONFIG_JSON.write_text(data)

def load():
        if not CONFIG_JSON.exists():
                init()
        
        with open(CONFIG_JSON, encoding="utf-8") as rf: 
                return json.load(rf)