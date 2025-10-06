from pathlib import Path

SCRIPTS = Path(__file__).parent / "scripts"

def read(script: str) -> str:
        """scripts.read
        
        """
        
        if not (SCRIPTS / script).exists():
                raise FileNotFoundError(f"Script '{script}' not found in {SCRIPTS}")

        return (SCRIPTS / script).read_text(encoding="utf-8")