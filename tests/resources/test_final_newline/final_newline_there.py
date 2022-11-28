# pylint: skip-file
# type: ignore
@staticmethod
def create_img_json_map(list_of_meta_files: list) -> dict:
    """ Creates mapping from metafile-filename to image-filename """
    return {key: splitter(key) for key in list_of_meta_files if key.endswith("json")}
