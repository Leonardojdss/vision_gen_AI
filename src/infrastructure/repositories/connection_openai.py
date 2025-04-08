from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class OpenAIConnection:
    """"
    Uma classe para gerenciar a conexão com o OpenAI
    """
    def __init__(self):
        """"
        Inicializa a conexão com o OpenAI com variáveis de ambiente.
        Levanta um ValueError se alguma variável de ambiente necessária estiver ausente.
        """
        self.azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.api_version = os.getenv("AZURE_OPENAI_API_VERSION")
        self.api_key = os.getenv("AZURE_OPENAI_API_KEY")
        self.maxretries = 0

        missing_variables = []

        if not self.api_key:
            missing_variables.append("AZURE_OPENAI_API_KEY")
        if not self.azure_endpoint:
            missing_variables.append("AZURE_OPENAI_ENDPOINT")
        if not self.api_version:
            missing_variables.append("AZURE_OPENAI_API_VERSION")    

        if missing_variables:        
            raise ValueError(f"As seguinte(s) variavel(is) esta(ão) ausente(s): {missing_variables}")

        self.client = AzureOpenAI(
            api_key=self.api_key,
            azure_endpoint=self.azure_endpoint,
            api_version=self.api_version,
            max_retries=self.maxretries
        )
    
    def connect(self):
        """ 
        Retorna o cliente do OpenAI.
        """
        return self.client
