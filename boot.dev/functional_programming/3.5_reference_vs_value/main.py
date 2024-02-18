def add_format(default_formats: dict[str, bool], new_format: str) -> dict[str, bool]:
    updated_formats = default_formats.copy()
    updated_formats[new_format] = True
    return updated_formats


def remove_format(default_formats: dict[str, bool], old_format: str) -> dict[str, bool]:
    updated_formats = default_formats.copy()
    updated_formats[old_format] = False
    return updated_formats
