# Busondi - sistema de localização de ônibus
Projeto da disciplina "Prática em desenvolvimento de Software"

## Equipe
- Arthur Lisboa - Desenvolvedor front-end
- Helena Pato - Desenvolvedora back-end
- Jackson Nunes - Desenvolvedor back-end
- Pedro Henrique Bertolini - Desenvolvedor front-end

<details>
  <summary>
    <h1>Escopo</h1>
  </summary>

### Funcional

O principal objetivo do sistema é o acompanhamento de linhas de ônibus na cidade de Belo Horizonte, MG. Ele terá as funcionalidades de listar os horários previstos de chegada dos ônibus de acordo com sua grade agendada, além do acompanhamento da posição dos veículos em tempo real, usando [informações da  prefeitura do município](https://dados.pbh.gov.br/dataset/tempo_real_onibus_-_coordenada/resource/d7ce6e9b-343f-4e83-8b46-68fa90a12d59?inner_span=True). O sistema também será capaz de sugerir uma ou mais rotas, dados um endereço de partida e um de destino. As rotas sugeridas poderão envolver mais de uma linha de ônibus que cumpram esse percurso.

### Tecnológico
Para a implementação do back-end do projeto serão utilizados a linguagem Python e o framework Flask, com o banco de dados sqlite. No caso do front-end, será utilizado o framework Angular, que é baseado na linguagem TypeScript.
</details>

<details>
  <summary>
    <h1>MVP (Minimum Viable Product)</h1>
  </summary>

A criação de um MVP para o sistema Busondi se basearia no tipo conhecido como **Mágico de Oz**, no qual a entrega de soluções é feita manualmente, por pessoas reais. Em suma, uma interface de interação seria oferecida ao cliente, através da qual ele estaria apto a solicitar um dos dois serviços principais do sistema: o acompanhamento de uma linha de ônibus específica, oferecendo seu respectivo identificador ou a verificação de rotas possíveis, dando um endereço de partida e outro de destino. Tendo recebido os dados, uma equipe nos bastidores entraria em ação, procurando manualmente as informações em sistemas de terceiros (como na [consulta de itinerários da BHTRANS](https://prefeitura.pbh.gov.br/bhtrans/informacoes/transportes/onibus/consulta-itinerarios)) para só então retornar a resposta ao usuário. Nesse caso, não seriam fornecidos dados em tempo real, devido à complexidade para realizar tal tarefa de modo manual; seriam retornados, pois, os dados estáticos, bem como previsões de tempo de embarque e chegada. Nessa estratégia, o tempo gasto em desenvolvimento seria basicamente na parte de front-end, cuja equipe poderia fornecer uma interface simples em tempo hábil. 

É válido ressaltar, no entanto, que a criação de um MVP para esse tipo de sistema talvez não seja a melhor estratégia a ser adotada, uma vez que se baseia em uma ideia já existente e amplamente utilizada no mundo real. No lugar, poderiam ser adotadas ferramentas de Product Discovery, como Jobs to be Done.
</details>

<details>
  <summary>
    <h1>Backlog</h1>
  </summary>

### Do Produto

1. Como usuário do sistema Busondi, quero descobrir quais linhas de ônibus passam por um ponto de ônibus.
2. Como usuário do sistema Busondi, quero descobrir qual o horário agendado para uma dada linha de ônibus passar por um dado ponto.
3. Como usuário do sistema Busondi, quero (fazer login para) salvar linhas, pontos de ônibus e endereços que uso frequentemente e ter acesso rápido a eles.
4. Como usuário do sistema Busondi, quero salvar um ponto, uma linha e um horário em que, quando o ônibus se aproximar, serei notificado.
5. Como usuário do sistema Busondi, quero descobrir qual a posição atual do ônibus em meio a sua rota.
6. Como usuário do sistema Busondi, quero poder ver toda a rota de uma dada linha de ônibus, destacando todas as suas paradas, incluindo seu ponto final.
7. Como usuário do sistema Busondi, quero descobrir qual a previsão de chegada do ônibus, baseada em sua posição atual.
8. Como usuário do sistema Busondi, quero descobrir qual o ponto de ônibus mais próximo em que a minha linha passa e em qual sentido.
9. Como usuário do sistema Busondi, quero fornecer um endereço de partida e outro de destino e receber sugestões de linhas de ônibus que fazem esse percurso.
10. Como usuário do sistema Busondi, quero poder ver um mapa do meu entorno que destaque pontos de ônibus próximos, que podem ser selecionados.
11. Como usuário do sistema Busondi, quero poder dar feedbacks sobre as previsões fornecidas pelo sistema, por exemplo, se um ônibus já passou ou não.

### Do Sprint 2

Tarefas técnicas back-end
  - Fazer diagrama da arquitetura do sistema [Helena]
  - Fazer esquema relacional do BD [Helena]
  - Criar banco de dados sqlite com as entidades do sistema [Jackson]
  - Criar projeto Flask [Jackson]

Tarefas técnicas front-end
  - Definir organização do projeto [Pedro]
  - Definir arquitetura [Arthur]
  - Definição de bibliotecas e frameworks adicionais [Pedro e Arthur]

História 1: Como usuário do sistema Busondi, quero descobrir quais linhas de ônibus passam por um ponto de ônibus.

Tarefas:
  - Obter [dados GTFS estáticos](https://dados.pbh.gov.br/dataset/gtfs-estatico-do-sistema-convencional) de ônibus em BH [Helena]
  - Processar os dados para ficarem no formato condizente com o esquema relacional [Helena]
  - Inserir os dados no BD [Jackson]
  - Criar endpoint `GET /stops` que retorna a lista de pontos cadastrados [Helena]
  - Criar endpoint `GET /stops/<stop_id>` que retorna a lista de linhas que passam por um dado ponto [Helena]
  - Criar interface do endpoint `GET /stops` [Arthur]
  - Criar interface do endpoint `GET /stops/<stop_id>` [Pedro]

História 2: Como usuário do sistema Busondi, quero descobrir qual o horário agendado para uma dada linha de ônibus passar por um dado ponto.

Tarefas:
  - Implementar algoritmo para calcular, dado o horário de partida e a localização do ponto, quanto tempo o ônibus deve demorar a chegar [Jackson]
  - Complementar o endpoint `GET /stops/<stop_id>` com a informação de, dada a hora atual, qual o próximo horário agendado para cada linha passar em dado ponto, usando o algoritmo citado acima [Jackson]
  - Adicionar, na interfacedo endpoint `GET /stops/<stop_id>`, o horário agendado de chegada de cada linha [Arthur]

História 3: Como usuário do sistema Busondi, quero (fazer login para) salvar linhas, pontos de ônibus e endereços que uso frequentemente e ter acesso rápido a eles.

Tarefas:
  - Criar CRUD de usuário [Helena]
  - Criar lógica de login de usuário [Jackson]
  - Adicionar tabela de favoritos do usuário no banco de dados [Jackson]
  - Criar CRUD de favoritos [Helena]
  - Criar interfaces de:
    * Criação de usuário, [Arthur]
    * Login, [Arthur]
    * Informações do usuário, [Pedro]
    * Listagem de favoritos [Pedro]

História 5: Como usuário do sistema Busondi, quero descobrir qual a posição atual do ônibus em meio a sua rota.

Tarefas:
  - Obter [dados de posição atual dos ônibus](https://dados.pbh.gov.br/dataset/tempo_real_onibus_-_coordenada) [Jackson]
  - Implementar lógica de atualização dos dados de posição atual dos ônibus [Jackson]
  - Criar endpoint `GET /current-position/<route_id>` que retorna a informação de posição atual do ônibus [Helena]
  - Criar interface com mapa que mostra a posição atual do ônibus em meio à sua rota (shape) [Pedro]

História 6: Como usuário do sistema Busondi, quero poder ver toda a rota de uma dada linha de ônibus, destacando todas as suas paradas, incluindo seu ponto final.

Tarefas: 
   - Criar endpoint `GET /routes/<route_id>` que retorna a informação de toda a rota do ônibus com seus pontos de parada [Jackson]
   - Criar interface com mapa que mostra toda a rota do ônibus com seus pontos de parada [Arthur]
</details>
 
<details>
  <summary>
    <h1>Arquitetura do Sistema</h1>
  </summary>

### Arquitetura Hexagonal
A Arquitetura Hexagonal consiste em criar componentes desacoplados, cuja conexão é feita por adaptadores e portas. O sistema Busondi se beneficia desse padrão arquitetural para ter independência entre lógica de aplicação e tecnologia, o que permite a substituição de componentes individualmente sem interferir no restante do projeto, além de aumentar a testabilidade. A arquitetura completa pode ser observada na imagem a seguir:
  
![DiagramaArquitetura](https://user-images.githubusercontent.com/42253628/172059355-b6b91ca7-f055-417c-a6ff-30160c1c5d63.jpg)

Como é possível observar, existem dois tipos de portas: 
- **Portas de entrada:** funcionam como interfaces para as classes externas acessarem métodos da classes de domínio. Um exemplo é a porta ```GetStop```, que retorna métodos de ```GetStopImpl```.
```python
class GetStop:
    def get_all_stops():
        return GetStopImpl.get_all_stops_impl()

    def get_stop_by_id(stop_id):
        return GetStopImpl.get_stop_by_id_impl(stop_id)

    def get_stops_coordinates(stops_list):
        return GetStopImpl.get_stops_coordinates_impl(stops_list)

    def get_stops_from_route(route_id):
        return GetStopImpl.get_stops_from_route_impl(route_id)
```

- **Portas de saída:** funcionam como interfaces para classes de domínio acessarem métodos de classes externas. A classe ```StopsRepository``` desempenha essa função, chamando métodos da classe ```StopsRepositoryImpl```.
```python
class StopsRepository:
    
    def return_all_stops():
        return StopsRepositoryImpl.return_all_stops_impl()

    def return_stop_by_id(stop_id):
        return StopsRepositoryImpl.return_stop_by_id_impl(stop_id)

    def return_all_stops_in_list(stops_list):
        return StopsRepositoryImpl.return_all_stops_in_list_impl(stops_list)
```

Também existem dois tipos de adaptadores: 
* Aqueles que recebem requisições de fora do sistema e chamam os métodos adequados através das portas de entrada, como o ```bus_stops_controller.py```, que chama o método ```get_all_stops()``` pela ```porta GetStop```.
```python
  def list_stops():
    stops_list = GetStop.get_all_stops()

    stops_dict = {}
    for stop in stops_list:
        stops_dict[stop.stop_id] = {
            'stop_lat' : stop.stop_lat,
            'stop_lon': stop.stop_lon,
            'stop_name' : stop.stop_name
        }
        
    return make_response(jsonify(stops_dict), 200)
```
  
* Aqueles que recebem chamadas vindas de dentro do domínio, através de uma porta de saída e realiza a conexão com um sistema externo, como por exemplo um Banco de Dados. A classe ```StopsRepositoryImpl``` desempenha essa função.
```python
  class StopsRepositoryImpl:
    def return_all_stops_impl():
        with DBConnection() as connection:
            all_stops = connection.session.query(BusStops).all()
        return all_stops

    def return_stop_by_id_impl(stop_id):
        with DBConnection() as connection:
            stop = connection.session.query(BusStops).get(stop_id)
        return stop

    def return_all_stops_in_list_impl(stops_list):
        with DBConnection() as connection:
            stops_list = connection.session.query(BusStops).filter(BusStops.stop_id.in_(stops_list)).all()
        return stops_list
```

### Domain-Driven Design (DDD)

</details>  
  
## Modelo das principais telas

Disponível no [Figma](https://www.figma.com/file/hSx4UFs5TYbPq3AHop0nI1/Clickons?node-id=243%3A471).

## Dados

[GTFS Estático do Sistema Convencional](https://dados.pbh.gov.br/dataset/gtfs-estatico-do-sistema-convencional)

[Tempo Real Ônibus - Coordenada atualizada](https://dados.pbh.gov.br/dataset/tempo_real_onibus_-_coordenada)
