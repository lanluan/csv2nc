import numpy as np


def compute_fft_along_axis(data: np.ndarray, axis: int = 1) -> np.ndarray:
    """Compute FFT along the specified axis."""
    if not isinstance(data, np.ndarray):
        raise TypeError("data must be a numpy array")

    if axis < 0 or axis >= data.ndim:
        raise ValueError(f"axis must be in range [0, {data.ndim - 1}]")

    return np.fft.fft(data, axis=axis)
