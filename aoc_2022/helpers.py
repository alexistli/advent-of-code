def load_day_input(path: str) -> list[str]:
    with open(path) as f:
        data = f.readlines()
    return data
