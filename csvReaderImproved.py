Created on Tue Mar 6 11:13:43 2021

@author: Jacob

#Station_ID,Date_Time,altimeter_set_1,air_temp_set_1,dew_point_temperature_set_1,relative_humidity_set_1,wind_speed_set_1,wind_direction_set_1,wind_gust_set_1,sea_level_pressure_set_1,weather_cond_code_s    et_1,cloud_layer_3_code_set_1,pressure_tendency_set_1,precip_accum_one_hour_set_1,precip_accum_three_hour_set_1,cloud_layer_1_code_set_1,cloud_layer_2_code_set_1,precip_accum_six_hour_set_1,precip_accum    _24_hour_set_1,visibility_set_1,metar_remark_set_1,metar_set_1,air_temp_high_6_hour_set_1,air_temp_low_6_hour_set_1,peak_wind_speed_set_1,ceiling_set_1,pressure_change_code_set_1,air_temp_high_24_hour_s    et_1,air_temp_low_24_hour_set_1,peak_wind_direction_set_1,dew_point_temperature_set_1d,cloud_layer_1_set_1d,cloud_layer_3_set_1d,cloud_layer_2_set_1d,wind_chill_set_1d,weather_summary_set_1d,wind_cardin    al_direction_set_1d,pressure_set_1d,sea_level_pressure_set_1d,heat_index_set_1d,weather_condition_set_1di')
#,,INHG,Fahrenheit,Fahrenheit,%,Miles/hour,Degrees,Miles/hour,INHG,code,code,code,Inches,Inches,code,code,Inches,Inches,Statute miles,text,text,Fahrenheit,Fahrenheit,Miles/hour,Feet,code,Fahrenheit,Fahrenheit,Degrees,Fahrenheit,code,code,code,Fahrenheit,code,code,INHG,INHG,Fahrenheit,code
import csv
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap

def convert_float(val): #convert string to float for float lists, return '' if false
    try:
        return float(val)
    except ValueError:
        return ''


#input file name
filename = input('Input the csv file name. Enter: ')
 
#open desired file
file = open(filename,'r') 

print('____________________________________________________________________________')
print()

#print station info of file
for i in range(6): 
    header = file.readline().replace('\n','').split(':')    
    print(header)

print('____________________________________________________________________________')

#split into columns for data types and units
dataType = file.readline().split(',') 
dataUnits = file.readline().split(',')

#defines variables as 0 to be assigned later
tempIndex = timeIndex = pressureIndex = dewpointIndex = windspeedIndex = rhIndex = winddirIndex = 0
sealevelpIndex = precip24hIndex = weathersumIndex = windcardinaldirIndex = statutemileIndex = 0
maxT = 0.0
maxDP = 0.0
maxIndex = minIndex = 0
minT = 1000.0
minDP = 1000.0
maxTime=''
minTime = ''
#centers labels for front and end of data set
timeLabel = 'Time'.center(21)
tempLabel = 'Temp'.center(8)
pressureLabel = 'Pressure'.center(12)
dewpointLabel = 'Dewpoint'.center(8)
rhLabel = 'RH'.center(8)
windspeedLabel = 'WindSpeed'.center(11)
winddirLabel = 'WindDir'.center(9)
windgustLabel = 'WindGust'.center(11)
precip24hrLabel = 'Precp24H'.center(8)
weathersumLabel = 'WeatherSum'.center(20)
windcardinalLabel = 'Crdnl'.center(5)
statutemilesLabel = 'SM'.center(9) 

#lists for data in value format(float/string, without units)
Temp = []
TempPlot = []
Time = []
TimePlot = []
Pressure = []
Dewpoint = []
DewpointPlot = []
RH = []
Windspeed = []
Winddir = []
Windgust = []
Precip24h = []
Weathersum = []
Windcardinal = []
Statutemiles=[]

