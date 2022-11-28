# pylint: skip-file
# type: ignore    
@staticmethod
def extract_groundtruth(uv_data: dict,
        cam_id: str,
    edge: str) -> Tuple[Union[list, np.ndarray], Union[list, np.ndarray]]:
    return dots_x, dots_y