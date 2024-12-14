import matplotlib.pyplot as plt


def plot_graph(normalized_noise, color_mode):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_ylim(0, 1)
    if color_mode:
        ax.plot(normalized_noise[0, :, 0], color="red")
        ax.plot(normalized_noise[0, :, 1], color="green")
        ax.plot(normalized_noise[0, :, 2], color="blue")
    else:
        ax.plot(normalized_noise[0, :], color="gray")
    ax.set_xlabel("X")
    ax.set_ylabel("Noise Value")
    ax.set_title("Y=0")
    return fig


import json
from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image

from generater import generate_noise, normalize, plot_noise
from utils import plot_graph


def save_params_to_json(params):
    params_json = json.dumps(params, indent=4)
    st.sidebar.download_button(
        label="Export Parameters",
        data=params_json,
        file_name="params.json",
        mime="application/json",
    )


def save_image(image_array, filename):
    image = Image.fromarray((image_array * 255).astype(np.uint8))
    buf = BytesIO()
    image.save(buf, format="PNG")
    st.download_button(
        label="Download Image",
        data=buf.getvalue(),
        file_name=filename,
        mime="image/png",
    )


def save_plot(fig, filename):
    buf = BytesIO()
    fig.savefig(buf, format="png")
    st.download_button(
        label="Download Graph",
        data=buf.getvalue(),
        file_name=filename,
        mime="image/png",
    )
