import os
import pandas as pd
import time
import matplotlib.pyplot as plt
from pathlib import Path
from services.calculator_service import calculator_service


EXPRESSION_FILES = {
    "expression_1e3.txt": 2.708673211137267,
    "expression_1e4.txt": 1.9361217662961778,
    "expression_1e5.txt": 30.168668920426107,
    "expression_2e5.txt": -40.786517563680654,
    "expression_4e5.txt": -28.262839343470613,
    "expression_6e5.txt": -43.51917840747542,
    "expression_8e5.txt": -78.54296916429949,
    "expression_1e6.txt": -18.668906995495558,
}


def get_raw_expression(
        file_name: str
) -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = f"{current_dir}/data/{file_name}"
    with open(file_path) as file:
        raw_expression = file.read()
    return raw_expression


def create_plot(
        performance: pd.DataFrame,
        save_fig: bool = False
):
    plt.plot(
        [0, max(performance["input size"])],
        [0, max(performance["duration [ms]"])],
        label="$O(n)$",
        c="r",
        zorder=1
    )
    plt.scatter(
        performance["input size"],
        performance["duration [ms]"],
        label="measured",
        zorder=2
    )
    plt.title("Algorithm execution time dependecy on expression length")
    plt.ylabel("time [ms]")
    plt.xlabel("N tokens")
    plt.grid()
    plt.legend()

    if save_fig:
        path = Path(os.path.dirname(os.path.abspath(__file__))) / \
            "performance.png"
        plt.savefig(path)
        print(path.parent.absolute())

    plt.show()


def main():
    input_sizes = []
    durations = []
    is_solved = []
    print(f"Evaluating expressions...\n")
    for file_name, correct_result in EXPRESSION_FILES.items():
        raw_expression = get_raw_expression(file_name=file_name)
        input_size = float(file_name.split('_')[-1].strip('.txt'))
        start = time.time()
        result = calculator_service.solve(raw_expression)
        duration = round((time.time() - start) * 1000, 2)
        solved_correctly = result.value == correct_result
        input_sizes.append(input_size)
        durations.append(duration)
        is_solved.append(solved_correctly)

    performance = pd.DataFrame(
        {
            "file name": list(EXPRESSION_FILES.keys()),
            "input size": input_sizes,
            "duration [ms]": durations,
            "solved correctly": is_solved
        }
    )
    performance["input size"] = performance["input size"].astype(int)
    print("***************************** RESULTS *****************************")
    print(performance)
    create_plot(performance)


if __name__ == "__main__":
    main()
