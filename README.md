# Busondi - sistema de localização de ônibus
Projeto da disciplina "Prática em desenvolvimento de Software"

## Equipe
- Arthur Lisboa - Desenvolvedor front-end
- Helena Pato - Desenvolvedora back-end
- Jackson Nunes - Desenvolvedor back-end
- Pedro Henrique Bertolini - Desenvolvedor front-end

## Escopo

### Funcional

O principal objetivo do sistema é o acompanhamento de linhas de ônibus na cidade de Belo Horizonte, MG. Ele terá as funcionalidades de listar os horários previstos de chegada dos ônibus de acordo com sua grade agendada, além do acompanhamento da posição dos veículos em tempo real, usando [informações da  prefeitura do município](https://dados.pbh.gov.br/dataset/tempo_real_onibus_-_coordenada/resource/d7ce6e9b-343f-4e83-8b46-68fa90a12d59?inner_span=True). O sistema também será capaz de sugerir uma ou mais rotas, dados um endereço de partida e um de destino. As rotas sugeridas poderão envolver mais de uma linha de ônibus que cumpram esse percurso.

### Tecnológico
Para a implementação do back-end do projeto serão utilizados a linguagem Python e o framework Django, com o banco de dados sqlite. No caso do front-end, será utilizado o framework Angular, que é baseado na linguagem TypeScript.

## MVP (Minimum Viable Product)

A criação de um MVP para o sistema Busondi se basearia no tipo conhecido como **Mágico de Oz**, no qual a entrega de soluções é feita manualmente, por pessoas reais. Em suma, uma interface de interação seria oferecida ao cliente, através da qual ele estaria apto a solicitar um dos dois serviços principais do sistema: o acompanhamento de uma linha de ônibus específica, oferecendo seu respectivo identificador ou a verificação de rotas possíveis, dando um endereço de partida e outro de destino. Tendo recebido os dados, uma equipe nos bastidores entraria em ação, procurando manualmente as informações em sistemas de terceiros (como na [consulta de itinerários da BHTRANS](https://prefeitura.pbh.gov.br/bhtrans/informacoes/transportes/onibus/consulta-itinerarios)) para só então retornar a resposta ao usuário. Nesse caso, não seriam fornecidos dados em tempo real, devido à complexidade para realizar tal tarefa de modo manual; seriam retornados, pois, os dados estáticos, bem como previsões de tempo de embarque e chegada. Nessa estratégia, o tempo gasto em desenvolvimento seria basicamente na parte de front-end, cuja equipe poderia fornecer uma interface simples em tempo hábil. 

É válido ressaltar, no entanto, que a criação de um MVP para esse tipo de sistema talvez não seja a melhor estratégia a ser adotada, uma vez que se baseia em uma ideia já existente e amplamente utilizada no mundo real. No lugar, poderiam ser adotadas técnicas de Product Discovery, como Design Thinking ou Jobs to be Done.

## Histórias de usuário

- Como usuário do sistema Busondi, quero descobrir qual o ponto de ônibus mais próximo em que a minha linha passa e em qual sentido.
- Como usuário do sistema Busondi, quero descobrir quais linhas de ônibus passam por um ponto de ônibus.
- Como usuário do sistema Busondi, quero descobrir qual o horário agendado para uma dada linha de ônibus passar por um dado ponto. 
- Como usuário do sistema Busondi, quero descobrir qual a previsão de chegada do ônibus, baseada em sua posição atual.
- Como usuário do sistema Busondi, quero descobrir qual a posição atual do ônibus em meio a sua rota.
- Como usuário do sistema Busondi, quero fornecer um endereço de partida e outro de destino e receber sugestões de linhas de ônibus que fazem esse percurso.
- Como usuário do sistema Busondi, quero (fazer login para) salvar linhas, pontos de ônibus e endereços que uso frequentemente e ter acesso rápido a eles.
- Como usuário do sistema Busondi, quero poder ver um mapa do meu entorno que destaque pontos de ônibus próximos, que podem ser selecionados.
- Como usuário do sistema Busondi, quero poder ver toda a rota de uma dada linha de ônibus, destacando todas as suas paradas, incluindo seu ponto final.
- Como usuário do sistema Busondi, quero poder dar feedbacks sobre as previsões fornecidas pelo sistema, por exemplo, se um ônibus já passou ou não.
- Como usuário do sistema Busondi, quero salvar um ponto, uma linha e um horário em que, quando o ônibus se aproximar, serei notificado.
