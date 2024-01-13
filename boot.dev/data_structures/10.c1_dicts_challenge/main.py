"""
CHECK GRADE
A local college is having trouble with its student administration program. They have asked you to help them print a student's grade from their English_1010 class.

Here's the structure of a student dictionary:

{
    "type": {
        "student": {
            "name": "Allan",
            "courses": {
                "math_1050": {
                    "current_grade": "B",
                },
                "English_1010": {
                    "current_grade": "A-",
                },
            },
        }
    }
}

CHALLENGE
Complete the get_english_grade function. It accepts a student nested dictionary and returns the student's grade in English 1010.
"""


def get_english_grade(student):
    try:
        return (
            student.get("type", {})
            .get("student", {})
            .get("courses", {})
            .get("English_1010", {})
            .get("current_grade")
        )
    except AttributeError:
        return None
