"""Simulação de vídeo de construção (placeholder)."""

import matplotlib.pyplot as plt
import numpy as np

def generate_construction_video(data: dict) -> str:
    """Gera uma imagem estática simulando construção (placeholder para vídeo)."""
    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, "Simulação de Construção\nCasa crescendo...", ha='center', va='center', fontsize=20)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.savefig("construction_simulation.png")
    plt.close()
    return "construction_simulation.png"  # Return image instead of video