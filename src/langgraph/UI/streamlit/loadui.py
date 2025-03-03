import streamlit as st
import os
from dotenv import load_dotenv
from datetime import date

from langchain_core import AIMessage, HumanMessage, SystemMessage
from src.langgraph.UI.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_config = {}

    def initialize_state(self):
        return {
            "timeframe": "",
            "current_step": "requirements",
            "requirements": "",
            "user_stories": "",
            "IsFetchButtonClicked": False,
            "Is_SDLC": False
        }
    
    # def render_requirements(self):
    #     st.markdown("## Requirements Submission")
    #     st.session_state.state["requirements"] = st.text_area("Enter Your Requirements", height=100, key="get_requirements")

    #     if st.button("Submit Requirements", key="submit_requirements"):
    #         st.session_state["current_step"] = "generate_user_stories"
    #         st.session_state.IsSLDC = True


    def load_ui(self):
        st.set_page_config(
            page_title="👁" + self.config.get_page_title(),
            #page_icon=self.config.get_page_icon(),
            layout="wide"
        )
        st.header(self.config.get_page_title())
        st.markdown("---")
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.Is_SDLC = False

        with st.sidebar:
            #Getting sidebar options from the config file
            LLM_OPTIONS = self.config.get_llm_options()
            USE_CASE_OPTIONS = self.config.get_usecase_options()

            #Creating a dropdown for the LLM options
            st.session_state.selected_llm = st.selectbox("Select LLM", LLM_OPTIONS)

            if st.session_state.selected_llm == "Groq":
                model = self.config.get_groq_model()
                st.session_state.selected_model = st.selectbox("Select Model", model)
                st.session_state.selected_model_api_key = st.text_input("Enter API Key", type="password")

                #validating the API key
                if not st.session_state.selected_model_api_key:
                    st.error("Please enter the correct API key. refer :  https://console.groq.com/keys")

            #Creating a dropdown for the use case options
            st.session_state.selected_usecase = st.selectbox("Select Use Case", USE_CASE_OPTIONS)

            if "state" not in st.session_state:
                st.session_state.state = self.initialize_state()
            #self.render_requirements()

        return self.user_controls

            
