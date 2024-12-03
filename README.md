
# 🖥️ Interface de Monitoramento do Trajeto do Carrinho Bluetooth

Este repositório é parte de um conjunto de três repositórios que compõem o projeto do **Carrinho Bluetooth Controlado por App**, sendo eles:

- **CarroBluetooth-Interface (atual)**: Repositório da interface de monitoramento do trajeto realizado pelo carrinho.
- [CarroBluetooth-App (clique aqui!)](https://github.com/leonfagundes/CarroBluetooth-App): Repositório do aplicativo responsável pelo controle Bluetooth do carrinho.
- [CarroBluetooth-API (clique aqui!)](https://github.com/leonfagundes/CarroBluetooth-API): Repositório da API que conecta o carrinho ao banco de dados na nuvem.

---

## 🛠 Funcionalidades

- **Monitoramento do trajeto do carrinho**: O programa exibe o trajeto percorrido pelo carrinho em um gráfico, processando os comandos recebidos do banco de dados através da API.
- **Atualização automática do gráfico**: A interface é atualizada periodicamente para refletir os comandos mais recentes enviados ao carrinho.
- **Limpeza de dados**: Permite limpar os registros no banco de dados diretamente pela interface.

---

## 💻 Tecnologias Utilizadas

<p>
   <img src="https://github.com/tandpfun/skill-icons/blob/main/icons/Python-Dark.svg" alt="Python" width="50"/>
   <img src="https://github.com/tandpfun/skill-icons/blob/main/icons/VSCode-Dark.svg" alt="VSCode" width="50"/>
   <img src="https://github.com/tandpfun/skill-icons/blob/main/icons/Git.svg" alt="Git" width="50"/>
   <img src="https://github.com/tandpfun/skill-icons/blob/main/icons/Github-Dark.svg" alt="Github" width="50"/>
</p>

## 📚 Bibliotecas:

- **Matpltlib** ([Documentação oficial](https://matplotlib.org))
- **PyPI - Dotenv** ([Documentação oficial](https://pypi.org/project/python-dotenv/))
- **PyPI - Requests** ([Documentação oficial](https://pypi.org/project/requests/))

---

## 🧩 Requisitos

- [Python 3.x](https://www.python.org/) instalado no sistema
- Bibliotecas `requests`, `matplotlib`, e `python-dotenv` instaladas no ambiente Python

### Para instalar as bibliotecas

```bash
pip install requests matplotlib python-dotenv
```

---

## ⚙ Configuração do Projeto

### 1. Clonar o Repositório

```bash
git clone https://github.com/leonfagundes/CarroBluetooth-Interface.git
cd CarroBluetooth-Interface
```

### 2. Configurar o Ambiente

1. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

2. Configure o arquivo `.env` com a URL da API publicada:

```plaintext
API_BASE_URL=https://carrobluetooth-api-9bn0.onrender.com
```

---

## 🖥️ Uso da Interface

1. Inicie o programa com o seguinte comando:

```bash
python interface.py
```

2. Utilize os botões disponíveis na interface:
   - **Exibir Gráfico**: Exibe o trajeto registrado no banco de dados, destacando o ponto atual.
   - **Limpar Gráfico**: Limpa o gráfico e remove todos os registros no banco de dados.

3. A interface será atualizada automaticamente a cada 2 segundos para refletir as mudanças no trajeto.

---

## 🧩 Estrutura do Projeto

```plaintext
|-- interface.py      # Código principal da interface
|-- .env              # Variáveis de ambiente (URL da API)
|-- README.md         # Documentação do projeto
```

---

## 🖼️ Visual da Interface

Abaixo está uma prévia de como a interface se apresenta durante o monitoramento do trajeto:

- **Gráfico do trajeto em tempo real:**
  ![Gráfico de exemplo](https://github.com/leonfagundes27/Assets/blob/main/Images/print-interface-carro.png)

---

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto.
2. Crie uma nova branch com suas alterações (`git checkout -b feature/nova-funcionalidade`).
3. Faça commit de suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4. Envie para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

---

## Licença

Este projeto é de código aberto e está licenciado sob a licença MIT.
