# Sistema de Monitoramento de Utilização de CPU

## Descrição do Projeto

Este projeto consiste em um sistema de monitoramento da porcentagem de utilização de CPU de um determinado computador durante a execução de trabalhos, como a transcodificação de vídeo. O sistema permite aos usuários visualizarem a utilização atual da CPU e analisarem tendências de uso ao longo do tempo.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do sistema.
- **Matplotlib**: Biblioteca para criação de gráficos e visualização de dados, utilizada para exibir os dados de utilização da CPU.
- **Tkinter**: Biblioteca padrão do Python para criação de interfaces gráficas.
- **NumPy**: Biblioteca para manipulação de arrays e operações matemáticas em Python.
- **SciPy**: Biblioteca para funções matemáticas avançadas, estatísticas e otimização em Python.

## Instalação

Para executar o projeto, siga os passos abaixo:

1. Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo [aqui](https://www.python.org/downloads/).

2. Clone este repositório para o seu ambiente local:

```
git clone https://github.com/lima-vinicius/group8-if971.git
```

3. Navegue até o diretório do projeto:

```
cd group8-if971/src/
```

4. Instale as dependências do projeto utilizando o pip (gerenciador de pacotes do Python):
   
```
pip install [tkinter, numpy, scipy, matplotlib]
```

## Executando o Projeto

Após a instalação das dependências, execute o projeto com o seguinte comando:

```
python3 main.py
```

Isso iniciará a aplicação de monitoramento.

## Processo de Desenvolvimento

O desenvolvimento deste projeto seguiu os seguintes passos:

1. **Análise de Requisitos:** Compreensão dos requisitos do projeto, incluindo a necessidade de monitorar a utilização da CPU e as tecnologias a serem utilizadas.

2. **Estruturação do Projeto:** Definição da estrutura de diretórios e arquivos do projeto, incluindo a separação por módulos.

3. **Implementação dos Módulos:** Desenvolvimento das funções para consulta da utilização da CPU e atualização dos gráficos de visualização.

4. **Interface Gráfica:** Implementação da interface gráfica utilizando a biblioteca Tkinter para exibir os gráficos de utilização da CPU.

5. **Testes e Depuração:** Realização de testes para garantir o funcionamento correto do sistema e correção de eventuais erros ou bugs.

6. **Documentação:** Elaboração da documentação do projeto, incluindo este arquivo README.md e comentários nos códigos para facilitar a compreensão e manutenção do sistema.

## Autor

- [Vinícius Lima](https://github.com/lima-vinicius)

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
