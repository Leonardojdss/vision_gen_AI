from src.infrastructure.repositories.connection_openai import OpenAIConnection

# Cliente Azure OpenAI
client = OpenAIConnection().connect()

def completion_image(image_base64: str, prompt: str, model: str):
    """
    Função para analisar uma imagem
    """
    # load prompt path or prompt text
    if prompt.endswith(".txt"):
        with open(prompt, "r") as file:
            prompt = file.read()
    else:
        prompt = prompt

    print(f"Prompt: {prompt}")
    response_image = client.chat.completions.create(
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
    return response_image.choices[0].message.content

def completion_text(input: str, model: str):
    """
    Função para conversar
    """
    response_text = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": input
            }
        ],
        temperature=0.1
    )
    return response_text.choices[0].message.content