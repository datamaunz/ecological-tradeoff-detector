from src.modules.load_packages import *


def initalize_session_state_dict():
    
    st.session_state["model_name"] = "gpt-3.5-turbo"
    
    st.session_state["instruction"] = "Evaluate the proposal for each of the parameters listed below.\
            To each of these parameters, assign 1 if the impact of the suggested proposal will likely improve the parameter.\
            Assign -1 if it will likely deteriorate the parameter.\
            Assign 0 if there will be no impact.\
            Assign the label 'unclear' in case there is not enough information to make an estimate."
            
    st.session_state["list_of_parameters"] = ["Energy scarcity", "Natural resource attrition and degradation", "Dangerous levels of waste", "Water pollution", "Air pollution", "Land pollution", "Ocean acidification", "Global warming"]
    
    
    
    if "prompt" not in st.session_state:
        st.session_state["prompt"] = ""
    
    
        