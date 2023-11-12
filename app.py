from flask import Flask, redirect, render_template, request, session
import pandas as pd
import pickle
import numpy as np

model = pickle.load(open('./new_pickle.pkl','rb'))

brand = {'Ambassador Classic': 0,'Audi A3': 1,'Audi A4': 2,'Audi A6': 3,'Audi A7': 4,'Audi A8': 5,'Audi Q3': 6,'Audi Q5': 7,
 'Audi Q7': 8,'Audi RS5': 9,'Audi TT': 10,'BMW 1': 11,'BMW 3': 12,'BMW 5': 13,'BMW 6': 14,'BMW 7': 15,'BMW X1': 16,'BMW X3': 17,
 'BMW X5': 18,'BMW X6': 19,'BMW Z4': 20,'Bentley Continental': 21,'Chevrolet Aveo': 22,'Chevrolet Beat': 23,'Chevrolet Captiva': 24,
 'Chevrolet Cruze': 25,'Chevrolet Enjoy': 26,'Chevrolet Optra': 27,'Chevrolet Sail': 28,'Chevrolet Spark': 29,'Chevrolet Tavera': 30,
 'Datsun GO': 31,'Datsun Redi': 32,'Datsun redi-GO': 33,'Fiat Avventura': 34,'Fiat Grande': 35,'Fiat Linea': 36,'Fiat Punto': 37,
 'Force One': 38,
 'Ford Aspire': 39,
 'Ford Classic': 40,
 'Ford EcoSport': 41,
 'Ford Ecosport': 42,
 'Ford Endeavour': 43,
 'Ford Fiesta': 44,
 'Ford Figo': 45,
 'Ford Freestyle': 46,
 'Ford Fusion': 47,
 'Ford Ikon': 48,
 'Ford Mustang': 49,
 'Honda Accord': 50,
 'Honda Amaze': 51,
 'Honda BR-V': 52,
 'Honda BRV': 53,
 'Honda Brio': 54,
 'Honda CR-V': 55,
 'Honda City': 56,
 'Honda Civic': 57,
 'Honda Jazz': 58,
 'Honda Mobilio': 59,
 'Honda WR-V': 60,
 'Honda WRV': 61,
 'Hyundai Accent': 62,
 'Hyundai Creta': 63,
 'Hyundai EON': 64,
 'Hyundai Elantra': 65,
 'Hyundai Elite': 66,
 'Hyundai Getz': 67,
 'Hyundai Grand': 68,
 'Hyundai Santa': 69,
 'Hyundai Santro': 70,
 'Hyundai Sonata': 71,
 'Hyundai Tucson': 72,
 'Hyundai Verna': 73,
 'Hyundai Xcent': 74,
 'Hyundai i10': 75,
 'Hyundai i20': 76,
 'ISUZU D-MAX': 77,
 'Isuzu MUX': 78,
 'Jaguar F': 79,
 'Jaguar XE': 80,
 'Jaguar XF': 81,
 'Jaguar XJ': 82,
 'Jeep Compass': 83,
 'Lamborghini Gallardo': 84,
 'Land Rover': 85,
 'Mahindra Bolero': 86,
 'Mahindra KUV': 87,
 'Mahindra Logan': 88,
 'Mahindra NuvoSport': 89,
 'Mahindra Quanto': 90,
 'Mahindra Renault': 91,
 'Mahindra Scorpio': 92,
 'Mahindra Ssangyong': 93,
 'Mahindra TUV': 94,
 'Mahindra Thar': 95,
 'Mahindra Verito': 96,
 'Mahindra XUV300': 97,
 'Mahindra XUV500': 98,
 'Mahindra Xylo': 99,
 'Maruti 800': 100,
 'Maruti A-Star': 101,
 'Maruti Alto': 102,
 'Maruti Baleno': 103,
 'Maruti Celerio': 104,
 'Maruti Ciaz': 105,
 'Maruti Dzire': 106,
 'Maruti Eeco': 107,
 'Maruti Ertiga': 108,
 'Maruti Esteem': 109,
 'Maruti Grand': 110,
 'Maruti Ignis': 111,
 'Maruti Omni': 112,
 'Maruti Ritz': 113,
 'Maruti S': 114,
 'Maruti S-Cross': 115,
 'Maruti SX4': 116,
 'Maruti Swift': 117,
 'Maruti Versa': 118,
 'Maruti Vitara': 119,
 'Maruti Wagon': 120,
 'Maruti Zen': 121,
 'Mercedes-Benz A': 122,
 'Mercedes-Benz B': 123,
 'Mercedes-Benz C-Class': 124,
 'Mercedes-Benz CLA': 125,
 'Mercedes-Benz CLS-Class': 126,
 'Mercedes-Benz E-Class': 127,
 'Mercedes-Benz GL-Class': 128,
 'Mercedes-Benz GLA': 129,
 'Mercedes-Benz GLC': 130,
 'Mercedes-Benz GLE': 131,
 'Mercedes-Benz GLS': 132,
 'Mercedes-Benz M-Class': 133,
 'Mercedes-Benz New': 134,
 'Mercedes-Benz R-Class': 135,
 'Mercedes-Benz S': 136,
 'Mercedes-Benz S-Class': 137,
 'Mercedes-Benz SL-Class': 138,
 'Mercedes-Benz SLC': 139,
 'Mercedes-Benz SLK-Class': 140,
 'Mini Clubman': 141,
 'Mini Cooper': 142,
 'Mini Countryman': 143,
 'Mitsubishi Cedia': 144,
 'Mitsubishi Lancer': 145,
 'Mitsubishi Montero': 146,
 'Mitsubishi Outlander': 147,
 'Mitsubishi Pajero': 148,
 'Nissan Evalia': 149,
 'Nissan Micra': 150,
 'Nissan Sunny': 151,
 'Nissan Teana': 152,
 'Nissan Terrano': 153,
 'Nissan X-Trail': 154,
 'Porsche Boxster': 155,
 'Porsche Cayenne': 156,
 'Porsche Panamera': 157,
 'Renault Captur': 158,
 'Renault Duster': 159,
 'Renault Fluence': 160,
 'Renault KWID': 161,
 'Renault Koleos': 162,
 'Renault Lodgy': 163,
 'Renault Pulse': 164,
 'Renault Scala': 165,
 'Skoda Fabia': 166,
 'Skoda Laura': 167,
 'Skoda Octavia': 168,
 'Skoda Rapid': 169,
 'Skoda Superb': 170,
 'Skoda Yeti': 171,
 'Tata Bolt': 172,
 'Tata Hexa': 173,
 'Tata Indica': 174,
 'Tata Indigo': 175,
 'Tata Manza': 176,
 'Tata Nano': 177,
 'Tata New': 178,
 'Tata Nexon': 179,
 'Tata Safari': 180,
 'Tata Sumo': 181,
 'Tata Tiago': 182,
 'Tata Tigor': 183,
 'Tata Venture': 184,
 'Tata Xenon': 185,
 'Tata Zest': 186,
 'Toyota Camry': 187,
 'Toyota Corolla': 188,
 'Toyota Etios': 189,
 'Toyota Fortuner': 190,
 'Toyota Innova': 191,
 'Toyota Platinum': 192,
 'Toyota Qualis': 193,
 'Volkswagen Ameo': 194,
 'Volkswagen Beetle': 195,
 'Volkswagen CrossPolo': 196,
 'Volkswagen Jetta': 197,
 'Volkswagen Passat': 198,
 'Volkswagen Polo': 199,
 'Volkswagen Tiguan': 200,
 'Volkswagen Vento': 201,
 'Volvo S60': 202,
 'Volvo S80': 203,
 'Volvo V40': 204,
 'Volvo XC60': 205,
 'Volvo XC90': 206}

