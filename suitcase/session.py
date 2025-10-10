import aiofiles
import aiohttp
import asyncio

from collections.abc import Iterable
from pathlib         import Path
from platformdirs    import user_downloads_path
from urllib.parse    import urlparse

_USER_DOWNLOADS_PATH = user_downloads_path()

def _download_verbose_print(
                filename: str,
                scheme: str,
                netloc: str,
                path: str,
                content: str,
                /
        ):
        """session._download_vprint

        Parameters
        ----------
        """

        print(f"Download of {filename} from {scheme}://{netloc} to {path}: {content}")

async def _download(
                url: str,
                path: Path,
                session: aiohttp.ClientSession,
                /,
                verbose: bool=False
        ):
        """session._download

        Parameters
        ----------
        """
        
        url_parse_tree = urlparse(url)
        filename       = url_parse_tree.path.split("/")[-1]
        path           = path / filename

        try:
                async with session.get(url) as response:
                        response.raise_for_status()
                        
                        async with aiofiles.open(path, "wb") as wbf:
                                async for chunk in response.content.iter_any():
                                        await wbf.write(chunk)
                
                if verbose:
                        _download_verbose_print(
                                filename, 
                                url_parse_tree.scheme, 
                                url_parse_tree.netloc, 
                                str(path), 
                                "Success"
                        )
                
                return path
        
        except aiohttp.ClientResponseError as e:
                if verbose:
                        _download_verbose_print(
                                filename, 
                                url_parse_tree.scheme, 
                                url_parse_tree.netloc, 
                                str(path), 
                                f"Failed with {e}"
                        )
                
                return None

async def download(
                urls: Iterable[str],
                path: Path | None=None,
                /,
                verbose: bool=False
        ):
        """session.download

        Parameters
        ----------
        """

        if path is None:
                path = _USER_DOWNLOADS_PATH

                if not path.exists():
                        raise ValueError("Resolution of symlink: Failed with path does not exist")
        else:  
                path.mkdir(parents=True, exist_ok=True)
                
        async with aiohttp.ClientSession() as session:
                return await asyncio.gather(*(_download(url, path, session, verbose=verbose) for url in urls))