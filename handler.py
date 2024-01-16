import os
import pickle
import pandas as pd
# flask conjunto de funções para lidar com ambiente WEB
from flask             import Flask, request, Response
# importando a classe: rossman minusculo é a pasta from é o pacote e import é o nome da classe
from rossmann.Rossmann import Rossmann

# loading model
model = pickle.load( open( 'model/model_rossmann1.pkl', 'rb') )

# initialize API (passo 1)
#instancia a classe Flask
app = Flask( __name__ )

#(passo 3) define o endpoint e define o metodo post para receber métodos  que envia dados para poder receber
# e não get onde ele pede alguma coisa
@app.route( '/rossmann/predict', methods=['POST'] )
def rossmann_predict():
    #pegando o dado enviado da API
    test_json = request.get_json()
   #testando se veio dado do POST
    if test_json: # there is data!
        # converte o dado em dataframe e inicia o index =0
        if isinstance( test_json, dict): #testa se veio unico # unique example ( ou seja vem um único jason ai consegue converter em um dataframe)
            test_raw = pd.DataFrame( test_json, index=[0] )
            
        else: # multiple example ( nesse caso vem vários jason) para ser convertido em dataframe
            test_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )# test_json[0].keys() esses são os valores da coluna
            
        # Instantiate Rossmann class
        pipeline = Rossmann()
        
        # data cleaning
        df1 = pipeline.data_cleaning( test_raw )
        
        # feature engineering
        df2 = pipeline.feature_engineering( df1 )
        
        # data preparation
        df3 = pipeline.data_preparation( df2 )
        
        # prediction
        #test_raw é passado para voltar o dado original para a pessoa e df3 é o dado tranformado para fazer a predição
        df_response = pipeline.get_prediction( model, test_raw, df3 )
        
        return df_response
        
        
    else: # quando não vem dadao da requisição, identifica que não tem dado e retorna vazio
        return Reponse( '{}', status=200, mimetype='application/json' )

    #quando rodado o script o interpretador vai procurar a função main dentro do script
    # quando encontrada é rodado o flask no endpoint 0.0.0.0(localhost) (passo 2)
if __name__ == '__main__':
    port = os.environ.get('PORT',5000)
    app.run( '0.0.0.0',port=port )
