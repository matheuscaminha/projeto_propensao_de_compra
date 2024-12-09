# Projeto de propenção de compra (Learn to Rank)

<img src="img\Sales-acquisition-1.png" width=800px height=350px>

# 1. Descrição
- O objetivo desse projeto foi o de implementar um <b> modelo de classificação </b> que possibilite <b>rankear</b> os clientes de uma base de dados de uma seguradora que oferta seguros de saúde, para que a mesma possa aborda-los de maneira mais eficiente a fim de oferecer um novo produto de seguros de carro. 
- O dataset utilizado já se encontra limpo e livre de valores nulos e possui as seguintes features:

Variável | Definição
------------ | -------------
|Id| Identificador único do cliente.|
|Gender| Gênero do cliente.|
|Age| Idade do cliente.|
|Driving License| 0, o cliente sem habilitação e 1, o cliente com habilitação |
|Region Code| Código da região do cliente.|
|Previously Insured| 0, o cliente sem seguro de automóvel e 1, o cliente com seguro de automóvel.|
|Vehicle Age| Idade do veículo.|
|Vehicle Damage| 0, cliente que nunca teve seu veículo danificado no passado e 1, cliente já teve seu veículo danificado no passado.|
|Anual Premium| Valor do custo do cliente pelo seguro de saúde anual.|
|Policy sales channel| código do canal de contato com o cliente.|
|Vintage| número de dias que o cliente se associou à empresa através da compra do seguro de saúde.|
|Response| 0, o cliente não tem interesse e 1, o cliente tem interesse.| 

- Foi performada uma <b>Análise exploratória de dados</b> a fim de gerar <b>insights chave</b> para performance do negócio, além de melhorar o entendimento sobre o dataset.
- Após isso os dados foram preparados por meio de <b>Encoding, Rescalling e Normalização</b>. E foi aplicado um modelo <b>Random Forest Classifier</b> para identificar as <b>principais fetures</b> que serão benéficas para o treinamento do modelo e filtra-las.
- Com as features definidas, foi realizado um ensaio com <b>quatro diferentes modelos</b> a fim de definir qual deles teria a melhor performance. Para tanto as principais métricas levadas em consideração foram as <b>curvas de Gain e Lift, além da Precisão e do Recall</b>.
- Por fim, com o modelo definido e treinado foi colocado em produção com a construção de uma <b>API em Flask</b> que foi utilizada para atribuir um valor de propenção para cada cliente dentro de uma planilha no <b>Google sheets</b>.

# 2. Tecnologias e ferramentas
As tecnologias e ferraementas utilizadas foram Pyhton (Pandas, Numpy, Seaborn, Scikit-learn, Pickle, Flask), Jupyer Notebook, Pyenv, Git and Github (controle de versão), algorítimos de machine learning para classificação, estatística e VsCode.

# 3. Estrutura do projeto
Cada arquivo/pasta contém os seguintes conteúdos:

<b>Data:</b> Contém os arquivo de treino e teste no formato .csv.

<b>Notebooks:</b><br>
- notebook.ipynb: Contém todos os passos do projeto descrito na primeira sessão.

<b>Reports:</b> Contém imagens e pdf's úteis para análises.

<b>Models:</b> Contém os modelos pré-treinados, assim como os parametros para Rescalling serializados.

<b>Requirements, setup, gitignore, readme:</b> O arquivo setup.py me permite construir todo o meu projeto como um pacote, contendo metadados e assim por diante. Além disso, o arquivo requirements.txt lista todas as dependências necessárias para o projeto com as versões específicas para garantir a reprodução. O arquivo .gitignore me permite esconder informações irrelevantes dos commits e estou usando o arquivo readme.md para documentação e storytelling.

# 4. Problema de negócio e objetivos do projeto

