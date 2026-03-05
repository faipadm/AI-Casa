import streamlit as st
import os
import sys
sys.path.append(os.getcwd())

try:
    from utils.parser import parse_prompt
    from agent.plant_generator import generate_plan
    from utils import data_fetcher
    from calculations import calculate_all
    from render_3d import generate_3d_images
    from video_simulation import generate_construction_video
except ImportError as e:
    st.error(f"Erro de importação: {e}")
    st.stop()

st.title("Agente de Planta de Casa Avançado")

prompt = st.text_area("Digite o prompt para a casa:", "terreno 20x30 em São Paulo com 3 quartos e 2 banheiros")

if st.button("Gerar Planta Completa"):
    with st.spinner("Processando..."):
        try:
            # Parse prompt
            data = parse_prompt(prompt)
            st.write("Dados extraídos:", data)
            
            # Fetch external data
            loc = data.get("localizacao")
            if loc:
                codes = data_fetcher.fetch_building_codes(loc)
                mapfile = data_fetcher.fetch_maps(loc)
                st.write("Códigos de construção:", codes)
            
            # Generate plan
            plan_file = generate_plan(data)
            st.success(f"Planta gerada: {plan_file}")
            if os.path.exists(plan_file):
                st.download_button("Baixar DXF", open(plan_file, "rb"), file_name="plan.dxf")
            
            # 3D Images
            st.subheader("Imagens 3D")
            interior_3d, exterior_3d = generate_3d_images(data)
            if os.path.exists(interior_3d):
                st.image(interior_3d, caption="Interior 3D")
            if os.path.exists(exterior_3d):
                st.image(exterior_3d, caption="Exterior 3D")
            
            # Calculations
            st.subheader("Cálculos Detalhados")
            calc_results = calculate_all(data)
            st.json(calc_results)
            
            # Video
            st.subheader("Vídeo de Construção")
            try:
                video_file = generate_construction_video(data)
                if video_file and os.path.exists(video_file):
                    if video_file.endswith('.mp4'):
                        st.video(video_file)
                    else:
                        st.image(video_file, caption="Simulação de Construção")
                else:
                    st.write("Simulação não gerada")
            except Exception as e:
                st.write(f"Erro na simulação: {e}")
        except Exception as e:
            st.error(f"Erro durante o processamento: {e}")
