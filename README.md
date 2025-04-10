# vision_gen_AI

## Descrição do Projeto

O `vision_gen_AI` é um projeto que combina visão computacional com modelos generativos da OpenAI para realizar diversas tarefas relacionadas à análise de imagens. Ele utiliza modelos de linguagem avançados para interpretar imagens e gerar respostas baseadas em prompts específicos. As principais funcionalidades incluem:

- **OCR (Reconhecimento Óptico de Caracteres):** Extração de texto presente em imagens, preservando a formatação original.
- **Descrição de Imagens:** Geração de descrições detalhadas sobre o conteúdo visual de uma imagem, incluindo objetos, cores, ações e contexto.
- **Extração de Chaves e Valores:** Identificação e extração de pares de chave e valor presentes em imagens.
- **Análise Personalizada:** Permite ao usuário fornecer um prompt personalizado para analisar a imagem de acordo com suas necessidades.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python 3.12 ou superior

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/Leonardojdss/vision_gen_AI
   cd vision_gen_AI
   ```

2. Crie um ambiente virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:

   Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

   ```env
   AZURE_OPENAI_ENDPOINT=<seu_endpoint>
   AZURE_OPENAI_API_VERSION=<sua_versao>
   AZURE_OPENAI_API_KEY=<sua_chave_api>
   ```

5. Adicione o caminho do projeto ao `PYTHONPATH`:

   ```bash
   export PYTHONPATH=$(pwd)
   ```

## Uso

1. Execute o aplicativo Streamlit:

   ```bash
   streamlit run src/app.py
   ```

2. No navegador, você verá a interface do projeto. Siga as etapas abaixo:

   - Escolha um modelo de LLM na barra lateral.
   - Selecione a funcionalidade desejada (OCR, Descrever Imagem, Extrair Chaves e Valores ou Personalizado).
   - Faça o upload de uma imagem no formato `.jpg`, `.jpeg` ou `.png`.
   - Clique no botão "Iniciar análise" para processar a imagem.

3. O resultado será exibido na interface principal.

## Exemplos de Uso

### OCR
Carregue uma imagem contendo texto e selecione a funcionalidade "OCR". O sistema extrairá o texto presente na imagem.

### Descrição de Imagens
Carregue uma imagem e selecione "Descrever Imagem". O sistema gerará uma descrição detalhada do conteúdo visual.

### Extração de Chaves e Valores
Carregue uma imagem contendo informações estruturadas (como formulários) e selecione "Extrair Chaves e Valores". O sistema identificará e extrairá os pares de chave e valor.

### Análise Personalizada
Carregue uma imagem e selecione "Personalizado". Insira um prompt descrevendo o que deseja analisar na imagem.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Para dúvidas ou sugestões, entre em contato pelo e-mail: seu-email@exemplo.com