location ={'Ahmedabad': 0,'Bangalore': 1,'Chennai': 2,'Coimbatore': 3,'Delhi': 4,'Hyderabad': 5,'Jaipur': 6,'Kochi': 7,
 'Kolkata': 8,'Mumbai': 9,'Pune': 10}

owner = {'First': 0, 'Fourth & Above': 1, 'Second': 2, 'Third': 3}

transmission = {'Automatic': 0, 'Manual': 1}

fuel_type = {'CNG': 0, 'Diesel': 1, 'LPG': 2, 'Petrol': 3}

app = Flask(__name__,template_folder='templates')

# server = app.server

@app.route('/')
def home():
     return render_template('index.html')

@app.route('/predict.html/')
def predict():
	return render_template("predict.html")  

@app.route('/predict.html',methods=['POST','GET'])
def prediction():
	#a=request.form['g']
	#return a
	try:
		features=["1","2","3","4","5","6","7","8"]
		int_features=[]
		for i in features:
				#a=request.form.get(i)
				if i in "1":
					int_features.append(brand[request.form.get(i)])

				elif i in "2":
					int_features.append(location[request.form.get(i)])

				elif i in "3":
					int_features.append(fuel_type[request.form.get(i)])

				elif i in "4":
					int_features.append(transmission[request.form.get(i)])	

				elif i in "5":
					int_features.append(owner[request.form.get(i)])			
				else:
					# print("else",request.form.get(i))
					int_features.append(request.form.get(i))
				
		print(int_features)
		int_features = list(map(int,int_features))
		#final_features = [np.array(int_features)]

		# trial = [23,1,3,1,2,2012,37000,18]
		# print(trial)
		prediction = model.predict([int_features])
		output=str(prediction[0])
		#output = model.predict([[0,61,3,1,30,0,0,1,0,225,150,95,28.8,65,103]])
		#output=str(output)
		#return redirect(url_for('success',output=age1))
		#return output
	except Exception as msg:
		print("NO value : ",msg)
	return render_template("predict.html" ,prediction_value='The Recommend value is {} Lakh'.format(round(float(output),2)))

if __name__ == '__main__':
    app.run(debug=True,threaded=True)