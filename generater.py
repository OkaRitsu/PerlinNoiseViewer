import matplotlib.pyplot as plt
import noise
import numpy as np

WIDTH, HEIGHT = 1024, 1024
BASE_SCALE = 100.0


def generate_noise(color_mode, octaves, persistence, lacunarity, color_scale):
    if color_mode:
        noise_array = np.zeros((HEIGHT, WIDTH, 3))
        for c in range(3):
            for y in range(HEIGHT):
                for x in range(WIDTH):
                    nx = x / BASE_SCALE
                    ny = y / BASE_SCALE
                    nz = c / color_scale
                    noise_array[y][x][c] = noise.pnoise3(
                        nx,
                        ny,
                        nz,
                        octaves=octaves,
                        persistence=persistence,
                        lacunarity=lacunarity,
                    )
    else:
        noise_array = np.zeros((HEIGHT, WIDTH))
        for y in range(HEIGHT):
            for x in range(WIDTH):
                nx = x / BASE_SCALE
                ny = y / BASE_SCALE
                noise_array[y][x] = noise.pnoise2(
                    nx,
                    ny,
                    octaves=octaves,
                    persistence=persistence,
                    lacunarity=lacunarity,
                )
    return noise_array


def normalize(noise_array):
    min_val = np.min(noise_array)
    max_val = np.max(noise_array)
    return (noise_array - min_val) / (max_val - min_val)


def plot_noise(normalized_noise, color_mode):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Perlin Noise")
    if color_mode:
        ax.imshow(normalized_noise, origin="lower")
    else:
        ax.imshow(normalized_noise, cmap="gray", origin="lower")
    return fig
