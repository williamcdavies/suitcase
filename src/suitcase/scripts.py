from pathlib import Path


SCRIPTS_PATH = Path(__file__).parent / "scripts"


def read(
        script: str,
        /
        ) -> str:
        """scripts.read
        """
        
        if not (SCRIPTS_PATH / script).exists():
                raise FileNotFoundError("Resolution of symlink: Failed with path does not exist")

        return (SCRIPTS_PATH / script).read_text(encoding="utf-8")