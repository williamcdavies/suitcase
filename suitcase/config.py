import json

from pathlib import Path
from typing  import Any

CONFIG_JSON = Path(__file__).parent.parent / "config.json"

def init() -> None:    
        """config.init
        """

        CONFIG_JSON.write_text(
                json.dumps(
                        {
                                "filters": [
                                        ".kml", 
                                        ".txt", 
                                        ".zip"
                                ]
                        }, 
                        indent=8
                )
        )

def load() -> Any:
        """config.load
        """

        if not CONFIG_JSON.exists():
                init()
        
        with open(CONFIG_JSON, encoding="utf-8") as rf: 
                return json.load(rf)