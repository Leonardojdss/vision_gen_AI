import base64

def encode(image):
    """
    Função para codificar uma imagem em base64
    """
    encoded_string = base64.b64encode(image.read()).decode('utf-8')
    return encoded_string
