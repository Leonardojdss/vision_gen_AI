from src.service.completion import completion_image, completion_text
from src.service.base64 import encode

class AnalyzeImageUseCase:
    """
    Classe para casos de uso de análise de imagem
    """
    @staticmethod
    def analyze_image(image_input, prompt, model):
        """
        Caso de uso de análise de imagem
        """
        # Convert a image to base64
        image_base64 = encode(image_input)

        # call the service of completions
        response = completion_image(image_base64, prompt, model)
        return response

    @staticmethod
    def analyze_image_text(input_text, model):
        """
        Caso de uso de análise de texto de imagem
        """
        # call the service of completions
        response = completion_text(input_text, model)
        return response