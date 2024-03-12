from pathlib import Path
import pytest
from src.alc.alc import main
from src.resources.tester import get_input_and_output, run_main

TIMEOUT: int = 1

@pytest.mark.timeout(TIMEOUT)
@pytest.mark.parametrize('pair_of_input_output', get_input_and_output(Path(__file__).parent.resolve()))
def test_main(pair_of_input_output: tuple[list[str], list[str]]) -> None:
    run_main(main, pair_of_input_output)