Problema de negócio:
- Uma seguradora que trabalha principalmente com seguros de saúde pretende lançar um novo produto de seguro para carros. Para tanto, a mesma realizou uma pesquisa de mercado com sua base de clientes e agora pretende abordar uma nova base com uma campanha de marketing direcionada a fim de oferecer seu novo produto.
- A campanha irá ter como sua principal ferramenta a prática do cold calling e o time de dados devará fornecer uma base de clientes ordenada por aqueles com maior probabilidade de aderirem ao seguro de carro a fim de maximizar os resutlados obtidos, já que o time comercial só conseguirá realizar cerca de 20 mil contatos durante a campanha.

Considerando o que foi mencionado acima, os <b> objetivos do projeto </b> são:

1. Explorar a base de dados fornecida pela pesquisa de mercado a fim de encontrar e solucionar erros, além de gerar insights importantes para o negócio.
2. Tratar os dados e testar diferentes features e modelos para garantir um melhor modelo final.
3. Realizar o deploy do modelo de forma que a equipe de vendas consiga carregar os dados e obter um retorno do modelo de forma simples e rápida em uma ferramenta que seja familiar para a equipe. 

# 5. Pipeline da solução
A seguinte <b>pipeline</b> foi usada, baseada no framework <b>CRISP-DM</b>:

1. Entendimento inicial e limpeza dos dados
2. Feature engeneering
3. Filtragem de dados
4. EDA (Análise exploratória dos dados)
5. Preparação dos dados para treino
6. Seleção de features
7. Teste com diferentes modelos
8. Treino e validação do modelo final
9. Deploy do modelo em produção

# 6. EDA & Modelagem

1. Limpeza e feature engeneering:
    
    - Os dados do dataset já se encontravam sem dados faltantes e com a correta tipagem.
    - A feature vehicle_age foi transformada a fim de eliminar caracteres especiais.
    - A feature vehiicle_damage foi tranformada em uma feature binária.

2. EDA:

- Analisando o dataset foram observados os seguintes relacionamentos com a variável resposta:
    - A feature idade influência positivamente o interesse em seguros de carro, já que pessoas mais velhas tem maior interesse.

        <img src="reports\age_boxplot.png" width=300px height=250px>

    - Aproximadamente 87% das pessoas que possuem habilitação não tem interesse em seguro de carro.

        <img src="reports\driving_license_responde.png" width=300px height=250px>

    - Existe uma distribuição próxima da normal para quanto as pessoas gastam com o seguro de saúde, porém isso não impacta no interesse ou não em seguro de carros, portatno essa provavelmente não será uma feature importante para o modelo.

        <img src="reports\annual_premium_response.png" width=700px height=300px>
    
    - Homens apresentaram um interesse ligeiramente maior em seguros do que mulheres.

        <img src="reports\gender_response.png" width=300px height=250px>
        
    - Levando em consideração que a média de respostas positivas em cada região é de 10% e o desvio padrão é cerca de 3.39%, existem 7 regiões que apresentam respostas acima desse desvio, podendo essa ser uma boa variável decriminatória para o modelo.

        <img src="reports\perc_response_by_region.png" width=700px height=350px>

    - Levando em consideração que a média de respostas positivas para cada canal de vendas é de 11.1% e o desvio padrão é cerca de 9.28%, existem 24 canais que apresentam respostas acima desse desvio, também representando uma possível boa variável para o treino do modelo.

        <img src="reports\sales_cahnnel_response.png" width=900x height=350px>

    - A variável idade do carro também contribuiu positivamente para a variável resposta, sendo que donos de carros mais velhos tem maior interesse no seguro.

        <img src="reports\vehicle_age_response.png" width=350px height=300px> 

    - A variável que indica se o cliente já possui ou não alguma seguro tera que ser removida do treinamento devido a ter uma corelação muito alta com a variável resposta.
    
        <img src="reports\previously_insured_response.png" width=350px height=300px>

    - Por fim, a variável vintage demonstra que os clientes estão distribuiudos de forma homogenea independente das respostas, o que provavelmente a torna uma variável que não irá contribuir para o treinamneto do modelo.

        <img src="reports\vintage_response.png" width=700px height=300px>


# 7. Machine learning

1. Preparação dos dados

