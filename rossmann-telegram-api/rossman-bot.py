import requests
import json
import pandas as pd
from flask import Flask,request,Response

#constants
TOKEN = '5518514255:AAHipZkI9Hcic3qN0bcSHEURZD9e74cYQv8';

#Info about BOT
#https://api.telegram.org/bot5518514255:AAHipZkI9Hcic3qN0bcSHEURZD9e74cYQv8/getMe

# ger updates
#https://api.telegram.org/bot5518514255:AAHipZkI9Hcic3qN0bcSHEURZD9e74cYQv8/getUpdates

# ger updates
#https://api.telegram.org/bot5518514255:AAHipZkI9Hcic3qN0bcSHEURZD9e74cYQv8/sendMessage?chat_id=1369304880&text=Hi Felipe!

def send_message (chat_id, text):
	url = 'https://api.telegram.org/bot{}/'.format(TOKEN)
	url = url + 'sendMessage?chat_id={}'.format(chat_id)
	
	requests.post(url,json ={'text':text})
	print ('Status Code {}'.format(r.status_code))
	
	return None

def load_dataset(store_id):
	# loading test dataset
	df10 = pd.read_csv( '/home/felipe/Documents/DS_em_Producao/ds_em_producao/data/test.csv' )
	df_store_raw = pd.read_csv('/home/felipe/Documents/DS_em_Producao/ds_em_producao/data/store.csv' )

	# merge test dataset + store .O arquivo test tem apenas a performance das lojas , o arquivo store tem a caracteristica das lojas
	df_test = pd.merge( df10, df_store_raw, how='left', on='Store' )

	# choose store for prediction escolhendo algumas lojas para fazer a previsão e não  todas
	df_test = df_test[df_test['Store']== store_id ]

	if not df_test.empty:
		
		# remove closed days removendo as linhas onde as lojas estão fechadas pois não ajuda na predição
		df_test = df_test[df_test['Open'] != 0]
		df_test = df_test[~df_test['Open'].isnull()]
		df_test = df_test.drop( 'Id', axis=1 ) #id não usa pra nada

		# convert Dataframe to json
		data = json.dumps( df_test.to_dict( orient='records' ) ) # orientação records cada linha é um jason e o arquivo final é uma lista de jsons
	else:
		data = 'error'	
	return data


def predict(data):
	# API Call
	url = 'https://rossmann-model-test-fhs.herokuapp.com/rossmann/predict'
	#indica o tipo de dado que está recebendo
	header = {'Content-type': 'application/json' } 
	data = data

	r = requests.post( url, data=data, headers=header )
	print( 'Status Code {}'.format( r.status_code ) )

	d1 = pd.DataFrame( r.json(), columns=r.json()[0].keys() )
	return d1

def parse_message(message):
	chat_id = message['message']['chat']['id']
	store_id = message['message']['text']
	store_id = store_id.replace('/','')
	
	try:
		store_id = int(store_id)
	except ValueError:
			
		store_id = 'error'
	
	return chat_id,store_id

#API Initialize	
app = Flask(__name__)	
@app.route('/',methods=['GET','POST'])
def index():
	if request.method =='POST':
		message = request.get_json()
		chat_id,store_id = parse_message(message)
		if store_id !='error':
			#loading data
			data = load_dataset(store_id)
			if data != 'error':
				#prediction
				d1=predict(data)
				#calculation
				
				#soma do que será vendido ao final das 6 semanas
				d2 = d1[['store', 'prediction']].groupby( 'store' ).sum().reset_index()

				msg = 'Store Number {} will sell R${:,.2f} in the next 6 weeks'.format( 
						    d2.loc[i, 'store'], 
						    d2.loc[i, 'prediction'] )
				send_message(chat_id,msg)
				return Response ('Ok', status=200)
				
				#send message
			else:
				send_message(chat_id,'Store not available')
				return Response('Ok',status=200)
					
		else:
			send_message(chat_id,'Store ID is Wrong')
			return Response('Ok',status=200) #sempre que mandar msg mandar o status para a API não ficar rodando o tempo todo a espera de resposta	
		
	else:
		return '<h1> Rossmann Telegram BOT </h1>'	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
	
	
	
	

