from dataclasses import dataclass # type: ignore
import os
from pathlib import Path

from numpy.core.arrayprint import str_format # type: ignore


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    n_rows: int
    raw_data_path: Path
    loaded_data_path: Path
    chunk_size: int

@dataclass(frozen=True)
class DataCleaningConfig:
    root_dir: Path
    loaded_data_path: Path
    clean_data_path: Path
    chunk_size: int

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    loaded_data_path: Path
    clean_data_path: Path
    chunk_size: int

