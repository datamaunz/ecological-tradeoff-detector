from src.modules.load_packages import *


def initalize_session_state_dict():
    
    st.session_state["model_name"] = "gpt-4"
    
    st.session_state["instruction"] = "Evaluate the proposal for each of the parameters listed below.\
            To each of these parameters, assign 1 if the impact of the suggested proposal will likely improve the parameter.\
            Assign -1 if it will likely deteriorate the parameter.\
            Assign 0 if no impact can be expected.\
            Assign the label 'unclear' in case there is not enough information to make an estimate.\
                Display the estimate in the form of a table with three columns: 'Parameter', 'Estimate', 'Explanation'."
            
    st.session_state["list_of_parameters"] = [
        "Energy scarcity",
        "Natural resource attrition and degradation",
        "Irreversible resource commitments",
        "Dangerous levels of waste",
        "Water pollution","Air pollution", "Land pollution",
        "Marine Resources",
        "Global warming",
        "Biodiversity & Ecosystems",
        "Human health (including cumulative impacts of pollution)"]
    
    
    if "questions_simple" not in st.session_state:
        st.session_state["questions_simple"] = {}
        st.session_state["questions_simple"]["Project Description"] = {}
        #st.session_state["questions_simple"]["Environmental Impact"] = {}
        st.session_state["questions_simple"]["Resource Use"] = {}
        #st.session_state["questions_simple"]["Technological Aspects"] = {}
        
        st.session_state["questions_simple"]["Project Description"]["Executive summary"] = "Executive summary."
        st.session_state["questions_simple"]["Project Description"]["Objectives and goals"] = "Objectives and goals."
        st.session_state["questions_simple"]["Project Description"]["Geographic scope"] = "Geographic scope of the project."
        #st.session_state["questions_simple"]["Environmental Impact"]["Anticipated impacts"] = "Description of anticipated environmental impacts, both positive and negative."
        #st.session_state["questions_simple"]["Environmental Impact"]["Mitigation measures"] = "Measures to mitigate negative impacts."
        st.session_state["questions_simple"]["Resource Use"]["Required resources"] = "Type and amount of resources required (e.g., water, energy, land)."
        st.session_state["questions_simple"]["Resource Use"]["Resource sourcing"] = "Resource sourcing and sustainability considerations (along the entire supply chain)."
        #st.session_state["questions_simple"]["Technological Aspects"]["Technologies used"] = "Technologies to be used in the project."
        
    if "responses_simple" not in st.session_state:
        st.session_state["responses_simple"] = {}
        st.session_state["responses_simple"]["Project Description"] = {}
        st.session_state["responses_simple"]["Environmental Impact"] = {}
        st.session_state["responses_simple"]["Resource Use"] = {}
        st.session_state["responses_simple"]["Technological Aspects"] = {}
    
    
    if "prompt" not in st.session_state:
        st.session_state["prompt"] = ""
    
    if "response" not in st.session_state:
        st.session_state["response"] = ""
        