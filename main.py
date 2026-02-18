from pathlib import Path


def ensure_project_dirs(project_root: Path) -> tuple[Path, Path]:
    data_dir = project_root / 'data'
    storage_dir = project_root / 'storage'

    data_dir.mkdir(exist_ok=True)
    storage_dir.mkdir(exist_ok=True)

    return data_dir, storage_dir


def main() -> None:
    project_root = Path('.').resolve()  # absolute path to current folder
    data_dir, storage_dir = ensure_project_dirs(project_root)

    print(f"Project root: {project_root}")
    print(f"Data directory: {data_dir}")
    print(f"Storage directory: {storage_dir}")

    print("Done")


if __name__ == '__main__':
    main()
