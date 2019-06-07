# Name - Shubham Mathankar
# Description - code for scrapping all hotel name, hotel address and aminities corresponding their city name. It requires city main page "url1" and total no. of pages in range()

from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
 

for i in range(1):
    url1 = urlopen("https://www.cleartrip.com/hotels/india/tiruvannamalai?page=" + str(i))
    bs_obj = BeautifulSoup(url1, "html.parser")
    
    def down_aminity(bs_obj):
        aminity_name1 = bs_obj.find_all("div", {"class": "col-sm-8 pad-lzero hidden-xs"})
        A1=[]
        A2=[]
        A3=[]
        A4=[]
        A5=[]
        A6=[]
        A7=[]
        A8=[]
        A9=[]

        if aminity_name1:
            for tag in aminity_name1:
            
                if tag.find("span", {"class":"amWIFI"}):
                    A1.append(tag.find("span", {"class":"amWIFI"}).text)
                else:
                    A1.append("*")
                if tag.find("span", {"class":"amAC"}):
                    A2.append(tag.find("span", {"class":"amAC"}).text)
                else:
                    A2.append("*")
                if tag.find("span", {"class":"amRestaurant"}):
                    A3.append(tag.find("span", {"class":"amRestaurant"}).text)
                else:
                    A3.append("*")
                if tag.find("span", {"class":"amBar"}):
                    A4.append(tag.find("span", {"class":"amBar"}).text)
                else:
                    A4.append("*")
                if tag.find("span", {"class":"amRoomService"}):
                    A5.append(tag.find("span", {"class":"amRoomService"}).text)
                else:
                    A5.append("*")
                if tag.find("span", {"class":"amInternet"}):
                    A6.append(tag.find("span", {"class":"amInternet"}).text)
                else:
                    A6.append("*")
                if tag.find("span", {"class":"amBusinessCenter"}):
                    A7.append(tag.find("span", {"class":"amBusinessCenter"}).text)
                else:
                    A7.append("*")
                if  tag.find("span", {"class":"amPool"}):
                    A8.append(tag.find("span", {"class":"amPool"}).text)
                else:
                    A8.append("*")
                if tag.find("span", {"class":"amGym"}):
                    A9.append(tag.find("span", {"class":"amGym"}).text)
                else:
                    A9.append("*")
        lis=[]
        for i,j,k,l,m,n,o,p,q in zip(A1,A2,A3,A4,A5,A6,A7,A8,A9):
            lis.append([i,j,k,l,m,n,o,p,q])




        with open('all.csv','a',newline='') as f:
            head1=['hotel_name','location','aminity']
            writer=csv.DictWriter(f,fieldnames=head1)
            writer.writeheader()
            for i,j,k in zip(hot,loc,lis):
                writer.writerow({'hotel_name':i,'location':j,'aminity':k})





    def down_hotel(bs_obj):
        dn1 = bs_obj.find_all("h2", {"class": "hotels-name"})
        a1=[]
        if dn1:
            for tag in dn1:
                hotel_name1 = tag.find("span").text
                a1.append(hotel_name1)
        return a1



    
    def loca(bs_obj):
        lc = bs_obj.find_all("li", {"class": "hotels-location"})
        a2=[]
        if lc:
            for tag in lc:
                location = tag.find("a")
                if location:
                    a2.append(location.text)
                else:
                    a2.append("*")
        return a2


    
    hot = down_hotel(bs_obj)
    loc = loca(bs_obj)
    down_aminity(bs_obj)
