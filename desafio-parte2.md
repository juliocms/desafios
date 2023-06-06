# Desafio Parte 2

* Considerando o alto volume de transações e cargas de trabalho em grandes quantidades, dividi abaixo possíveis soluções:

    - Como vários processamentos simultânes e cargas de trabalho gigantes, seria interessante utilizarmos um banco de dados distribuído capacidade de lidar com situações como essa. 
        Existem várias opções no mercado que podem atender essa demanda. Bancos de dados Distribuídos são projetados para escalabilidade horizontal e 
        alta disponibilidade.

    - Como apresentado na pergunta que é necessário apresentar o valor total do mês, uma abordagem interessante para isto seria adotar o processamento em Lote. Com todas as transações
        armazenadas podemos executar um processamento em lote para o cáculo do ganho total mensal. Isso permite que podemos processar grandes volumes de dados de forma paralela. 
        A ferramenta mais interessante e que é amplamente utilizada no mercado é o Apache Spark e para armazenamento poderia ser utilizado o Azure Data Lake Gen2, que é integrado no Azure com o Spark.
        Ainda com essa preocupação de termos cáculo do ganho total mensal, podemos também armazenar os resultados agregados em um banco de dados separado, como um banco de dados colunar, 
        que é otimizado para consultas analíticas. Dessa forma você poderá obter resultados pré-calculados do valor total do mês, economizando tempo de processamento.

    - Quando estamos tratando de m volume gigantesco de transações podemos adotar o Balanceamento de carga. Isso faz com que consigamos a distribuição de carga de forma equilibrada entre os serviços da Cloud.
        O Balanceamento de carga também evita gargalos e maximiza o desempenho.

    - Quando estamos lidando com volumes de transações dessa magnitude é importante Monitorar e realizar Logging dessas transações. Isso é uma estratégia tanto para identificar problemas quanto para otimizar
        o desempenho dos recursos utilizados.
        

    