!pip install bs4
!pip install selenium
!pip install lxml
import lxml
import urllib3
import pandas as pd
import requests
import sys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
class Prices:
	if __name__ == "__main__":
"""
Appends chromedriver to system using its given location on host computer.
"""
		
def system_get_function():
	val = input("Enter:your system directory for chromedriver")
	try:
		sys.path.append(val)
	except:
		System.out.println("Invalid path directory pointer location")
"""
Takes input as a shoe name and makes it a search term by making it lowercase and adding it to the standard stockxsearch term.
Checks wheter input is a valid shoe by ensuring its length fits into certain parameters that are standard shoes
@Returns: The complete search term.
"""
def url_getter():
		Stockx_Search_Url= "https://www.stockx.com/"
	searchTerm = input("Enter the Search Term of the shoe exactly as it appears:")
	searchTerm = searchTerm.lower()
	count = len(searchTerm.split())
	print (count) 
	if count > 13:
		print("Invalid entry, please enter the shoe name exactly as it appears on the Stockx website")
	if count <= 5: 
		print("Invalid entry, please enter the shoe name exactly as with words like Air and Retro")
	for i in range(0, len(searchTerm), 1):

		# Changing the ith character
		# to '-' if it's a space.
		if (searchTerm[i] == ' '):
		    searchTerm = searchTerm.replace(searchTerm[i],'-')
	print (searchTerm)
	Stockx_Search_Url= "https://www.stockx.com/"
	url = Stockx_Search_Url+searchTerm
	print(url)
	return url
"""
Scrapts the first iteration of stockx htmly layout.
Finds volatillity by using class value in the layout and scraps unwanted characters with the regex sub function.
Finds date using class value and places it into date/month/year format.
Uses the difference from release time and current date and the shoe type to create predictions on the shoes release price.
"""
def html_scraper1(table_top):
	 table_top.drop_duplicates(subset='Size', keep="first")
        vola = soup.findAll(class_="value")
        date = soup.findAll(class_="detail")
        text=str(date)
        new_vola=str(vola)
        x = re.findall('[0-9]+', new_vola)
        re.sub("span", "", str(x))
        re.sub("class", "", str(x))
        re.sub("<", "", str(x))
        re.sub(">", "", str(x))
        re.sub("value", "", str(x))
        re.sub("/", "", str(x))
        re.sub("-", "", str(x))
        def numConcat(num1, num2):
       
		# Convert both the numbers to
		# strings
		    num1 = str(num1)
		    num2 = str(num2)

		# Concatenate the strings
		    num1 += num2

		    return int(num1)
        one=(x[2])
        two=(x[3])
        comb_vola=(numConcat(one, two))/100
        print(comb_vola)
        vola=comb_vola
        y= re.findall('[0-9]+', text)
        print(y)
        loc_year=y.index("2022")
        loc_month=(loc_year-2)
        loc_day=(loc_year-1)
        year=y[(loc_year)]
        month=y[(loc_month)]
        day=y[(loc_day)]
        
        reldate= '/'.join([str(num) for num in [month, day, year]])
        date_format = "%m/%d/%Y"

        reldate= datetime.datetime.strptime(reldate,date_format)
        reldate=reldate.date()
        now_date= table_top.loc[1,"Date"]
        print(now_date)
        now_month = now_date.split(' ')[1]
        now_month1 = now_month[0:3]
        now_day=now_date.split(' ')[2]
        now_day = now_day.replace(',','')
        now_year=now_date.split(' ')[3]
        nowcomb_date=now_month1+ " " +now_day+ " "+now_year

        date_time_obj = datetime.datetime.strptime(nowcomb_date, '%b %d %Y')
        current_date=date_time_obj.date()
        delta=reldate-current_date
        daysdrop=delta.days
        table_top.drop_duplicates(subset=['Size'], inplace=True)
        if "jordan" in searchTerm: 
            zero_drop= 15
        
        elif "yeezy" in searchTerm: 
            zero_drop= 20
        elif "nike" in searchTerm: 
            zero_drop= 12
        else: 
            zero_drop=13
        if 0<daysdrop <=8:
            value_counter =13
            initial_val = value_counter- (daysdrop*(.9))
            dailydrop=initial_val*vola
            totaldrop=dailydrop*daysdrop+zero_drop
        elif 9<=daysdrop <= 20:
            value_counter=13
            initial_val = (value_counter- (8*.9*vola)*8)
            add_val= (1.8*vola)*(daysdrop-8)
            totaldrop=initial_val+add_val+zero_drop
            
        elif 21 <= daysdrop <65:
            initialval= ((21-(20*.91))*vola)*20
            add_val= (daysdrop-20)*(1.1*vola)
            totaldrop==initial_val+add_val+zero_drop
        table_top['Subtracting Value']=str(totaldrop)
        #table_top['Prediced Values']=float(table_top['Sale Price'])-table_top['Subtracting Value']
        table_top['Predicted Values'] = table_top.apply(lambda x: x['Sale Price'] - x['Subtracting Value'], axis=1)

        table_top.drop(['Sale Price','Date','Time'], axis = 1)
