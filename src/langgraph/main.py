import streamlit as st
import json
from .UI.streamlit.loadui import LoadStreamlitUI
from .llm.groqllm import GroqLLM
from .graph.graph_builder import GraphBuilder
from .UI.streamlit.displayresult import DisplayResultStreamlit


def load_app():
    """
    
    Loads and runs the LangGranph Agentic AI POC application.

    """

    #load the UI
    ui = LoadStreamlitUI()
    user_input = ui.load_ui()

    if not user_input:
        st.error("Please enter the requirements and click on the button to generate the SDLC")
        return
    
    #Test input for user message state
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.state.timeframe
    else:
        user_message = st.chat_input("Enter your message here...")

    #Initialize the LLM
    if user_message:
        try:
            llm = GroqLLM(user_controls_input=user_input)
            model = llm.get_llm_model()

            if not model:
                st.error("Failed to initialize the LLM model")
                return
            
            #select use-case
            use_case = user_input.get("selected_use_case")
            if not use_case:
                st.error("No Use Case Selected")
                return
            
            #Graph Builder
            graph_builder = GraphBuilder(llm=model, use_case=use_case)
            try:
                graph = graph_builder.setup_graph(use_case)
                DisplayResultStreamlit(use_case, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph setup failed - {e}")
                return
                

        except Exception as e:
            raise ValueError(f"Error Occurred with Exception : {e}")
            
