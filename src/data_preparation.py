from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"


def load_data(filename, columns=None):
    file_path = DATA_DIR / filename

    if file_path.suffix == ".json":
        df = pd.read_json(file_path, lines=True)

    elif file_path.suffix == ".csv":
        df = pd.read_csv(file_path)

    else:
        raise ValueError(f"Unsupported file format: {file_path.suffix}")

    if columns is not None:
        df = df[columns]

    return df