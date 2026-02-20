from pathlib import Path


def ensure_project_dirs(project_root):
    """
    Ensures that the project's data and storage directories exist.


    Args:
        project_root: The path to the root directory of the project.


    Returns:
        A tuple containing the paths to the project's data and storage directories.
    """
    data_dir = project_root / 'data'
    storage_dir = project_root / 'storage'

    data_dir.mkdir(exist_ok=True)
    storage_dir.mkdir(exist_ok=True)

    return data_dir, storage_dir