- O dataset de treino foi dividido entre dois, na proporção de 2:10, para validação e treino respectivamente.
- A variável annual_premium foi <b> normalizada </b> devido a sua distribuição próxima a normal.
- As variáveis age e vintage foram <b> re-escaladas </b> utilizando <b> MinMaxScaler </b> pois não possuem muitos outliers.
- As variáveis gender e region_code foram transformadas utilizando <b> target encoding </b>.
- Para a variável vehicle_age foi utilizado <b> OneHotEncoding </b> devido ao baixa quantidade de valores
- Por fim para variável policy_sales_channel foi realizado <b> FrequencyEncoding </b>.

2. Feature selection

- Com os dados padronizados, foi treinado um modelo utilizando <b> ExtraTreesClassifier </b> a fim de se utilizar da função <b> feature_importances </b> para definir quais as variáveis mais relevantes para o modelo.

    <img src="reports\feature_importances.png" width=400px height=500px>

- Com base no gráfico foram selecionadas as features que obtiveram uma relevância maior que 0.05, a não ser a variável previously insured, já que essa apresentou muita corelação com a variável resposta.

3. Machine learning

- A seguir, para efeitos de comparação, foram treinados 4 modelos diferentes a fim de identificar algum que gere resultados mais satisfatórios. Os modelos treinados foram <b> KNN, LogisticRegression, ExtraTreesClassifier e RandomForestClassifier </b>.
- O modelo final escolhido foi decidido baseado na comparação entre os gráficos de curva de <b> Cumulative gain e Lift </b>, assim como com base nas métricas de precision e recall no ponto de 20000 chamadas estabaelecido pelo problema de negócios, os resultados obtidos para cada modelo foram:

    - KNN:

        <img src="reports\knn_curves.png" width=750px height=300px>

    - Logistic Regression:

        <img src="reports\log_curves.png" width=750px height=300px>

    - Extra Trees Classifier:

        <img src="reports\extra_curves.png" width=750px height=300px>

    - Random Forrest Classifier  

        <img src="reports\rf_curves.png" width=750px height=300px>

    - Precision & Recall com 20000 ligações:

        Modelo | Precisão | Recall
        ------------ | ------------- | -------------
        KNN | 28.53% | 62.40%
        Logistic Regression | 27.05% | 58.21%
        Extra Trees Classifier | 28.84% | 62.05%
        Random Forest Classifier | 28.84% | 62.05%


# 8. Modelo Final & Resultados obtidos

1. Modelo final e Fine Tunning:

- O modelo escolhido com base na análise gráfica e, principalmente, em relação as métricas de precision e recall foi o modelo <b> Random Forest Classifier </b>.
- A seguir os hiperparametros do modelo foram ajustado utilizando <b> BeayesSearhCV </b> a fim de identificar os melhores valores para cada um.
- Mesmo após a tunagem dos hyperparametros o modelo ainda assim continuou com os mesmos resultados.

2. Resultados obtidos

    <img src="reports\rf_curves.png" width=750px height=300px>

-  Considerando que ao realizarmos os 20 mil contatos dentro da base de validação estamos abordando cerca de 26.24% dessa mesma base, o modelo nos permite atingir, segundo a curva de Cumulative Gain, 64.55% dos contatos que tem interesse em seguros para carro. Isso representa que, ao utilizar o modelo, a eficiencia desses contatos é 2.46 x maior do que a baseline estabelecida, segundo a curva de Lift.


# 9. Deploy do modelo em produção

 - O deploy do modelo foi possibilitado por meio de uma API simples construida em flask, essa API será acessada pelos colaboradores responsáveis pelas ligações via Google Sheets, já que essa é uma ferramena amplamente utilizada nesse ambiente.
 
Passo a passo:

1. Foi criada uma classe contendo as funções necessárias para limpeza, criação de features, preparação e predição dos dados fornecidos pelos colaboradores via Google sheets.


# 10. Contact me
<b>Linkedin:</b> https://www.linkedin.com/in/matheus-wilhelms-85455a175/

<b>Github:</b> https://github.com/matheuscaminha

<b>Gmail:</b> matheus-caminha@hotmail.com
