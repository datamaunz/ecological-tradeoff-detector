from src.modules.load_packages import *




def display_methodology_page():
    
    
    #st.markdown("### Methodology")
    
    st.markdown("### 🔖 Methodology: Ecological Parameter Assessment for Funding Applications")
    
    st.divider()
    
    st.markdown(f"The methodology behind this paper is explained in\
        *[Estevez, I., Schollmeyer, J. (2023): Problem Analysis for Green Industrial Policy](https://www.springerprofessional.de/en/problem-analysis-for-green-industrial-policy/25977890).*\
        The goal is to provide an approach to evaluate proposals with regard to a list of parameters\
            relevant to the goal of preserving a liveable planet.\
            Note that this application is still in an experimental form.\
                The evaluations are based on OpenAI's `{st.session_state['model_name']}`.")
    
    
    st.markdown("Understanding the interconnected nature of ecological parameters is crucial for advancing the green transition. From the research by [Livotov et al., 2019](https://www.cambridge.org/core/journals/proceedings-of-the-international-conference-on-engineering-design/article/ecological-advanced-innovation-design-approach-for-efficient-integrated-upstream-and-downstream-processes/917F6006EDBE7C0AD2E8D4A15E10FE27), it can be seen that even projects that intend to improve ecological matters, carry inherent ecological trade-offs. Specifically, the study found that enhancing one out of 11 ecological parameters tends to negatively impact around three other parameters.")

    st.markdown("Given this dynamic, it's essential for administrators allocating funds to be cognizant that preserving a livable planet is a nuanced challenge with several intertwined ecological parameters.")

    st.divider()

    st.markdown("#### Proposal Evaluation System")
    st.markdown("For a holistic evaluation, each project proposal seeking funding should be assessed based on the following scale for each ecological parameter:")

    st.markdown("""
                `-1`: Indicates the project will likely have a negative effect on the parameter.
                
                `0 `: Indicates the project will likely have a neutral effect on the parameter.
                
                `+1`: Indicates the project will likely have a positive effect on the parameter.
                """)

    st.divider()
    st.markdown("#### Consideration for Funding")
    st.markdown("When deciding on which projects to fund, it's paramount that the funders:")

    st.markdown("""
                1. View the Cumulative Impact: Consider the collective effect of all funded projects to ensure a balanced outcome for the planet's ecology.
                2. Promote Intra-Project Balance: Encourage applicants to address and rectify internal trade-offs before submission. By ensuring that their projects inflict minimal harm on other parameters, applicants not only contribute to the broader ecological goal but also boost their chances of obtaining funding.""")

    st.markdown("By incorporating this methodology, the funding allocation process will be better equipped to support projects that holistically consider and address the myriad ecological parameters that govern our planet's health. This approach not only optimizes the use of funds but also steers innovation towards truly sustainable solutions.")
    
    
    
    
    #st.write(methodology_text)