import json


from pathlib import Path


CONFIG_PATH = Path(__file__).parent / "config"
CONFIG      = CONFIG_PATH / "config.json"


def init():
        """config.init
        """

        CONFIG.write_text(
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

def load() -> dict[str, list[str]]:
        """config.load
        """

        if not CONFIG.exists():
                init()
        
        with open(CONFIG, encoding="utf-8") as rf: 
                return json.load(rf)