from io import StringIO, TextIOWrapper
import re
from pathlib import Path
from typing import Any, Callable, Iterable
from unittest.mock import patch

def get_all_files_path(parent_path: Path) -> list[tuple[Path, Path]]:
    all_files_path: list[Path] = [file for file in parent_path.glob('**/*') if file.is_file()]
    files_path_to_check: list[tuple[Path, Path]] = []

    in_pattern = re.compile(r'.*.in')
    for file in all_files_path:
        parent: Path = file.parent
        in_file_name: str = file.name

        if in_pattern.match(in_file_name):
            out_file_name: str = f"{in_file_name[:-3]}.out"
            out_file: Path = parent / out_file_name
            if out_file.exists():
                files_path_to_check.append((file, out_file))
    
    return files_path_to_check

def get_input_and_output(parent_path: Path) -> Iterable[tuple[list[str], list[str]]]:
    files_to_check: list[tuple[Path, Path]] = get_all_files_path(parent_path)
    for in_file_path, out_file_path in files_to_check:
        with open(in_file_path) as in_file, open(out_file_path) as out_file:
            input = get_all_words(in_file)
            output = get_all_words(out_file)
            yield (input, output)

def run_main(main_function: Callable[[], None], pair_of_input_output: tuple[list[str], list[str]]) -> None:
    input, output = pair_of_input_output

    with patch('builtins.input', side_effect=input), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        main_function()
        result = mock_stdout.getvalue().split()

    assert len(output) == len(result)
    assert all([a == b for a, b in zip(output, result)])

def get_all_lines(file: TextIOWrapper) -> list[str]:
    lines: list[str] = []
    
    for line in file:
        lines.append(line)
    return lines

def get_all_words(file: TextIOWrapper) -> list[str]:
    words: list[str] = []

    for line in get_all_lines(file):
        words += line.split()
    return words