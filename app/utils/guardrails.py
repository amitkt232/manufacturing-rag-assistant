BLOCKED_TERMS = [

    "hack",

    "bypass",

    "explosive",

    "weapon"
]


def validate_query(query):

    lower_query = query.lower()

    for term in BLOCKED_TERMS:

        if term in lower_query:

            return False

    return True