class Questionario:
    
   
    def __init__(self, aluno):
        self.aluno = aluno
        print("Digite 's' para responder sim e 'n' para responder não.")
        self.questoes = {
            "Instabilidade de atenção": [
                
                "\n1. Desvia facilmente sua atenção do que está fazendo,quando recebe um pequeno estímulo.\nUm assobio do vizinho é suficiente para interromper uma leitura.\n",
                
                "\n2. Tem dificuldade em prestar atenção à fala dos outros.\nNuma conversa com outra pessoa tende a captar apenas ”pedaços” soltos do assunto.\n",
                
                "\n3. Desorganização cotidiana.\nTende a perder objetos (chaves, celular, canetas, papéis), atrasar-se ou faltar a compromissos, \nesquecer o dia de pagamento das contas (luz, gás, telefone, seguro).\n",
                
                "\n4. Frequentemente apresenta ”brancos” durante uma conversa.\n A pessoa está explicando um assunto e no meio da fala esquece o que ia dizer.\n",
                
                "\n5. Tendência a interromper a fala do outro.\nNo meio de uma conversa lembra de algo e fala sem esperar o outro completar seu raciocínio.\n",
                
                "\n6. Costuma cometer erros de fala, leitura ou escrita.\nEsquece uma palavra no meio de uma frase ou pronuncia errado palavras longas como ”cineangiocoronariografia”.\n",
                
                "\n7. Presença de hiperfoco (concentração intensa em um único assunto num determinado período). Pode ficar horas a fio no computador sem se dar conta do que acontece ao seu redor.\n",
                
                "\n8. Dificuldade de permanecer em atividades obrigatórias de longa duração. Participar como ouvinte de uma palestra em que o tema não seja motivo de grande interesse e não o faça entrar em hiperfoco.\n",

                "\n9. Interrompe tarefas no meio.\n",

            ],
            "Hiperatividade fisica ou mental": [
                
                "\n10. Dificuldade em permanecer sentado por muito tempo. Durante uma palestra ou sessão de cinema costuma mexer-se o tempo todo na tentativa de permanecer em seu lugar.\n",
                "\n11. Está sempre mexendo com os pés ou as mãos. São os indivíduos que têm os pés ”nervosos”, girando suas cadeiras de trabalho, ou que estão sempre com suas mãos ocupadas, pegando objetos, desenhando em papéis ou ainda ajeitando suas roupas ou seus cabelos.\n",
                "\n12. Constante sensação de inquietação ou ansiedade. Um DDA sempre tem a sensação de que tem algo a fazer ou pensar, de que alguma coisa está faltando.\n",
                "\n13. Tendência a estar sempre ocupado com alguma problemática em relação a si ou com os outros. São as pessoas que ficam ”remoendo” sobre suas falhas cometidas, ou ainda sobre os problemas de amigos ou conhecidos.\n",
                "\n14. Costuma fazer várias coisas ao mesmo tempo. É a pessoa que lê e vê TV ou ouve música simultaneamente.\n",
                "\n15. Envolve-se em vários projetos ao mesmo tempo. Um exemplo é a pessoa que tem várias ideias simultaneamente e acaba por não levar a cabo nenhuma delas em função desta dispersão.\n",
                "\n16. Às vezes se envolve em situações de alto risco em busca de estímulos fortes, como dirigir em alta velocidade.\n",
                "\n17. Frequentemente fala sem parar, monopolizando as conversas em grupo. É a pessoa que fala sem se dar conta de que as outras estão tentando emitir suas opiniões (além de não se dar conta do impacto que o conteúdo do seu discurso pode estar causando a outras pessoas).\n",


            ],
            "Impulsividade": [
               
               "\n18. Baixa tolerância à frustração. Quando quer algo não consegue esperar, se lança impulsivamente numa tarefa, mas, como tudo na vida requer tempo, tende a se frustrar e desanimar facilmente.\n",
                "\n19. Costuma responder a alguém antes que este complete a pergunta. Não consegue conter o impulso de responder ao primeiro estímulo criado pelo início de uma pergunta.\n",
                "\n20. Costuma provocar situações constrangedoras, por falar o que vem à mente sem filtrar o que vai ser dito. Durante uma discussão, um DDA pode deixar escapar ofensas impulsivas.\n",
                "\n21. Impaciência marcante no ato de esperar ou aguardar por algo. Filas, telefonemas, atendimento em lojas ou restaurantes podem ser uma tortura.\n",
                "\n22. Impulsividade para comprar, sair de empregos, romper relacionamentos, praticar esportes radicais, comer, jogar etc. É aquela pessoa que rompe um relacionamento várias vezes e volta logo depois, arrependida.\n",
                "\n23. Reage irrefletidamente às provocações, críticas ou rejeição. É o tipo de pessoa que explode de raiva ao sentir-se rejeitada.\n",
                "\n24. Tendência a não seguir regras ou normas preestabelecidas. Um exemplo seria o trabalhador que teima em não usar equipamentos de segurança, apesar de saber da importância destes.\n",
                "\n25. Compulsividade. Na realidade a compulsão ocorre pela repetição constante dos impulsos, os quais, com o tempo, passam a fazer parte da vida dessas pessoas, como as compulsões por compras, jogos, alimentação etc.\n",
                "\n26. Sexualidade instável. Tende a apresentar períodos de grande impulsividade sexual alternados com fases de baixo desejo.\n",
                "\n27. Ações contraditórias. Um TDAH é capaz de ter uma explosão de raiva por causa de um pequeno detalhe (por mexerem em sua mesa de trabalho, por exemplo) numa hora, e poucos momentos mais tarde, ser capaz de uma grande demonstração de afeto, através de um belo cartão, flores ou um carinho explícito. Ou ainda ser um homem arrojado e moderno no trabalho e, ao mesmo tempo, tradicional e conservador no âmbito familiar e afetivo.\n",
                "\n28. Hipersensibilidade. O TDAH costuma melindrar-se facilmente. Uma simples observação desfavorável sobre a cor de seus sapatos é suficiente para deixá-lo internamente arrasado, sentindo-se inadequado.\n",
                "\n29. Hiper-reatividade. Essa é uma característica que faz com que o TDAH se contagie facilmente com os sentimentos dos outros. Pode ficar profundamente triste ao ver alguém chorar, mesmo sem saber o motivo, ao mesmo tempo que pode ficar muito agitado ou irritado em ambientes barulhentos ou em presença de multidão.\n",
                "\n30. Tendência a culpar os outros. Um TDAH muitas vezes poderá culpar outra pessoa por seus fracassos e erros, como o aluno que culpa o colega de turma por ter errado em uma questão da prova, já que este colega estava cantarolando baixinho na hora.\n",
                "\n31. Mudanças bruscas e repentinas de humor (instabilidade de humor). O TDAH costuma mudar de humor rapidamente, várias vezes no mesmo dia, dependendo dos acontecimentos externos ou ainda de seu estado cerebral, uma vez que o cérebro do TDAH pode entrar em exaustão, prejudicando a modulação do seu estado de humor.\n",
                "\n32. Tendência a ser muito criativo e intuitivo. O impulso criativo do TDAH é talvez a maior de suas virtudes. Pode se manifestar nas mais diversas áreas do conhecimento humano.\n",
                "\n33. Tendência ao ”desespero”. Quando um TDAH se vê diante de uma dificuldade, seja ela de qualquer ordem, ele tende a vê-la como algo impossível de ser transposto e com isso sente-se tomado por uma grande sensação de incapacidade. Sua primeira reação é o ”desespero”. Só mais tarde consegue raciocinar e constatar o verdadeiro ”peso” que o problema tem. Isso ocorre porque seu cérebro apresenta dificuldades em acionar uma parte da memória chamada funcional, cujo objetivo é trazer à mente situações vividas no passado e utilizá-las como instrumentos capazes de ajudar a encontrar saídas para as mais diversas problemáticas. Essa memória funcional parece ser bloqueada pela ativação precoce da impulsividade que, nesse tipo de pessoa, encontra-se hiperacionada.\n",


            ],
            "Sintomas secundários": [
                "\n34. Tendência a ter um desempenho profissional abaixo do esperado para sua real capacidade.\n",
                "\n35. Baixa auto-estima. Em geral o TDAH sofre desde muito cedo uma grande carga de repreensões e críticas negativas. Sem compreender o porquê disso, ele tende, com o passar do tempo, a ver-se de maneira depreciativa e passa a ter como referência pessoas externas e não ele próprio.\n",
                "\n36. Dependência química. Pode ocorrer como consequência do uso abusivo e impulsivo de drogas durante vários anos.\n",
                "\n37. Depressões frequentes. Ocorrem em geral por uma exaustão cerebral associada às frustrações provenientes de relacionamentos malsucedidos e fracassos profissionais e sociais.\n",
                "\n38. Intensa dificuldade em manter relacionamentos afetivos, conforme será visto na parte referente à dificuldade afetiva dos TDAHs.\n",
                "\n39. Demora excessiva para iniciar ou executar algum trabalho. Tais fatos ocorrem pela combinação nada produtiva de desorganização aliada a uma grande insegurança pessoal.\n",
                "\n40. Baixa tolerância ao estresse. Toda situação de estresse leva a um desgaste intenso da atividade cerebral. No caso de um cérebro TDAH, esse desgaste apresentar-se-á de maneira mais marcante.\n",
                "\n41. Tendência a apresentar um lado ”criança” que aparecerá, por toda a vida, na forma de brincadeiras, humor refinado, caprichos, pensamentos mágicos e intensa capacidade de fantasiar fatos e histórias.\n",
                "\n42. Tendência a tropeçar, cair ou derrubar objetos. Isso ocorre em função da dificuldade do TDAH de concentrar-se nos atos e de controlar ou coordenar a intensidade de seus movimentos.\n",
                "\n43. Tendência a apresentar uma caligrafia de difícil entendimento.\n",
                "\n44. Tensão pré-menstrual muito marcada. Ao que tudo indica, em função das alterações hormonais durante esse período, que intensificam os sintomas do TDAH. A retenção de líquido que ocorre durante os dias que antecedem a menstruação parece ser um dos fatores mais importantes.\n",
                "\n45. Dificuldade em orientação espacial. Encontrar o carro no estacionamento do shopping quase sempre é um desafio para um TDAH.\n",
                "\n46. Avaliação temporal prejudicada. Esperar por um TDAH pode ser algo muito desagradável, pois em geral sua noção de tempo nunca corresponde ao tempo real.\n",
                "\n47. Tendência à inversão dos horários de dormir. Em geral adormece e desperta tardiamente, por isso alguns deles acabam viciando-se em algum tipo de hipnótico.\n",
                "\n48. Hipersensibilidade a ruídos, principalmente se repetitivos.\n",
                "\n49. Tendência a exercer mais de uma atividade profissional, simultânea ou não.\n",
                "\n50. História familiar positiva para TDAH.\n",

            ]
        }
        self.respostas = {categoria: [] for categoria in self.questoes}
    
    def coletar_respostas(self):
        for categoria, perguntas in self.questoes.items():
            for pergunta in perguntas:
                while True:
                    resposta = input(f"{pergunta}(sim/nao): ").strip().lower()
                    if resposta in ["s", "n"]:
                        self.respostas[categoria].append(resposta)
                        break
                    else:
                        print("Resposta inválida. Por favor, responda com 'sim' ou 'nao'.")
                        
    def calcular_pontuacao(self):
        pontuacao = {categoria: 0 for categoria in self.questoes}
        for categoria, respostas in self.respostas.items():
            for resposta in respostas:
                if resposta == "s":
                    pontuacao[categoria] += 1
        return pontuacao
