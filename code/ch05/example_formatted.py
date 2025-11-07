"""Example showing code after black formatting."""

from collections import Counter


def calculate_statistics(
    data, include_mean=True, include_median=False, include_mode=False
):
    """Calculate various statistics with proper formatting."""
    results = {}

    if include_mean:
        results["mean"] = sum(data) / len(data)

    if include_median:
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            results["median"] = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            results["median"] = sorted_data[n // 2]

    if include_mode:
        counts = Counter(data)
        results["mode"] = counts.most_common(1)[0][0]

    return results


class DataProcessor:
    """Process data with consistent formatting."""

    def __init__(
        self,
        data,
        normalize=False,
        remove_outliers=True,
        outlier_threshold=3.0,
    ):
        self.data = data
        self.normalize = normalize
        self.remove_outliers = remove_outliers
        self.outlier_threshold = outlier_threshold

    def process(self):
        """Process the data."""
        result = self.data[:]

        if self.remove_outliers:
            mean = sum(result) / len(result)
            std_dev = (sum((x - mean) ** 2 for x in result) / len(result)) ** 0.5
            result = [
                x for x in result if abs(x - mean) <= self.outlier_threshold * std_dev
            ]

        if self.normalize:
            min_val, max_val = min(result), max(result)
            result = [(x - min_val) / (max_val - min_val) for x in result]

        return result


def complex_function_with_long_arguments(
    argument_one,
    argument_two,
    argument_three,
    argument_four,
    argument_five,
    argument_six,
):
    """Function with arguments properly split across lines."""
    return (
        argument_one
        + argument_two
        + argument_three
        + argument_four
        + argument_five
        + argument_six
    )


# Dictionary with proper formatting
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "username": "admin",
        "password": "secret",
    },
    "cache": {"enabled": True, "ttl": 3600},
    "logging": {
        "level": "INFO",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    },
}


# List comprehension properly formatted
def example_with_long_comprehension():
    """Example function with a properly formatted list comprehension."""
    data_source = []
    filtered_and_transformed_data = [
        x * 2 for x in data_source if x > 0 and x < 100 and x % 2 == 0
    ]
    return filtered_and_transformed_data
