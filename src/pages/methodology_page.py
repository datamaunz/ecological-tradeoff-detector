from src.modules.load_packages import *




def display_methodology_page():
    methodology_text = f"The methodology behind this paper is explained in *Estevez, L.I., Schollmeyer, J. (forthcoming): Problem Analysis for Green Industrial Policy.*\
        The goal is to provide an approach to evaluate proposals with regard to a list of parameters relevant to the goal of preserving a liveable planet.\
            Note that this application is still in an experimental form. The evaluations are based on OpenAI's `{st.session_state['model_name']}`."
    
    
    st.markdown("### Methodology")
    
    st.write(methodology_text)