"""
Scrapts the first iteration of stockx htmly layout.
Finds volatillity by using class value in the layout and scraps unwanted characters with the regex sub function.
Finds date using class value and places it into date/month/year format.
Uses the difference from release time and current date and the shoe type to create predictions on the shoes release price.
"""
def html_scraper2(table_top):
	  #vola= driver.find_element_by_xpath("//dict[@typename='SalesInformation']")
        vola=soup.findAll(text=re.compile("volatility"))
        #x = re.findall('[0-9]+',str(vola))
        x= re.findall("\d+\.\d+",str(vola))
        vola_list=[]
        big_number = str(.1)
        for value in x[1:]:
         if value < big_number:
            vola_list.append(value)
        vol_val=vola_list[1]
        vola=float(vol_val)
        vola=vola*10
        
        date = soup.findAll(class_="chakra-container new-product-view css-vp2g1e")
        text=str(date)
       
        x = re.findall('[0-9]+', text)
        loc_year=[i for i, n in enumerate(x) if n == '2022'][1]
        loc_month=(loc_year+1)
        loc_day=(loc_year+2)
        year=x[(loc_year)]
        month=x[(loc_month)]
        day=x[(loc_day)]
        print(year)
        print(month)
        print(day)
        num='/'.join([str(num) for num in [month, day, year]])
        date_format = "%m/%d/%Y"

        reldate=datetime.datetime.strptime(num, date_format)
        reldate=reldate.date()
        print(reldate)
        now_date= table_top.loc[1,"Date"]
        print(now_date)
        now_month = now_date.split(' ')[0]
        now_month1 = now_month[0:3]
        now_day=now_date.split(' ')[1]
        now_day = now_day.replace(',','')
        now_year=now_date.split(' ')[2]
        nowcomb_date=now_month1+ " " +now_day+ " "+now_year

        date_time_obj = datetime.datetime.strptime(nowcomb_date, '%b %d %Y')
        current_date=date_time_obj.date()
        delta=reldate-current_date
        daysdrop=delta.days
        print(delta.days)
        print(daysdrop)
        if "jordan" in searchTerm: 
            zero_drop= 15
        
        elif "yeezy" in searchTerm: 
            zero_drop= 20
        elif "nike" in searchTerm: 
            zero_drop= 12
        else: 
            zero_drop=13
        if 0<daysdrop <=8:
            value_counter =13
            initial_val = value_counter- (daysdrop*(.9))
            dailydrop=initial_val*vola
            totaldrop=dailydrop*daysdrop+zero_drop
        elif 9<=daysdrop <= 20:
            value_counter=13
            initial_val = (value_counter- (8*.9*vola)*8)
            add_val= (1.8*vola) *(daysdrop-8)
            totaldrop=initial_val+add_val+zero_drop
            
        elif 21 <= daysdrop <65:
            initialval= ((21-(20*.91))*vola)*20
            add_val= (daysdrop-20)*(1.1*vola)
            totaldrop=initial_val+add_val+zero_drop
        else: 
            print("Invalid Restart Program and Enter a product that is releasing in less then 65 days and has not already released")
	
"""
Uses chromedriver to createa an automated chrome window that opens up to specific url of the shoe inputted.
Clicks button to expose sale data in stockx website and then uses previous scraping function to get the data.
@Returns: The final table display with the price predictions for each size of shoe.
"""
def site_data_scrapper():
	driver = webdriver.Chrome(executable_path='C:/users/Rpeddu/chromedriver_win32/chromedriver.exe')
	session = requests.Session()
	response = session.get(url)
	driver.get(url)
	driver.maximize_window()
	time.sleep(10)
	#driver.find_element_by_class_name('css-14bs28v').click()
	#driver.find_element_by_class_name('css-1ianwbe').click()
	#driver.find_element_by_class_name('all').click()
	driver.find_element_by_xpath('//button[normalize-space()="View Sales"]').click()

	import datetime
	if driver.find_elements_by_class_name('all'):
	    driver.find_element_by_xpath('//button[normalize-space()="Load More"]').click()
	    driver.find_element_by_xpath('//button[normalize-space()="Load More"]').click()
	    driver.find_element_by_xpath('//button[normalize-space()="Load More"]').click()


	time.sleep(5)
	soup = BeautifulSoup(driver.page_source,'html5lib')

	table = soup.find_all('table')
	table_top = pd.read_html(str(table))[0]

	if driver.find_elements_by_class_name('all'):
		html_scraper1(table_top)
	else: 
		html_scraper2(table_top)

	table_top['Sale Price'] = table_top['Sale Price'].map(lambda x: x.lstrip('$'))
	table_top['Sale Price'] = pd.to_numeric(table_top['Sale Price'], downcast="float")
	avg_saleval=table_top['Sale Price'].mean()
	avg_saleval=avg_saleval-totaldrop
	sizes=pd.Series(['7.0', '8.0', '9.0', '10.0','11.0','12.0','13.0'])
	table_top['Size']=sizes
	value_list=pd.Series([avg_saleval+10,avg_saleval-8,avg_saleval-4,avg_saleval-5,avg_saleval+4,avg_saleval+6,avg_saleval+7.5])
	table_top['Predicted Values']=value_list
	new_table_top=table_top.drop(['Sale Price','Date','Time'], axis = 1)
	final_display=new_table_top.head(7)
	return final_display
"""
Turns the final display inputted into a csv file with the location specified by the user.
"""
def tocsv(final_display):
	val_input= input("Enter the file location of where you would like to csv to go")
	final_display.to_csv(val_input)

