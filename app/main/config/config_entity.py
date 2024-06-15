from dataclasses import dataclass
import os
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    roor_dir:Path
    raw_data_path: Path
    ingested_data_path: Path

    