def questionario():
    marca = str(input("Qual é o nome da marca do cliente? "))
    hist = str(input("Conte uma breve história da empresa: "))
    proposito = str(input("Qual e o proposito da empresa: "))
    servico = str(input("Qual serviço é prestado pela marca? "))
    visao = str(input("Qual a visao da marca? "))
    missao = str(input("Qual é a missao da marca? "))
    valores = str(input("Qual sao os valores da marca? "))
    dic = {"historia": [marca, hist, proposito, servico, visao, missao, valores]}

    n_mod = int(input("Quantos modelos de negocios a marca utiliza:  "))
    mod_txt = str(input("Digite o valor por extenso: "))
    dic['n_Modelos'] = [n_mod, mod_txt]
    for i in range(1, n_mod + 1):
        nome = str(input(f"Qual o nome do modelo {i}? "))
        inv_inicial = str(
            input(f"Qual o valor do investimento inicial do modelo {i}? ")
        )
        inv_inicial_txt = str(
            input("Digite o valor por extenso: ")
        )
        taxa_franquia = str(
            input(f"Qual o valor da taxa inicial de franquia do modelo {i}? ")
        )
        taxa_franquia_txt = str(
            input("Digite o valor por extenso: ")
        )
        taxa_royalty = int(input("A taxa de royalties é: (% - 1 / R$ - 2) "))
        royalty = str(input(f"Qual o valor de royalties do modelo {i}? "))
        royalty_txt = str(input("Digite o valor por extenso? "))
        taxa_publicidade = int(
            input("A taxa de publicidade é: (Nenhum - 0 / % - 1 / R$ - 2) ")
        )
        publicidade = str(input(f"Qual o valor da taxa de publicidade do modelo {i}? "))
        publicidade_txt = str(input("Digite o valor por extenso? "))
        
        dic[f"Modelo{i}"] = [nome, inv_inicial, inv_inicial_txt, taxa_franquia, taxa_franquia_txt, taxa_royalty, royalty, royalty_txt, taxa_publicidade, publicidade, publicidade_txt]
    
        

    segmento = str(input("Qual e o segmento da marca? "))
    faturamento = str(input("Qual a variação de faturamento do segmento? "))
    homebased = int(input("A franquia sera homebased? (1 - Sim; 0 - Nao) - "))
    sistemaop = str(input("Qual e o sistema operacional da marca? "))
    dic["Segmento"] = [segmento, faturamento, homebased, sistemaop]

    pre_inauguracao = int(
        input("Será aplicado um treinamento pré-inauguração? (1 - Sim / 0 - Não) - ")
    )
    n_dias_treino_inic = int(
        input("Quantos dias será a duracao do treinamento inicial? ")
    )
    dias_treino_inic = str(input("Digite o valor dos dias por extenso "))
    treinamento_inic = int(
        input(
            "Qual formato do treinamento inicial? (1 - EAD / 2 - Presencial / 3 - Combinado (EAD e Presencial) - "
        )
    )
    funcionarios = int(
        input(
            "Quem fará o treinamento dos funcionários? (1 - FRANQUEADORA / 2 - FRANQUEADO) - "
        )
    )
    dic["Treinamento"] = [
        pre_inauguracao,
        n_dias_treino_inic,
        dias_treino_inic,
        treinamento_inic,
        funcionarios,
    ]

    if (
        int(
            input(
                "Alem dos servicos, sao vendidos alguns produtos? (1 - Sim / 0 - Nao) - "
            )
        )
        == 1
    ):
        produtos = str(
            input("Qual produto é vendido pela marca? - ")
        )  # Servicos prestados
    else:
        produtos = 0
    dic["Produtos"] = [produtos]

    treinamentos = [
        "Franchising e Negócios",
        "Implantação",
        "Operação",
        "Marketing e vendas",
        "Gestão",
        "Técnico",
    ]
    saida_tr = []
    for t in treinamentos:
        res = int(
            input(
                f"Sera abordado o treinamento de {t} no treinamento inicial? - (1 - Sim / 0 - Não) - "
            )
        )
        if res == 1:
            saida_tr.append(t)  # Saida com os treinamentos que serao dados
        else:
            saida_tr.append(res)
    dic["Treino_franqueadora"] = saida_tr

    manuais = [
        "Fanqueado",
        "Implantação",
        "Operações",
        "Gestão",
        "Marketing e Vendas",
    ]
    saida_ma = []
    for m in manuais:
        res = int(input(f"Será distribuido o manual {m}? (1 - Sim / 0 - Não) - "))
        if res == 1:
            saida_ma.append(m)  # Saida com os manuais que serao dados
        else:
            saida_ma.append(res)
    dic["Manuais"] = saida_ma

    layout = [
        "sugestão de arranjo físico de equipamentos e móveis",
        "memorial descritivo",
        "composição",
        "croqui",
    ]
    saida_la = []
    for l in layout:
        res = int(input(f"Será indicado os layouts de {l}? (1 - Sim / 0 - Não) - "))
        if res == 1:
            saida_la.append(l)  # Saida com os layouts que serao dados
        else:
            saida_la.append(res)
    dic["Layout"] = saida_la

    prest_ser = int(input("A franqueada presta algum serviço? (1 - Sim / 0 -  Não) - "))
    if prest_ser == 1:
        prestacao_servico = str(input("Quais serviços são prestados: "))
        dic["Prestação Serviço"] = [prest_ser, prestacao_servico]
    else:
        dic["Prestação Serviço"] = [prest_ser, 0]

    print("\nFUNCIONARIO IDEAL\n")
    funcionario_ideal = []
    criterios = [
        "os Franqueados devem ser capazes de trabalhar em conformidade com as regras e padrões estabelecidos pela Franqueadora, respeitando as estratégias, políticas e procedimentos especificados por esta ; embora se deseje que os Franqueados tenham espírito empreendedor, os Franqueados devem estar cientes de que seu ímpeto de empreendedorismo pode encontrar limitação nas regras estabelecidas pelo bem de toda a Rede de Franquias MARCA DO CLIENTE",
        "\nos Franqueados devem ser absolutamente comprometidos com o projeto MARCA DO CLIENTE, estando dispostos a trabalhar com afinco, em prol do desenvolvimento da sua unidade franqueada, dedicando-se integralmente/intensamente  à operação da sua unidade, a gerenciando de maneira empresarial;",
        "\nos Franqueados devem ter objetivos alinhados aos objetivos da Franqueadora e do projeto MARCA DO CLIENTE ; devem se identificar com a marca e, principalmente, com o seu ramo de atuação;",
        "\nos Franqueados deverão dispor de recursos financeiros próprios  e suficientes para assegurar seu sustento pessoal e a manutenção da unidade franqueada em operação, independentemente das suas expectativas de faturamento da operação franqueada, especialmente no início da sua operação ; isso pode ser determinante para a manutenção da operação durante os primeiros meses;",
        "\nos Franqueados devem apresentar 18 (dezoito) anos de idade, ou mais;",
        "\nespera-se que os Franqueados apresentem, Ensino Superior completo;",
        "\nespera-se que os Franqueados apresentem, Ensino Médio completo;",
    ]
    for i in criterios:
        res = int(input(f"{i} (1 - Obrigatoriamente / 2 - Preferencialmente) - "))
        funcionario_ideal.append(res)
    dic["Funcionario Ideal"] = funcionario_ideal

    balanco = int(
        input(
            "A empresa possui balanço financeiro dos  últimos dois exercícios?  (1- Sim / 0 - Não) - "
        )
    )
    dic["Balanço"] = balanco

    pendencias = int(
        input("A empresa possui pendências jurídicas? (1 - Sim / 0 - Não) - ")
    )
    dic["Pendência"] = pendencias

    envolvimento = int(
        input(
            "A Franqueadora exige dedicação integral à operação? (1 - Sim / 0 - Não) - "
        )
    )
    dic["Envolvimento"] = envolvimento

    print("\nUNIDADES EM OPERAÇÃO\n")
    localidade = {}
    endereco = int(input("Existem quantos endereços registrados? "))
    for i in range(endereco):
        cadastro = [
            str(input(f"Digite o {n}: ")) for n in ["Endereco", "Tel", "Pessoa"]
        ]
        localidade[i + 1] = cadastro
    dic["Localidade"] = localidade

    print("\nLIMITES TERRITORIAIS\n")
    crit_ter = int(
        input(
            "Qual criterio de delimitacao de territorio sera usado? (1 - Territorio / 2 - Raio) - "
        )
    )
    raio = str(input("Digite o raio de delimitacao: ")) if crit_ter == 2 else 0
    raio_txt = str(input("Digite o valor por extenso: ")) if crit_ter == 2 else 0
    pref = [
        int(input(f"Digite se existira {f} (1 - Sim / 0 - Nao) - "))
        for f in ["Exclusividade", "Preferencia"]
    ]
    dic["Território"] = [crit_ter, raio, raio_txt, pref]

    print("\nECOMMERCE\n")
    ecommerce = int(
        input(
            "E-commerce : (1 - Proibido / 2 - Proibido, exceto delivery / 3 - Permitido) - "
        )
    )
    website = int(input("Criacao de website: (1 - Sim / 0 - Nao) "))
    perfis = int(
        input("Autorizacao na criacao de perfis em rede social: (1 - Sim / 0 - Nao) - ")
    )
    retirada_produtos = int(
        input("Havera retirada de produtos da franqueadora? (1 - Sim / 0 - Nao) - ")
    )
    dic["Ecommerce"] = [ecommerce, website, perfis, retirada_produtos]

    print("\nINPI\n")
    n_processos_inpi = int(input("Digite o número de processos ingressados no INPI? "))
    inpi = []
    for _ in range(n_processos_inpi):
        processo = [
            str(input(f"Digite o {n}: "))
            for n in ["Numero do processo do INPI", "Status do processo"]
        ]
        inpi.append(processo)
    dic["INPI"] = inpi

    print("\nHERANCA\n")
    falecimento = int(
        input(
            "Em caso de falecimento, a Franquia sera: (1 - Extinta / 2 - Transferida ao herdeiro) - "
        )
    )
    dic["Herança"] = falecimento

    return dic
