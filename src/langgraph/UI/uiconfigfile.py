from configparser import ConfigParser

class Config:
    def __init__(self):
        #os.path.join(os.path.dirname(__file__), 'uiconfigfile.ini')
        self.config = ConfigParser()
        self.config.read('uiconfigfile.ini')

    def get_llm_option(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
