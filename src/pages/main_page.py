from src.modules.load_packages import *


def create_prompt(proposal_desc, resources):
    """_summary_

    Args:
        proposal_desc (_type_): _description_
        resources (_type_): _description_
    """
    
    if proposal_desc:
        prompt = f"The following proposal has to be evaluated: {proposal_desc}"
    else:
        prompt = ""
        
    if resources:
        prompt = f"{prompt} About the resources, we know the following: {resources}"
    
    prompt = f"""
    
    {prompt}
    
    {st.session_state['instruction']}
    
    The parameters that are to be used for the assessement are:
    
    {', '.join(st.session_state['list_of_parameters'])}"""
    
    return prompt

def generate_prompt():
    
    
    specifications = []
    for category in st.session_state["responses_simple"].keys():
                for question in st.session_state["responses_simple"][category].keys():
                    specifications.append(f'{question}: {st.session_state["responses_simple"][category][question]}')
    
    specifications_string = "\n".join(specifications)
    
    prompt = f'{specifications_string}\n\n\n{st.session_state["instruction"]}\
        \n\nThe parameters that are to be used for the assessement are:{st.session_state["list_of_parameters"]}'
    
    return prompt
    

@st.cache_resource
def generate_response(prompt):

    response = openai.ChatCompletion.create(
        model=st.session_state["model_name"],
        messages=[
            {"role": "system", "content": "You are a diligent advisor."},
            {"role": "user", "content": prompt}
            ])
    return response["choices"][0]["message"]["content"]

def display_main_page():
    st.markdown("### 🧪 Evaluate Your Proposal (Test Version)")
    
    
    #with st.form("my_form"):
    #    st.write("### Describe your proposal")
        
    #    proposal_desc = st.text_area('Describe the proposal', max_chars=3000)    
    #    resources = st.text_area("What resources are being used? From where are they sourced?", max_chars=3000)
    #    submitted = st.form_submit_button("Evaluate the proposal")
         
    #    if submitted:
            
    #        st.session_state["prompt"] = create_prompt(proposal_desc, resources)
    #        st.success("Success!")

    with st.form("simple form"):
        data_dict = {}
        st.write("### Describe your proposal")
        for category in st.session_state["questions_simple"].keys():
            data_dict[category] = {}
            st.markdown(f'#### {category}')
            
            questions = st.session_state["questions_simple"][category].keys()
            for question in questions:
                question_text = st.session_state["questions_simple"][category][question]
                data_dict[category][question] = st.text_area(question_text, max_chars=500)    
            
        
        submitted_button = st.form_submit_button("Evaluate this proposal")
        

        if submitted_button:
            
            for category in data_dict.keys():
                for question in data_dict[category].keys():
                    st.session_state["responses_simple"][category][question] = data_dict[category][question]
                    
            prompt = generate_prompt()
                
            st.session_state["response"] = generate_response(prompt)
            
            
    st.write(st.session_state["response"])
            
    