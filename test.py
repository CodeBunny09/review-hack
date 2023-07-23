from selenium import webdriver
from selenium.webdriver.common.by import By

import sys
from time import sleep
import pandas as pd
import random

reviews = ["Delicious pizza with excellent toppings.", 
"Great customer service and quick delivery.", 
"Perfectly baked crust with mouthwatering flavors.", 
"Melt-in-your-mouth cheese and flavorful sauce.", 
"Consistently fresh and flavorful pizzas.", 
"Authentic taste that always hits the spot.", 
"Amazing variety of toppings to choose from.", 
"Tasty and satisfying every single time.", 
"Satisfies all our pizza cravings.", 
"Never disappoints with their quality.", 
"Delightful combination of flavors in every bite.", 
"Crunchy crust and perfectly melted cheese.", 
"Always reliable for a delicious pizza feast.", 
"Generous portions of toppings on a perfectly thin crust.", 
"Top-notch pizza with unbeatable taste.", 
"Unforgettable and delightful pizza experience.", 
"Highly recommended for pizza lovers.", 
"Savory and satisfying till the last slice.", 
"Can't resist their mouthwatering pizzas.", 
"Always fresh and piping hot.", 
"Delivers exactly what we crave.", 
"Flavor explosion in every bite.", 
"Never get enough of their amazing pizzas.", 
"Craving their pizzas again and again.", 
"Efficient and friendly staff.", 
"Perfectly balanced flavors that keep you coming back.", 
"Best pizza place in town.", 
"Absolutely addictive and delicious.", 
"Best combination of ingredients on a crispy crust.", 
"Consistently amazing pizzas.", 
"Outstanding quality and taste.", 
"Always a treat for our taste buds.", 
"Satisfying and flavorful pizzas every time.", 
"Prompt service and mouthwatering flavors.", 
"Seriously addictive and tasty pizzas.", 
"Can't resist ordering from PizzaHut.", 
"Mouthwatering aroma and deliciously cheesy.", 
"Never fails to deliver a fantastic pizza.", 
"Impeccable taste and quality.", 
"Crusty and cheesy perfection in every slice.", 
"Always fresh and satisfying.", 
"Best pizza we've ever had.", 
"Craving PizzaHut's delightful pizzas.", 
"Consistently outstanding and savory.", 
"Perfectly baked pizzas with incredible taste.", 
"Quality ingredients that make a difference.", 
"Amazing value for the price.", 
"Great place for a family pizza night.", 
"Exquisite flavors that leave you wanting more.", 
"Best place to satisfy your pizza cravings.", 
"Incredibly delicious and truly satisfying.", 
"Outstanding blend of flavors and textures.", 
"PizzaHut never disappoints!", 
"Crunchy, cheesy, and everything we love.", 
"Irresistible and mouthwatering pizzas.", 
"Always exceeds our expectations.", 
"Delicious crust and well-balanced toppings.", 
"Consistently the best quality pizzas.", 
"Perfect spot for a pizza party.", 
"Satisfies our pizza desires every time.", 
"Flavorful, cheesy, and absolutely heavenly.", 
"Awesome service and scrumptious pizzas.", 
"Addictive taste that leaves you craving more.", 
"Best pizza experience in town.", 
"Fresh and flavorful ingredients on a perfect crust.", 
"Reliable for the most delicious pizzas.", 
"Can't get enough of their tasty delights.", 
"Fantastic variety and flavors to choose from.", 
"Always a winner for pizza lovers.", 
"Elevates pizza to a whole new level.", 
"Crave-worthy pizzas that never disappoint.", 
"Always reliable for a fantastic pizza feast.", 
"Delectable taste and exceptional quality.", 
"Authentic flavors that transport you.", 
"Consistently delivers heavenly pizzas.", 
"Deliciously crispy crust with mouthwatering toppings.", 
"Never disappoints with their incredible pizzas.", 
"Perfectly seasoned and utterly delicious.", 
"Keeps us coming back for more.", 
"Mouthwatering and satisfying every time.", 
"Can't resist their cheesy and savory pizzas.", 
"Always delivers a top-notch pizza experience.", 
"Absolutely worth every penny.", 
"Best pizza place around, hands down.", 
"Unforgettable taste that lingers.", 
"Delightful combination of flavors.", 
"Crunchy perfection with gooey goodness.", 
"Always a happy pizza experience.", 
"Irresistibly delicious and satisfying.", 
"Exquisite and unforgettable flavors.", 
"Best pizza in town, no doubts.", 
"Authentic and mouthwatering pizzas.", 
"Never fails to impress with their pizza.", 
"Savor the sensational taste every time.", 
"Flavor-packed pizzas that leave you craving more."]


