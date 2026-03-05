"""Módulo para cálculos detalhados de construção."""

import pandas as pd
from typing import Dict, Any

def calculate_all(data: Dict[str, Any]) -> Dict[str, Any]:
    """Calcula medidas, custos, materiais, etc."""
    terreno = data.get("terreno", "20x30")
    try:
        width, height = map(float, terreno.split('x'))
        area = width * height
    except:
        area = 600  # default
    
    quartos = data.get("quartos", 3)
    banheiros = data.get("banheiros", 2)
    
    # Estimativas simples (em cenário real, usar bancos de dados reais)
    materials = {
        "cimento": area * 0.1,
        "areia": area * 0.2,
        "tijolos": area * 50,
        "ferro": area * 10
    }
    
    costs = {
        "materiais": sum(materials.values()) * 100,  # R$ estimado
        "mao_de_obra": area * 500,
        "acabamento": quartos * 10000 + banheiros * 5000,
        "mobiliario": quartos * 15000,
        "eletrodomesticos": quartos * 5000
    }
    
    weights = {
        "estrutura": area * 2000,  # kg
        "acabamento": area * 500
    }
    
    machinery = ["escavadeira", "betoneira", "guindaste"]
    
    return {
        "medidas": {"area": area, "largura": width, "altura": height},
        "materiais": materials,
        "custos": costs,
        "pesos": weights,
        "maquinario": machinery,
        "total_custo": sum(costs.values())
    }