from pathlib import Path


def get_name_from_file(file_path: Path) -> str:
    return file_path.name.split('.')[0]