import src.utils.json_crud


class DatabaseObject:
    """
    manages the database data
    """
    # stores the database
    dataset: dict

    # stores the index of the new to add song
    # it does not go down, only up, and cannot be changed
    __global_index: int

    def __init__(self, data_path: str):
        self.dataset = src.utils.json_crud.read_data(data_path)


    def add_song(self, song_data: dict):
        pass

    def find_song(self, song_name: str):
        pass

    def remove_song(self, song_name: str):
        pass

    def update_song(self, song_name: str, song_data: dict):
        pass

    def get_song_data(self, song_name: str) -> dict:
        return {}

    def update_fields_data(self, field_name: str, field_new_data, lambda_func=None):
        pass

    def add_fields(self, fields_values: dict):
        pass

