import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def FortYatesBS():
    data = pd.read_csv('Fort Yates Avg Bare Soil Temp.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Bare Soil Temperature for Mesonet Fort Yates County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()

def FortYatesWC():
    data = pd.read_csv('Fort Yates Avg Wind Chill.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Wind Chill for Mesonet Fort Yates County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()
   
def FortYatesPENPET():
    data = pd.read_csv('Fort Yates Avg Penman PET.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Penman PET for Mesonet Fort Yates County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Inches')
   
    plt.show()
   
def FortYatesTSP():
    data = pd.read_csv('Fort Yates Avg Turf Temp.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Turf Soil Temperature for Mesonet Fort Yates County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()
   
def FortYatesMaxT():
    data = pd.read_csv('Fort Yates MaxTemp.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Maximum Temperature for Mesonet Fort Yates County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()
   
def FortYatesWS():
    data = pd.read_csv('Fort Yates Avg Wind Speed.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Wind Speed for Mesonet Fort Yates County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Miles Per Hour')
   
    plt.show()
   
def FortYatesAT():
    data = pd.read_csv('Fort Yates Total Penman PET.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Total Penman PET for Mesonet Fort Yates County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Inches')
   
    plt.show()
   
def FortYatesMWS():
    data = pd.read_csv('Fort Yates Max Wind Speed.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Maximum Wind Speed for Mesonet Fort Yates County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Miles Per Hour')
   
    plt.show()
   
def FortYatesMinT():
    data = pd.read_csv('Fort Yates MinTemp.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Minimum Temperature for Mesonet Fort Yates County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()
   
def FortYatesAT():
    data = pd.read_csv('Fort Yates AvgTemp.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Temperature for Mesonet Fort Yates County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()
   
def FortYatesDP():
    data = pd.read_csv('Fort Yates Avg Dew Point.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Dew Point for Mesonet Fort Yates County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()
   
def FortYatesTSR():
    data = pd.read_csv('Fort Yates Total Solar Radiation.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Total Solar Radiation for Mesonet Fort Yates County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Lysine')
   
    plt.show()
def FortYatesTPP():
    data = pd.read_csv('Fort Yates Avg Penman PET.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Penman PET for Mesonet Fort Yates County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Inches')
   
    plt.show()
def CarsonBS():
    data = pd.read_csv('Carson Avg Bare Soil Temp.csv')
    ids = data['Value']
    days = data['Period']

    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))

    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)

    plt.title('Average Bare Soil Temperature for Mesonet Carson County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')

    plt.show()
   
def CarsonDP():
    data = pd.read_csv('Carson Avg Dew Point.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Dew Point for Mesonet Carson County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()

def CarsonPENPET():
    data = pd.read_csv('Carson Avg Penman PET.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Penman PET for Mesonet Carson County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Inches')
   
    plt.show()
   
def CarsonTSP():
    data = pd.read_csv('Carson Avg Turf Soil Temp.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Turf Soil Temperature for Mesonet Carson County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()
   
def CarsonWC():
    data = pd.read_csv('Carson Avg Wind Chill.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Wind Chill for Mesonet Carson County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()

def CarsonWS():
    data = pd.read_csv('Carson Avg Wind Speed.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Wind Speed for Mesonet Carson County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Miles Per Hour')
   
    plt.show()
def CarsonAT():
    data = pd.read_csv('Carson AvgTemp.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Temperature for Mesonet Carson County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()

def CarsonMWS():
    data = pd.read_csv('Carson Max Wind Speed.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Maximum Wind Speed for Mesonet Carson County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Miles Per Hour')
   
    plt.show()
   
def CarsonMaxT():
    data = pd.read_csv('Carson MaxTemp.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Maximum Temperature for Mesonet Carson County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()

def CarsonMinT():
    data = pd.read_csv('Carson MinTemp.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Minimum Temperature for Mesonet Carson County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()

def CarsonTPP():
    data = pd.read_csv('Carson Avg Penman PET.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Penman PET for Mesonet Carson County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Inches')
   
    plt.show()
   
def CarsonTSR():
    data = pd.read_csv('Carson Total Solar Radiation.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Total Solar Radiation for Mesonet Carson County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Lysine')
   
    plt.show()
   
def lintonBS():
    data = pd.read_csv('Linton Avg Bare Soil Temp.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Bare Soil Temperature for Mesonet Linton County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')

    plt.show()
def lintonDP():
    data = pd.read_csv('Linton Avg Dew Point.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Dew Point for Mesonet Linton County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()
def lintonPENPET():
    data = pd.read_csv('Linton Avg Penman PET.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Penman PET for Mesonet Linton County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Inches')
   
    plt.show()
def lintonTSP():
    data = pd.read_csv('Linton Avg Turf Soil Temp.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Turf Soil Temperature for Mesonet Linton County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()
def lintonWC():
    data = pd.read_csv('Linton Avg Wind Chill.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Wind Chill for Mesonet Linton County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()

def lintonAT():
    data = pd.read_csv('Linton AvgTemp.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Temperature for Mesonet Linton County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()
def lintonWS():
    data = pd.read_csv('linton Avg Wind Speed.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Wind Speed for Mesonet Linton County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Miles Per Hour')
   
    plt.show()
def lintonAT():
    data = pd.read_csv('Linton AvgTemp.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Temperature for Mesonet Linton County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()
def lintonMaxT():
    data = pd.read_csv('Linton MaxTemp.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Maximum Temperature for Mesonet Linton County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()
def lintonMinT():
    data = pd.read_csv('Linton MinTemp.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Minimum Temperature for Mesonet Linton County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
   
    plt.show()
def lintonMWS():
    data = pd.read_csv('linton Max Wind Speed.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Maximum Wind Speed for Mesonet Linton County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Miles Per Hour')
   
    plt.show()
def lintonTSR():
    data = pd.read_csv('Linton Total Solar Radiation.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Total Solar Radiation for Mesonet Linton County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Lysine')
   
    plt.show()

def lintonTPP():
    data = pd.read_csv('Linton Avg Penman PET.csv')
    ids = data['Value']
    days = data['Period']
   
    objects = ('November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020','December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021')
    y_pos = np.arange(len(objects))
   
    plt.bar(y_pos, ids, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=90)
   
    plt.title('Average Penman PET for Mesonet Linton County (2019-Present)')
    plt.xlabel('Month')
    plt.ylabel('Inches')
   
    plt.show()