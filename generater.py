import matplotlib.pyplot as plt
import noise
import numpy as np

WIDTH, HEIGHT = 1024, 1024


def generate_noise(
    color_mode,
    octaves,
    persistence,
    lacunarity,
    num_grids,
    color_scale,
):
    x_scale = WIDTH // num_grids
    y_scale = HEIGHT // num_grids
    if color_mode:
        noise_array = np.zeros((HEIGHT, WIDTH, 3))
        for c in range(3):
            for y in range(HEIGHT):
                for x in range(WIDTH):
                    nx = x / x_scale
                    ny = y / y_scale
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
                nx = x / x_scale
                ny = y / y_scale
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


def plot_noise(normalized_noise, color_mode, num_grids=0):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Perlin Noise")
    if color_mode:
        ax.imshow(normalized_noise, origin="lower")
    else:
        ax.imshow(normalized_noise, cmap="gray", origin="lower")
    if num_grids > 0 and num_grids < 20:
        w = normalized_noise.shape[0]
        h = normalized_noise.shape[1]
        for x in range(0, w, w // num_grids):
            ax.axhline(x, color="white", lw=0.5)
        for y in range(0, h, w // num_grids):
            ax.axvline(y, color="white", lw=0.5)
    return fig
