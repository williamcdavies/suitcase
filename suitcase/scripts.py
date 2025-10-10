from pathlib import Path

SCRIPTS = Path(__file__).parent / "scripts"

def read(
                script: str,
                /
        ) -> str:
        """scripts.read
        """
        
        if not (SCRIPTS / script).exists():
                raise FileNotFoundError("Resolution of symlink: Failed with path does not exist")

        return (SCRIPTS / script).read_text(encoding="utf-8")