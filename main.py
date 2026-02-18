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


def discover_doc_files(data_dir):
    """Discover all .md and .txt files in data_dir and its subdirectories.

    Returns a sorted list of all discovered files.
    """
    txt_files = list(data_dir.rglob('*.md'))
    md_files = list(data_dir.rglob('*.txt'))

    files = md_files + txt_files

    return sorted(files)


def main():
    """
    Prints the project root, data directory and storage directory to the console.

    After resolving the absolute path to the current folder, it ensures that
    the project's data and storage directories exist, and then prints the
    absolute paths to the project root, data directory and storage directory.

    Prints "Done" when it has finished.
    """
    project_root = Path('.').resolve()  # absolute path to current folder
    data_dir, storage_dir = ensure_project_dirs(project_root)

    print(f"Project root: {project_root}")
    print(f"Data directory: {data_dir}")
    print(f"Storage directory: {storage_dir}")

    print("Done")


if __name__ == '__main__':
    main()
