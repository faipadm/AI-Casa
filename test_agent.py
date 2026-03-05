import sys, os
sys.path.append(os.getcwd())
from utils.parser import parse_prompt
from agent.plant_generator import generate_plan

print(parse_prompt("terreno 20x30 em São Paulo"))
print(generate_plan({'raw': 'test', 'terreno': '20x30'}))
