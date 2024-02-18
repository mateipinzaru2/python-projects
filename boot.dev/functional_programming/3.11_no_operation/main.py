"""
Complete the markdown_to_text function.

It should:

    Remove any # characters that are at the beginning of a line. (Headings in markdown.) Use lstrip which also removes leftover whitespace.

    Remove any single and double * characters that are at the start or end of a word. (Emphasis in markdown.) Use strip.
"""


def markdown_to_text(doc_content: str) -> str:
    input_lines = doc_content.split("\n")
    output_lines = []

    for line in input_lines:
        if line:
            line = line.lstrip("# ")
            line = " ".join(
                word.strip("*") if len(word) > 1 else word for word in line.split()
            )
        output_lines.append(line)

    return "\n".join(output_lines)
