import numpy as np
from fft_utils import compute_fft_along_axis

def main():
    # 2 x 500 array of random temperatures (float64)
    temperature = np.random.random((2, 500))

    # FFT along the “long dimension” (axis=1, length 500)
    fft_data = compute_fft_along_axis(temperature, axis=1)

    print("input shape:", temperature.shape)
    print("fft shape:", fft_data.shape)

    # show first few values for row 0 and row 1
    for i in range(2):
        print(f"\nrow {i} first 6 FFT values:")
        print(fft_data[i, :6])


if __name__ == "__main__":
    main()
