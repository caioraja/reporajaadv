def questionario():
    cof = int(input("Essa COF é: (1 - Serviço / 2 - Produtos) "))

    marca =str(input("Qual é o nome da marca do cliente? "))
    hist = str(input("Conte uma breve história da empresa: "))
    proposito = str(input("Qual e o proposito da empresa: "))
    servico = str(input("Qual serviço é prestado pela marca? "))
    visao = str(input("Qual a visao da marca? "))
    missao = str(input("Qual é a missao da marca? "))
    valores = str(input("Qual sao os valores da marca? "))
    historia = [marca, hist, proposito, servico, visao, missao, valores]

    modelos = int(input("Quantos modelos de negocios a marca utiliza:  "))    
    segmento = str(input("Qual e o segmento da marca? "))
    faturamento = str(input("Qual a variação de faturamento do segmento? "))
    unidades = str(input("Qual a variação da quantidade de novas unidades do segmento? "))
    homebased = int(input("A franquia sera homebased? (1 - Sim; 0 - Nao) - "))
    sistemaop = str(input("Qual e o sistema operacional da marca? "))
    modelo = [modelos, segmento, faturamento, unidades, homebased, sistemaop]

    def _perguntas_treinamento(arg0, arg1, arg2, arg3, arg4):
        pre_inauguracao = int(input(arg0))
        n_dias_treino_inic = int(input(arg1))
        dias_treino_inic = str(input(arg2))
        treinamento_inic = int(input(arg3))
        funcionarios = int(input(arg4))
        return [
            pre_inauguracao,
            n_dias_treino_inic,
            dias_treino_inic,
            treinamento_inic,
            funcionarios,
        ]

    def _perguntas_ecommerce(arg0, arg1, arg2, arg3):
        ecommerce = int(input(arg0))
        website = int(input(arg1))
        perfis = int(input(arg2))
        retirada_produtos = int(input(arg3))
        return [ecommerce, website, perfis, retirada_produtos]


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

    
    

    treinamentos = [
        "Franchising e Negocios",
        "Implantacao",
        "Operacao",
        "Marketing e vendas",
        "Gestao",
        "Tecnico",
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

    treinamento = _perguntas_treinamento(
        "Será aplicado um treinamento pré-inauguração? (1 - Sim / 0 - Não) - ",
        "Quantos dias será a duracao do treinamento inicial? ",
        "Digite o valor dos dias por extenso ",
        "Qual formato do treinamento inicial? (1 - EAD / 2 - Presencial / 3 - Combinado (EAD e Presencial) - ",
        "Quem fará o treinamento dos funcionários? (1 - FRANQUEADORA / 2 - FRANQUEADO) - ",
    )

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
            saida_la.append(m)  # Saida com os layouts que serao dados

    prest_ser = int(input("A franqueada presta algum serviço? (1 - Sim / 0 -  Não) - "))
    if prest_ser == 1:
        prestacao_servico = str(input("Quais serviços são prestados: "))

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

    balanco = int(
        input(
            "A empresa possui balanço financeiro dos  últimos dois exercícios?  (1- Sim / 0 - Não) - "
        )
    )
    pendencias = int(
        input("A empresa possui pendências jurídicas? (1 - Sim / 0 - Não) - ")
    )
    envolvimento = int(
        input(
            "A Franqueadora exige dedicação integral à operação? (1 - Sim / 0 - Não) - "
        )
    )

    print("\nINVESTIMENTOS\n")
    for i in range(1, modelos + 1):
        pass
    inv_inicial = []
    taxa_franquia = []
    taxa_royalties = []
    taxa_marketing = []
    inv = 1
    tx_ini = 1
    tx_ro = 1
    tx_ma = 1
    nu_inv = ""
    nu_ini = ""
    nu_ro = ""
    nu_ma = ""

    while True:
        inv = str(input("Digite o investimento inicial do modelo? (0 para sair) - "))
        if inv == "0":
            break
        nu_inv = str(input("Digite o mesmo valor por extenso: "))
        tx_ini = str(input("Digite o o valor da taxa inicial do modelo? - "))
        nu_ini = str(input("Digite o mesmo valor por extenso: "))
        tx_ro = str(
            input(
                "Digite o o valor da taxa de royalties do modelo? (0 caso n seja cobrada) - "
            )
        )
        nu_ro = str(input("Digite o mesmo valor por extenso: "))
        tx_ma = str(
            input(
                "Digite o o valor da taxa de marketing do modelo? (0 caso n seja cobrada) - "
            )
        )
        nu_ma = str(input("Digite o mesmo valor por extenso: "))

        inv_inicial.append([inv, nu_inv])
        taxa_franquia.append([tx_ini, nu_ini])
        taxa_royalties.append([tx_ro, nu_ro])
        taxa_marketing.append([tx_ma, nu_ma])

    modelo_taxa = []
    for i in ["taxa de royalty", "taxa de marketing"]:
        res = int(input(f"Qual ser a o modelo de cobranca da {i} (1 - %, 2 - R$) - "))
        modelo_taxa.append(res)

    seguro = str(input("Digite o valor do seguro? (0 caso n seja pedido seguro) - "))

    aluguel_equip = int(
        input("E cobrado algum aluguel de equipamento? (1 - Sim / 0 - Não) - ")
    )

    print("\nUNIDADES EM OPERAÇÃO\n")
    localidade = {}
    i = 1
    while int(input("Existe algum endereço registrado (1 - Sim / 0 - Não) ")) != 0:
        cadastro = [
            str(input(f"Digite o {n}: ")) for n in ["Endereco", "Tel", "Pessoa"]
        ]
        localidade[i] = cadastro
        crit = int(input("Deseja continuar? (1 - Sim / 0 - Nao) - "))
        if crit == 0:
            break
        i += 1

    print("\nLIMITES TERRITORIAIS\n")
    crit_ter = int(
        input(
            "Qual criterio de delimitacao de territorio sera usado? (1 - Territorio / 2 - Raio) - "
        )
    )
    raio = str(input("Digite o raio de delimitacao: ")) if crit_ter == 2 else 0
    pref = [
        int(input(f"Digite se existira {f} (1 - Sim / 0 - Nao) - "))
        for f in ["Exclusividade", "Preferencia"]
    ]

    print("\nECOMMERCE\n")
    perguntas_ecommerce = _perguntas_ecommerce(
        "E-commerce : (1 - Proibido / 2 - Proibido, exceto delivery / 3 - Permitido) - ",
        "Criacao de website: (1 - Sim / 0 - Nao) ",
        "Autorizacao na criacao de perfis em rede social: (1 - Sim / 0 - Nao) - ",
        "Havera retirada de produtos da franqueadora? (1 - Sim / 0 - Nao) - ",
    )
    n_processos_inpi = int(input("Digite o número de processos ingressados no INPI? "))
    inpi = []
    for i in range(n_processos_inpi):
        processo = [
            str(input(f"Digite o {n}: "))
            for n in ["Numero do processo do INPI", "Status do processo"]
        ]
        inpi.append(processo)
    print("\nHERANCA\n")
    falecimento = int(
        input(
            "Em caso de falecimento, a Franquia sera: (1 - Extinta / 2 - Transferida ao herdeiro) - "
        )
    )

    return [
        cof,
        historia,
        produtos,
        modelo,
        saida_tr,
        treinamento,
        saida_ma,
        saida_la,
        prest_ser,
        funcionario_ideal,
        balanco,
        pendencias,
        envolvimento,
        inv_inicial,
        taxa_franquia,
        taxa_royalties,
        taxa_marketing,
        modelo_taxa,
        seguro,
        aluguel_equip,
        localidade,
        crit_ter,
        raio,
        pref,
        perguntas_ecommerce,
        n_processos_inpi,
        inpi,
        falecimento,
    ]
