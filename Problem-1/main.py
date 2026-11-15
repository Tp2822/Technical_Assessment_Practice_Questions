def sort_names(names: str) -> str:
    """Sort names by lastname and parse the list."""
    if not names:
        return ""

    names_list = names.split(";")
    result = []
    for name in names_list:
        first_last_name = name.split(":")
        first = first_last_name[0]
        last = first_last_name[1]
        result.append((last.upper(), first.upper()))

    result.sort()

    output = ""
    for last, first in result:
        output += f"({last}, {first})"
    return output


if __name__ == "__main__":
    print(sort_names("John:Bell;Ann:Kern"))