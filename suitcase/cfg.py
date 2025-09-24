import json

from pathlib import Path

def init():
        path = Path("config.json")
        if not path.exists():
                path.write_text(json.dump("{\"filters\": [\".kml\", \".txt\", \".zip\"]}"))

def load():
        with open("config.json", "r") as rf: 
                return json.load(rf)