def review(link):

    data = pd.read_csv('data.csv')
    driver = webdriver.Chrome()
    driver.get(link)
    sleep(5)

    driver.find_element(By.ID, "NextButton").click()
    sleep(3)

    #Star 1
    print("Star1")
    driver.find_element(By.XPATH, '//*[@id="FNSR007000"]/td[1]/span').click()
    sleep(3)

    #Star 2
    print("Star2")
    driver.find_element(By.XPATH, '//*[@id="FNSR000205"]/td[1]/span').click()
    sleep(3)

    #Service satisfaction
    print("Satisfaction")
    driver.find_element(By.ID, "FNSR000175").click()
    driver.find_element(By.ID, "FNSR000171").click()
    driver.find_element(By.ID, "FNSR000169").click()
    driver.find_element(By.ID, "FNSR000168").click()
    driver.find_element(By.ID, "FNSR000172").click()
    driver.find_element(By.ID, "FNSR000173").click()
    driver.find_element(By.ID, "FNSR000170").click()
    driver.find_element(By.ID, "FNSR000190").click()

    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/form/div/div[3]/input').click()
    sleep(3)

    #Cheese Max
    print("Cheese Max")
    driver.find_element(By.XPATH, '//*[@id="FNSR000265"]/div/div/div[10]').click()
    sleep(3)

    #Momo Pizza
    print("Momo Pizza")
    driver.find_element(By.XPATH, '//*[@id="FNSR000290"]/div/div/div[1]').click()
    sleep(3)

    #Manager said
    print("Manager Said")
    driver.find_element(By.XPATH, '//*[@id="FNSR000291"]/div/div/div[2]').click()
    sleep(3)

    #Prev experience
    print("Prev Exp")
    driver.find_element(By.XPATH, '//*[@id="FNSR000292"]/div/div/div[4]').click()
    sleep(3)

    #Four or more visit
    print("N Visits")
    driver.find_element(By.XPATH, '//*[@id="FNSR000294"]/div/div/div[4]').click()
    sleep(3)

    #Recieve emails
    print("Mails")
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/form/div/fieldset/div/div/div[1]').click()
    sleep(4)

    #Fname
    driver.find_element(By.ID, "S090100").send_keys(data.FirstName[-1])
    #LName
    driver.find_element(By.ID, "S090200").send_keys(data.LastName[-1])
    #Number
    driver.find_element(By.ID, "S092000").send_keys(data.PhoneNumber[-1])
    #Email
    driver.find_element(By.ID, "S093000").send_keys(data.Email[-1])
    #Conf Email
    driver.find_element(By.ID, "S093500").send_keys(data.Email[-1])

    data.drop(index=data.index[-1],axis=0,inplace=True)
    data.to_csv('data.csv', mode="w")

    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/form/div/div[9]/input').click()
    sleep(3)

    #Review
    print("Review")
    driver.find_element(By.ID, "S000176").send_keys(random.choice(reviews))

    print("Ok")
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/form/div/div[4]/input').click()
    sleep(5)

    code = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form/div/div/div/div[1]/div/p[5]').text

    data = {
          "link": [link],
          "code": [code]
    }

    df = pd.DataFrame(data)
    df.to_csv('verification_codes.csv', mode='a', index=False, header=False)

    driver.close()




"""
linklist = ["https://s.pizzahutsurvey.com/IND?CN=SFL222220723212020&V=5&O=1&source=SMS&U=1323109000011367",
"https://s.pizzahutsurvey.com/IND?CN=SFL222220723112020&V=5&O=1&source=SMS&U=1323109000011368",
"https://s.pizzahutsurvey.com/IND?CN=SFL222220723112920&V=5&O=1&source=SMS&U=1323109000011369",
"https://s.pizzahutsurvey.com/IND?CN=SFL222220723111020&V=5&O=1&source=SMS&U=1323109000011370",
"https://s.pizzahutsurvey.com/IND?CN=SFL222220723141020&V=5&O=1&source=SMS&U=1323109000011371",
"https://s.pizzahutsurvey.com/IND?CN=SFL222220723141920&V=5&O=1&source=SMS&U=1323109000011372",
"https://s.pizzahutsurvey.com/IND?CN=SFL222220723161920&V=5&O=1&source=SMS&U=1323109000011373",
"https://s.pizzahutsurvey.com/IND?CN=SFL222220723200920&V=5&O=1&source=SMS&U=1323109000011374",
"https://s.pizzahutsurvey.com/IND?CN=SFL222220723203020&V=5&O=1&source=SMS&U=1323109000011375",
"https://s.pizzahutsurvey.com/IND?CN=SFL222220723203920&V=5&O=1&source=SMS&U=1323109000011376",
"https://s.pizzahutsurvey.com/IND?CN=SFL222220723213920&V=5&O=1&source=SMS&U=1323109000011377",
"https://s.pizzahutsurvey.com/IND?CN=SFL222220723211820&V=5&O=1&source=SMS&U=1323109000011378",
"https://s.pizzahutsurvey.com/IND?CN=SFL222220723211810&V=5&O=1&source=SMS&U=1323109000011379",
"https://s.pizzahutsurvey.com/IND?CN=SFL222220723212810&V=5&O=1&source=SMS&U=1323109000011380"]

"""
# for link in linklist:
for i in range(20):
        review(sys.argv[1])
