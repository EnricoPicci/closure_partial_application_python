import pandas as pd


def build_sum_columns(start_count: int):
    count = start_count

    def sum_columns(row):
        nonlocal count
        count += 1
        print(f"Processing row {count}")
        return row["a"] + row["b"]

    return sum_columns


# Adds a column to a DataFrame - the new column is the sum of columns 'a' and 'b'
def add_column_to_df(_df):
    sum_columns = build_sum_columns(0)
    _df["c"] = df.apply(sum_columns, axis=1)


if __name__ == "__main__":
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    print("\nBefore processing all rows:")
    print(df)
    print("")
    add_column_to_df(df)
    print("\nAfter processing all rows:")
    print(df)

# python -m closures.add_column_to_df
