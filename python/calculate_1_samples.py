import json
import random
from pathlib import Path

SAVE_PATH = "results_sampling/result_X.json"

RADIUS: float = 1  # Just for verbosity
SAMPLES: int = 1_000_000

min_pos = -RADIUS
max_pos = RADIUS

r2 = RADIUS * RADIUS


def rand_float(x: float, y: float, depth: int = 100_000) -> float:
    big: int = random.randint(round(x * depth), round(y * depth))
    ret: float = big / depth
    return ret


def sample_random_point() -> bool:
    x = rand_float(min_pos, max_pos)
    y = rand_float(min_pos, max_pos)
    dist_squared = x * x + y * y
    return dist_squared < r2


def calculate(do_save: bool = True, do_print: bool = False) -> float:
    hits: int = 0
    misses: int = 0
    for i in range(SAMPLES):
        hit = sample_random_point()
        if hit:
            hits += 1
        else:
            misses += 1
        if do_print:
            print(str(i) + "/" + str(SAMPLES))

    if do_print:
        print()

        print(hits)
        print(misses)
        print(SAMPLES)

        print()

        print(4 * hits / SAMPLES)

    if do_save:
        save(4 * hits / SAMPLES, hits, misses, SAMPLES)

    return 4 * hits / SAMPLES


def save(result: float, hits: int, misses: int, samples: int) -> None:
    target_path = Path(SAVE_PATH.replace("X", str(get_saved_result_count())))
    # Create the results_sampling folder automatically if it is missing
    target_path.parent.mkdir(parents=True, exist_ok=True)

    dictionary = {
        "result": result,
        "hits": hits,
        "misses": misses,
        "samples": samples
    }

    target_path.write_text(json.dumps(dictionary))


def load(path: str) -> dict:
    target_path = Path(path)
    text = target_path.read_text()
    return json.loads(text)


def get_saved_result_count() -> int:
    path = Path(SAVE_PATH).parent
    path.mkdir(parents=True, exist_ok=True)

    count = 0

    for item in path.iterdir():
        if item.is_file() and item.name.startswith("result_") and item.name.endswith(".json"):
            count += 1

    return count


def main() -> None:
    request = input("Enter 1 for a calculation or enter 2 for loading all the previous calculations: ")
    match request:
        case "1":
            calculate(do_print=True)
        case "2":
            results = []
            results_number = []
            for i in range(get_saved_result_count()):
                path = SAVE_PATH.replace("X", str(i))
                result = load(path)
                results.append(result)
                results_number.append(result["result"])
            result_avg = sum(results_number) / len(results_number)
            print(results)
            print(result_avg)


if __name__ == "__main__":
    main()
