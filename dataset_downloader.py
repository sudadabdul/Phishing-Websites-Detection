"""Download dataset from the web and save it to the local disk."""
import asyncio
import logging
import zipfile
from functools import lru_cache
from pathlib import Path

import aiohttp

from utils import measure, async_measure, arff_to_csv

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
log_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(format=log_format)
logger.addHandler(logging.StreamHandler())

DATA_DIR = Path(__file__).parent / "data"
RAW_DATA_DIR = DATA_DIR / "raw"

@async_measure
@lru_cache
async def download_file(url: str, save_path: Path) -> None:
    """Download file from url and save it to the local disk."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                content = await response.read()
                save_path.write_bytes(content)
    except aiohttp.ClientError as error:
        logger.exception("Error downloading file %s", url)
        raise error
    finally:
        await session.close()


@measure
def unzip_file(zip_file_path: Path, destination_dir: Path) -> None:
    """Unzip file and save it to the local disk."""
    try:
        if not destination_dir.exists():
            destination_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(zip_file_path, "r") as zip_file:
            zip_file.extractall(destination_dir)
    except Exception as error:
        logger.exception("Error unzipping file %s", zip_file_path)
        raise error


@async_measure
async def main() -> None:
    """Download dataset from the web and save it to the local disk."""
    phishing_website_dataset_url = \
        "http://archive.ics.uci.edu/static/public/327/phishing+websites.zip"

    await download_file(
        phishing_website_dataset_url,
        RAW_DATA_DIR / "phishing-websites.zip",
    )

    unzip_file(
        zip_file_path=RAW_DATA_DIR / "phishing-websites.zip",
        destination_dir=RAW_DATA_DIR / "phishing-websites"
    )

    arff_to_csv(
        path=RAW_DATA_DIR / "phishing-websites/Training Dataset.arff",
        destination_dir=DATA_DIR,
        file_name="phishing-websites",
    )


if __name__ == "__main__":
    asyncio.run(main())
