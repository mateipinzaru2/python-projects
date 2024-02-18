valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line


def pair_document_with_format(
    doc_names: list[str], doc_formats: list[str]
) -> list[tuple[str, str]]:
    """
    Computes a list of filtered tuples, representing documents names and their format.

    Args:
        doc_names (list[str]): names of documents.
        doc_formats (list[str]): formats of documents.

    Returns:
        list[tuple[str]]: zipped and filtered list of document names and their format.
    """

    zipped = list(zip(doc_names, doc_formats))
    return list(filter(lambda item: item[1] in valid_formats, zipped))
