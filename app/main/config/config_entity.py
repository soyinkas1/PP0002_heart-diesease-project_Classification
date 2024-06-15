from dataclasses import dataclass
import os
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    n_rows: int
    raw_data_path: Path
    loaded_data_path: Path
    chunk_size: int

