from laeyerz.nodes.Node import Node
import pandas as pd

class FileLoader(Node):
    def __init__(self, node_name, config={}):
        super().__init__(node_name, config)

    def load_file(self, file_path):
        if file_path.endswith('.csv'):
            return pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            return pd.read_excel(file_path)
        elif file_path.endswith('.json'):
            return pd.read_json(file_path)
        elif file_path.endswith('.parquet'):
            return pd.read_parquet(file_path)
        elif file_path.endswith('.feather'):
            return pd.read_feather(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_path}")


def main():
    file_path = 'data/test.csv'
    data = load_file(file_path)
    print(data)

if __name__ == "__main__":
    main()