#lists for data in string format(with units and format)
TimeFormat = []
TempFormat = []
PressureFormat = []
DewpointFormat = []
RHFormat = []
WindspeedFormat = []
WinddirFormat = []
WindgustFormat = []
Precip24hFormat = []
WeathersumFormat = []
WindcardinalFormat = []
StatutemilesFormat = []

#finds index of dataType columns so that it may use the index to store the data in the correct list
for i,j in enumerate(dataType):
    if(j == 'air_temp_set_1'): 
        tempIndex = i               
    elif(j == 'Date_Time'): 
        timeIndex = i
    elif(j == 'pressure_set_1d'): 
        pressureIndex = i
    elif(j == 'dew_point_temperature_set_1d'): 
        dewpointIndex = i
    elif(j == 'relative_humidity_set_1'): 
        rhIndex = i
    elif(j == 'wind_speed_set_1'): 
        windspeedIndex = i
    elif(j == 'wind_direction_set_1'): 
        winddirIndex = i
    elif(j == 'wind_gust_set_1'): 
        windgustIndex = i
    elif(j == 'precip_accum_24_hour_set_1'): 
        precip24hIndex = i
    elif(j == 'weather_summary_set_1d'): 
        weathersumIndex = i
    elif(j == 'wind_cardinal_direction_set_1d'): 
        windcardinaldirIndex = i
    elif(j == 'visibility_set_1'):
        statutemileIndex = i

length = 0    
#Converts the column data into floats and then appends it into the proper lists. 
for line in file:
    length+=1
    #this wonderful csv reader splits by ',' and prevents weathersum of "rain,mist" to be split
    for linesplit in csv.reader([line]):
        continue
    
    Temp.append(convert_float(linesplit[tempIndex]))
    Time.append(linesplit[timeIndex])
    Pressure.append(convert_float(linesplit[pressureIndex]))
    Dewpoint.append(convert_float(linesplit[dewpointIndex]))
    RH.append(convert_float(linesplit[rhIndex]))
    Windspeed.append(convert_float(linesplit[windspeedIndex]))
    Winddir.append(convert_float(linesplit[winddirIndex]))
    Windgust.append(convert_float(linesplit[windgustIndex]))
    Precip24h.append(convert_float(linesplit[precip24hIndex]))
    Weathersum.append(linesplit[weathersumIndex])
    Windcardinal.append(linesplit[windcardinaldirIndex])
    Statutemiles.append(convert_float(linesplit[statutemileIndex]))
    
   
file.close()

#finds min and max values while ignoring ''
for i in range(length):
    if(Temp[i] == ''):
        continue
    else:
        if(Temp[i] > maxT):
            maxT = Temp[i]
            maxTime = Time[i]
            maxIndex=i
        if(Temp[i] < minT):
            minT = Temp[i]
            minTime = Time[i]
            minIndex=i
    
    if(Dewpoint[i] == ''):
        continue
    else:
        if(Dewpoint[i] > maxDP):
            maxDP = Dewpoint[i]
            maxIndexDP = i
        if(Dewpoint[i] < minDP):
            minDP = Dewpoint[i]
            minIndexDP = i
            
