"""Utility functions for the project."""
import logging
import psutil
from functools import wraps
from time import time

import pandas as pd
import scipy

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def async_measure(func):
    """Measure the execution time, memory usage, and network bandwidth of a function."""

    @wraps(func)
    async def wrapper(*args, **kwargs):
        """Wrapper function."""
        start_time = time()
        start_memory = psutil.Process().memory_info().rss
        start_net_stats = psutil.net_io_counters()

        result = await func(*args, **kwargs)

        end_time = time()
        end_memory = psutil.Process().memory_info().rss
        end_net_stats = psutil.net_io_counters()

        sent_bandwidth = (
            end_net_stats.bytes_sent - start_net_stats.bytes_sent
        ) / (1024 * 1024)  # MB
        received_bandwidth = (
            end_net_stats.bytes_recv - start_net_stats.bytes_recv
        ) / (1024 * 1024)  # MB

        logger.info(
            f"Function {func.__name__!r} executed in {end_time - start_time:.4f} seconds.\n"
            f"Memory usage: {(end_memory - start_memory) / 1024:.0f} KB.\n"
            f"Sent bandwidth: {sent_bandwidth:.3f} MB.\n"
            f"Received bandwidth: {received_bandwidth:.3f} MB.\n"
        )

        return result

    return wrapper


def measure(func):
    """Measure the execution time, memory usage, and network bandwidth of a function."""


    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function."""
        start_time = time()
        start_memory = psutil.Process().memory_info().rss
        start_net_stats = psutil.net_io_counters()

        result = func(*args, **kwargs)

        end_time = time()
        end_memory = psutil.Process().memory_info().rss
        end_net_stats = psutil.net_io_counters()

        sent_bandwidth = (
            end_net_stats.bytes_sent - start_net_stats.bytes_sent
        ) / (1024 * 1024)  # MB
        received_bandwidth = (
            end_net_stats.bytes_recv - start_net_stats.bytes_recv
        ) / (1024 * 1024)  # MB

        logger.info(
            f"Function {func.__name__!r} executed in {end_time - start_time:.4f} seconds.\n"
            f"Memory usage: {(end_memory - start_memory) / 1024:.0f} KB.\n"
            f"Sent bandwidth: {sent_bandwidth:.3f} MB.\n"
            f"Received bandwidth: {received_bandwidth:.3f} MB.\n"
        )

        return result

    return wrapper


def arff_to_csv(path: str, destination_dir: str, file_name: str) -> str:
    """Convert arff file to csv file."""
    data, meta = scipy.io.arff.loadarff(path)
    # Decode the data from bytes to strings
    data = pd.DataFrame(data).map(lambda x: x.decode("utf-8"))
    data.to_csv(destination_dir / f"{file_name}.csv", index=False)
    return "Successfully converted arff file to csv file."
