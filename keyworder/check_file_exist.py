from pathlib import Path


def make_documents_subfolder(name: str) -> Path:  # create folder "name" in User/Documents folder

    """Validate the input data"""
    if not isinstance(name, str):
        raise TypeError("Input must be a string")

    (Path.home() / "Documents" / f"{name}").mkdir(parents=True, exist_ok=True)
    return Path.home() / "Documents" / f"{name}"


def create_file_if_no(subfolder_name: str, file_name: str) -> str:
    # Validate subfolder_name
    if not isinstance(subfolder_name, str):
        raise TypeError("subfolder_name must be a string")
    if not subfolder_name:
        raise ValueError("subfolder_name cannot be empty")

    # Validate file_name
    if not isinstance(file_name, str):
        raise TypeError("file_name must be a string")
    if not file_name:
        raise ValueError("file_name cannot be empty")

    # Additional validation
    if "/" in subfolder_name:
        raise ValueError("subfolder_name cannot contain slashes")
    if "/" in file_name:
        raise ValueError("file_name cannot contain slashes")

    path_to_folder = make_documents_subfolder(subfolder_name)

    Path(f"{path_to_folder}/{file_name}").touch(exist_ok=True)

    return f"{path_to_folder}/{file_name}"


if __name__ == '__main__':
    create_file_if_no('subflder_name', 'file_name')