#combined dataType columns    
Datacomplist = zip(Time,Pressure,Temp,Dewpoint,RH,Windspeed,Windgust,Winddir,Windcardinal,Precip24h,Weathersum,Statutemiles)
#append string formatted data to formatted data type lists.
for a,b,c,d,e,f,g,h,i,j,l,m in Datacomplist:  
    
    TimeFormat.append(a)

    b_format = '{i}'.format(i = '---------' if b=='' else '{:5.2f} inHg'.format(b))
    PressureFormat.append(b_format)
    
    c_format = '{i}'.format(i = '------' if c=='' else '{:5.2f}F'.format(c))
    TempFormat.append(c_format)
        
    d_format = '{i}'.format(i = '------' if d=='' else '{:5.2f}F'.format(d))
    DewpointFormat.append(d_format)
      
    e_format = '{i}'.format(i = '------' if e=='' else '{:5.2f}%'.format(e))
    RHFormat.append(e_format)
       
    f_format = '{i}'.format(i = '---------' if f=='' else '{:5.2f} mph'.format(f))
    WindspeedFormat.append(f_format)
     
    g_format = '{i}'.format(i = '---------' if g=='' else '{:5.2f} mph'.format(g))
    WindgustFormat.append(g_format)
        
    h_format = '{i}'.format(i = '-------' if h=='' else '{:6.2f}°'.format(h))
    WinddirFormat.append(h_format)
    
    i_format = '{i}'.format(i = '---' if i=='' else '{:3}'.format(i))
    WindcardinalFormat.append(i_format)
      
    j_format = '{i}'.format(i = '-------' if j=='' else '{:5.2f}in'.format(j))
    Precip24hFormat.append(j_format)
    
    l_format = '{i}'.format(i = '---------------------------' if l=='' else 'Condition: {:16}'.format(l))
    WeathersumFormat.append(l_format)
    
    m_format = '{i}'.format(i = '------' if m=='' else '{:4.1f}SM'.format(m))
    StatutemilesFormat.append(m_format)
       
print()
print(timeLabel,pressureLabel,tempLabel,dewpointLabel,rhLabel,windspeedLabel,windgustLabel,winddirLabel,windcardinalLabel ,precip24hrLabel,statutemilesLabel,weathersumLabel)

#combined formatted dataType columns 
DataFormatList = zip(TimeFormat,PressureFormat,TempFormat,DewpointFormat,RHFormat,WindspeedFormat,WindgustFormat,WinddirFormat,WindcardinalFormat,Precip24hFormat,WeathersumFormat,StatutemilesFormat)
#print formatted data
for a,b,c,d,e,f,g,h,i,j,l,m in DataFormatList: 
    print(a,'|',b,'|',c,'|',d,'|',e,'|',f,'|',g,'|',h,'|',i,'|',j,'|',m,'|',l,'|')

print(timeLabel,pressureLabel,tempLabel,dewpointLabel,rhLabel,windspeedLabel,windgustLabel,winddirLabel,windcardinalLabel,precip24hrLabel,statutemilesLabel,weathersumLabel)
print()


for loop in range(100):
#user input for choice
    print('Type 1,2,3... for desired results. One at a time. Type q to quit.')
    print('----------------------------------------------------------------------------')
    print('1:Max and Min, Temp and Dew point Temp')
    print('2:')
    userInput = input('Enter: ')

    
#prints Min and Max Temp and DP
    if(userInput == '1'):
        print('Max Temp:',TempFormat[maxIndex],  '| Min Temp:',TempFormat[minIndex])
        print('Max DP:',DewpointFormat[maxIndexDP] ,  '| Min DP:',DewpointFormat[minIndexDP])
        print()
        
        #asks to plot the data
        print('Would you like to plot? y for yes and n for no' )
        plotInput = input('Enter: ')
        if (plotInput == 'y'):
            xint = (len(Temp)/9)
            
            #creates new lists for plotting, as '' in data is not ideal for plots.
            for T,D,i in zip(Temp,Dewpoint,Time):
                if(T == '' or D == ''):
                    continue
                else:
                    TempPlot.append(T)
                    DewpointPlot.append(D)
                    TimePlot.append(i)
                    
                    
           ## plotting code is in progress ##
            
            plt.figure(figsize=(40,24))
            x_ticks = np.linspace(0, len(Temp)+xint,10)
            plt.xticks(x_ticks)            
            y_ticks = np.arange(round(minDP-3), round(maxT+3),2)
            plt.yticks(y_ticks)
            
            Time = ['\n'.join(wrap(l, 12)) for l in Time]
            plt.plot(TimePlot,TempPlot, "-r", label="Temp")
            plt.plot(TimePlot,DewpointPlot, "-b", label="Dew point")
            plt.legend(loc='upper left')
            plt.xlabel('Time')
            plt.ylabel('Temp')
            plt.show()
            
                

                        


#quit
    if(userInput == 'q'):
        break
###############################################################################

