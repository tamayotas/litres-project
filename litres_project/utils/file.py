def abs_path_from_project(relative_path: str):
    import litres_project
    from pathlib import Path

    return (
        Path(litres_project.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
