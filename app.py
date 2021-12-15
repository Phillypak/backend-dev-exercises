from flask import Flask, render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

###############################
# Gets the information from the csv file, 
# converts it into a pie chart, 
# creates png, and then sends img.
###############################
@app.route('/get_image') 
def get_image():
    csv_file = 'Records.csv'
    data = pd.read_csv(csv_file)
    countries = data['country'] # grabs country column

    pychart = data['country'].value_counts().head().plot(kind='pie', figsize = (10, 8)) # creats piechart
    pychart.set_title("Distribution by Country")

    plt.legend() # displays legend
    #plt.show()

    plt.savefig('piechart.png') # saves piechart as an image
    imgname = 'piechart.png' 
    return send_file(imgname, mimetype='image/png')

@app.route('/')
def root():
    return render_template("index.html")

app.run(host='0.0.0.0', port=5000) # runs on port 5000


##############################
# ISSUES due to time constraint
# Barebones, does not have much customization
# Could have better data visualization
##############################