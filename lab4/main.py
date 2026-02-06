import math
import multiprocessing

NUM_PROCESSES = max(1, multiprocessing.cpu_count() - 1)


def f(x):
    return math.cos(x) + (math.log(x + 1) ** 2)


def compute_chunk(args):
    start, end, step = args
    result = []
    x = start
    while x < end:
        result.append((x, f(x)))
        x = x + step
    return result


if __name__ == "__main__":
    x_min = 1.0
    x_max = 1e6
    step = 0.01
    chunk_width = (x_max - x_min) / NUM_PROCESSES
    chunks = []
    for i in range(NUM_PROCESSES):
        start = x_min + i * chunk_width
        end = x_min + (i + 1) * chunk_width
        chunks.append((start, end, step))
    with multiprocessing.Pool(processes=NUM_PROCESSES) as pool:
        chunk_results = pool.map(compute_chunk, chunks)
    all_results = []
    for chunk_list in chunk_results:
        all_results.extend(chunk_list)
    print("Obliczono", len(all_results), "punktow.")
    print("Przyklad: dla x=1 wartosc f(x) =", all_results[0][1])
    print("Przyklad: dla x=100 wartosc f(x) =", all_results[9900][1])
