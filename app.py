from src.modules.load_packages import *
from src.pages.main_page import display_main_page

def main():
    st.set_page_config(layout="wide",
                       page_title="Tradeoff-Detector",
                       page_icon = '🌍')
    
    
    
        
    page_names_to_funcs = {
        "🧪 Evaluate your project": display_main_page,
        }
        
    
    selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
    page_names_to_funcs[selected_page]()
    
if __name__ == '__main__':
    main()
    