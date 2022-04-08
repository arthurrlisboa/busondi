# Busondi - sistema de localização de ônibus
Projeto da disciplina "Prática em desenvolvimento de Software"

## Equipe
- Arthur Lisboa - Desenvolvedor front-end
- Helena Pato - Desenvolvedora back-end
- Jackson Nunes - Desenvolvedor back-end
- Pedro Henrique Bertolini - Desenvolvedor front-end

## Escopo

### Funcional

O principal objetivo do sistema é o acompanhamento de linhas de ônibus na cidade de Belo Horizonte, MG. Ele terá as funcionalidades de listar os horários previstos de chegada dos ônibus de acordo com sua grade agendada, além do acompanhamento da posição dos veículos em tempo real, com a ajuda de uma [API](https://developers.google.com/transit/gtfs-realtime). O sistema também será capaz de sugerir uma ou mais rotas, dados um endereço de partida e um de destino. As rotas sugeridas poderão envolver mais de uma linha de ônibus que cumpram esse percurso.

### Tecnológico
Para a implementação do back-end do projeto serão utilizados a linguagem Python e o framework Django, com o banco de dados sqlite. No caso do front-end, será utilizado o framework Angular, que é baseado na linguagem TypeScript.


## MVP (Minimum Viable Product)

A criação de um MVP para o sistema Busondi se basearia no tipo conhecido como **Mágico de Oz**, no qual a entrega de soluções é feita manualmente, por pessoas reais. Em suma, uma interface de interação seria oferecida ao cliente, através da qual ele inicialmente forneceria seus dados para uma rápida autenticação e em seguida estaria apto a solicitar um dos dois serviços principais do sistema: o acompanhamento de uma linha de ônibus específica, oferecendo seu respectivo identificador ou a verificação de rotas possíveis, dando um endereço de partida e outro de destino. Tendo recebido os dados, uma equipe nos bastidores entraria em ação, procurando manualmente as informações em sistemas de terceiros para só então retornar ao usuário a resposta. Nessa estratégia, o tempo gasto em desenvolvimento seria basicamente na parte de front-end, cuja equipe poderia fornecer uma interface simples em tempo hábil.

É válido ressaltar, no entanto, que a criação de um MVP para esse tipo de sistema talvez não seja a melhor estratégia a ser adotada, uma vez que se baseia em uma ideia já existente e amplamente utilizada no mundo real. Por que motivo, por exemplo, um cliente deixaria de usar um sistema completo como o Moovit para fazer uso de uma versão limitada dele? É essa pergunta que nos leva à proposta de uma outra estratégia: a busca por um diferencial que elevaria o sistema Busondi à competitividade de mercado.
