import json
from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image

from generater import generate_noise, normalize, plot_noise
from utils import plot_graph, save_image, save_params_to_json, save_plot


def main():
    # パーリンノイズの設定
    octaves = st.sidebar.slider("Octaves", min_value=1, max_value=20, value=5)
    persistence = st.sidebar.slider(
        "Persistence", min_value=0.01, max_value=2.0, value=0.5, step=0.01
    )
    lacunarity = st.sidebar.slider(
        "Lacunarity", min_value=0.01, max_value=5.0, value=2.0, step=0.01
    )

    # カラー化
    color_mode = st.sidebar.checkbox("Color Mode")
    color_scale = st.sidebar.slider(
        "Color Scale",
        min_value=0.1,
        max_value=255.0,
        value=10.0,
        step=0.1,
        disabled=not color_mode,
    )

    # パラメータをJSON形式で保存
    params = {
        "octaves": octaves,
        "persistence": persistence,
        "lacunarity": lacunarity,
        "color_mode": color_mode,
        "color_scale": color_scale,
    }
    save_params_to_json(params)

    st.markdown("# Perlin Noise Viewer")

    noise_array = generate_noise(
        color_mode, octaves, persistence, lacunarity, color_scale
    )
    normalized_noise = normalize(noise_array)

    col1, col2 = st.columns(2)
    prefix = f"oct_{octaves}-per_{persistence}-lac_{lacunarity}"
    prefix += f"-color_{color_scale}" if color_mode else "-gray"
    filename = f"{prefix}.png"

    with col1:
        # ノイズ画像の表示
        fig1 = plot_noise(normalized_noise, color_mode)
        st.pyplot(fig1)
        save_image(normalized_noise, filename)

    with col2:
        fig2 = plot_graph(normalized_noise, color_mode)
        st.pyplot(fig2)
        save_plot(fig2, "graph_" + filename)


if __name__ == "__main__":
    main()
