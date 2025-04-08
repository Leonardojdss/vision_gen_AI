from src.infrastructure.repositories.connection_openai import OpenAIConnection

# Cliente Azure OpenAI
client = OpenAIConnection().connect()

def completion_image(image_base64: str, prompt: str, model: str):
    """
    Função para analisar uma imagem
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            { 
            "role": "system",
            "content": f"{prompt}"  
            },
            {
            "role": "user",
            "content": 
                [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_base64}"
                        }
                    }
                ]                
            }
        ],
        temperature=0.1
    )
    return response.choices[0].message.content