from flask import Flask, Response, json, request
from Crypto.Cipher import DES3
from Crypto import Random
import base64

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api', methods=['GET','POST'])
def api_call():
	key = 'Sixteen byte key'
	iv = b'\xf5\x00\xd2+1J\xc5\x19'
	
	if request.headers['Content-Type'] == 'application/json':
		context = {
			"Status": "Success",
		}

		resp = Response(json.dumps(context), status=200, mimetype='application/json')
		resp.headers['Link'] = request.url

		received_json_data = request.json

		print("\n\n==========>>>>>>>>>>>>\tReceived JSON data:\n\n"+ str(received_json_data))

		encrypted_text = request.json["encrypted_text"]

		print('\n\n==========>>>>>>>>>>>>\tExtracted received Encrypted data:\n\n'+ encrypted_text)

		decoded_data = base64.b64decode(encrypted_text)

		#print('\nDecoded data: '+ decoded_data.decode())

		cipher_decrypt = DES3.new(key, DES3.MODE_OFB, iv) 
		decrypted_text = cipher_decrypt.decrypt(decoded_data)

		print('\n\n==========>>>>>>>>>>>>\tDecrypted text (WITH PADDING):\n\n%s' % decrypted_text.decode())

		decrypted_text2 = decrypted_text.decode()

		decrypted_text3 = decrypted_text2.replace('\x01','')

		print("\n\n==========>>>>>>>>>>>>\tDecrypted JSON data (WITHOUT PADDING):\n\n"+decrypted_text3)

		decrypted_text4 = json.loads(decrypted_text3)

		print("\n\n==========>>>>>>>>>>>>\tMessage in the request:\n\n"+decrypted_text4["message"])
		print('\n\n')

		#index(str(received_json_data), encrypted_text, decrypted_text.decode(), decrypted_text3, decrypted_text4["message"])
		return resp
	else:
		context = {
			"Status": "Failure",
		}
		resp = Response(json.dumps(context), status=400, mimetype='application/json')
		resp.headers['Link'] = request.url

		return resp

@app.route('/')
def index():
	return "<h1>Flask API payment page<h1>"

		
app.run()


#Sample CURL request
# curl -H "Content-Type: POST http://127.0.0.1:5000/api -d '{"encrypted_text": "2XK4ZYgAWUNb658xCZrF1WxwrMDAFMpirugE13WUPgzImoagBT1I02l79yPVYuo+nLyA1XyLz2PUbsRK9ganG9egWpA0RTr14o+L2SPT2Geokq7FH1C8WdwsvGuBPIBjf5+Wjg1ljwbmYfPxo9I0qy625QS/UBlwnIKg1tGJs5arl7ViMQjUGWvfpKyXVkJzypUozSg57Te+qsefESWDFw=="}'


