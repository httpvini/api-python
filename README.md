# api-python

Api em python, utilizando connexion e swagger. Para fins de estudo.

## Getting Started

Para testar o funcionamento, basta clonar este repositório, buildar a imagem docker com o comando: *docker build -t <nome_da_imagem> .* 
Depois execute o comando: *docker-compose up -d* 
Todos os comandos devem ser executados no diretório da aplicação. 
Após isso, basta abrir o navegador e acessar http://localhost:5000/
### Pré-requisitos

É necessário ter o docker e o docker-compose instalado.

### Endpoints

Para configurar seus endpoints, adicione suas configurações no swagger.yml

Para acessar a interface web do swagger e obter detalhes sobre os endpoints disponíveis na api, acesse:
http://localhost:5000/api/ui/
