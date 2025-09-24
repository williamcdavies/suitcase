import json

from pathlib import Path

def init():
        p = Path("config.json")
        if not p.exists():
                p.write_text(json.dump("{\"filters\": [\".kml\", \".txt\", \".zip\"]}"))

def load():
        with open("config.json", "r") as rf: 
                return json.load(rf)