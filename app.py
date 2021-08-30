from flask import Flask, request, render_template
from os import listdir
def addallconfessions():
	import pandas as pd
	# read g-sheet
	gurl = "https://docs.google.com/spreadsheets/d/1QyRJTNd1eIOxjQXzOkhHnAfEvmZGTIix45fF24ylfck/gviz/tq?tqx=out:csv&sheet=confession"
	#dataframe data
	data = pd.read_csv(gurl)
	#drop duplicates (preprocessing)
	data.drop_duplicates(subset ="confession",
                     keep = "last", inplace = True)

	data["year"].fillna("9", inplace = True)
	data['year'] = data['year'].astype(int)
	data['dept'] = data['dept'].replace(['FALSE'],['Not want to mention'])
	#preprocessing end
	data = data.reset_index(drop=True)
	
	#personNum = int(input("Enter a number"))
	f = open("templates/viewstatic.html", mode="r", encoding="utf-8")
	contents = f.readlines()
	f.close()
	print(data.head())
	print()
	print(data.tail())
	for personNum in reversed(range(len(data.index))):
		if(data["year"][personNum]==9):
    			yearc = "Not want to mention"
		namec = data["Name"][personNum]
		deptc = data["dept"][personNum]
		yearc = data["year"][personNum]

		confessionc = data["confession"][personNum]
		#print(namec,deptc,yearc,confessionc)
		str = """        
		<div class=\"row\">
		
		    <div class=\"col s12 m6 l6\">
		
		        <div class=\"card blue\">
		
		            <div class=\"card-content white-text\">
		
		                <span class=\"card-title\">To: {} </span>
		                    <span>Department: {}</span><br>
		                        <span>Year: {}</span>
		                            <p>Confession:{}</p>
		            </div>
		        </div>
		    </div>
		
		""";
		str = str.format(namec,deptc,yearc,confessionc)
		
		
		# <h1>Don't run below cells blindly </h1>
		#     <h2>Please <a href="view.html">Click Here</a></h2>
		#     <p>Notice here! CSS WIll Not work on local host</p>
		
		# In[78]:
		


		contents = list(contents)
		#this code will append html code on line no 9994
		contents.insert(999999, str)
		f = open("templates/view.html", mode="w", encoding="utf-8")
		contents = "".join(contents)
		f.write(contents)
		f.close()
	print("Done")
app = Flask(__name__)

@app.route('/index.html')
def my_form():
    return render_template('index.html')
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route("/saytoutu.html")
def saytoutu():
    return render_template('saytoutu.html')
@app.route("/reload")
def reload():
	addallconfessions()
	return "thay gayu bhai!!!!!"
@app.route("/thankyou.html")
def thankyou():
	return render_template('thankyou.html')
@app.route("/rules.html")
def rules():
    return render_template('rules.html')
@app.route("/view.html")
def view():
    return render_template('view.html')
@app.route('/', methods=['POST'])
def my_form_post():
	input_nopol = request.form['text_box']
	if request.method == 'POST':
			lines.append(input_nopol)
			print(lines)
	return render_template('index.html', nopol=input_nopol)


if __name__ == '__main__':
	app.debug = True;
	app.run()
        

