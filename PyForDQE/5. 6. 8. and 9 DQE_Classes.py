import datetime
import os
import json
import xml.etree.ElementTree as ET
class NewsFeedContent:
    def __init__(self):
        self.content_type = None

    def choose_content_type(self):
        print('Please select the content type\n 1. News \n 2. Private Advertisment\n 3. Fun fact of the day\n 4. Take content from the file\n 5. Json Input\n 6. Xml Input\n')
        self.content_type = input("Enter the number of the content (1, 2, 3, 4, 5 or 6):\n")
        if self.content_type == '1':
         self.content_type = "News"
        elif self.content_type == '2':
            self.content_type = "Private Ad"
        elif self.content_type == "3":
            self.content_type = "Fun fact of the day"
        elif self.content_type == '4':
            self.content_type = "File Input"
        elif self.content_type == '5':
            self.content_type = "Json Input"
        elif self.content_type == '6':
            self.content_type = "XML Input"
        else:
            print("Incorrect choice of the content type. Plese enter '1', '2', '3', '4', '5' or '6'")
            self.choose_content_type()

    def write_content(self):
        pass
    def publish_content(self):
        pass

class News(NewsFeedContent):
    def __init__(self):
        super().__init__()
        self.news = None
        self.city = None

    def write_content(self):
        self.news = input("Write your news: \n")
        self.city = input("Write the city where the event happened: \n")
    def publish_content(self):
        date = datetime.datetime.today()
        file_writing = open("NewsFeed.txt", "a")
        file_writing.write(f"News----------------------------------\n {self.news} \n {self.city} {date.strftime('%x')}, {date.strftime('%H.%M')}\n")
        file_writing.close()
        file_reading = open("NewsFeed.txt", "r")
        print(file_reading.read())
        file_reading.close()

class Advertising(NewsFeedContent):
     def __init__(self):
        super().__init__()
        self.advertisment = None
        self.expiration_date = None

     def write_content(self):
      self.advertisment = input("Write the text of your advertisment: \n")
      self.expiration_date = input("Write the expiration date of your advertisment in the following format: day, month, year (e.g. 20.02.2024)\n")
     def publish_content(self):
         time_of_expiration = datetime.datetime.strptime(self.expiration_date, "%d.%m.%Y")
         date_until_expiration = datetime.datetime.today()
         days_until_expiration = (time_of_expiration - date_until_expiration).days
         file_writing = open("NewsFeed.txt", "a")
         file_writing.write(
             f"Private Ad----------------------------\n {self.advertisment} \nActual until: {time_of_expiration.strftime("%x,")} {days_until_expiration} days left\n")
         file_writing.close()
         file_reading = open("NewsFeed.txt", "r")
         print(file_reading.read())
         file_reading.close()

class FunFact(NewsFeedContent):
    def __init__(self):
        super().__init__()
        self.fun_fact = None
        self.rating = None

    def write_content(self):
        self.fun_fact = input("Write fun fact of the day: \n")
        self.rating = input("How would you rate the fact within the scale from 1 to 10? Enter the number:\n")

    def publish_content(self):
        file_writing = open("NewsFeed.txt", "a")
        file_writing.write(
            f"Fun fact of the day-------------------\n {self.fun_fact} \nRating of the fact: {self.rating}/10\n")
        file_writing.close()
        file_reading = open("NewsFeed.txt", "r")
        print(file_reading.read())
        file_reading.close()

import DQE_Functions_4

class InputFile(NewsFeedContent):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def publish_content(self):
     try:
        with open(self.file_path, 'r') as file:
            with open("NewsFeed.txt", "a") as file_writing:
              for line in file:
                  parsed_record = DQE_Functions_4.modify_text(line).replace(".", "\n")
                  file_writing.write(parsed_record)
        with open("NewsFeed.txt", "r") as file_reading:
           print(file_reading.read())
     except FileNotFoundError:
                print(f"File '{self.file_path}' not found.")
     else: os.remove(self.file_path)

class InputJson(NewsFeedContent):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def publish_content(self):
     try:
        with open(self.file_path, 'r') as json_file:
            with open("NewsFeed.txt", "a") as file_writing:
              data = json.load(json_file)
              news = data["news"]
              for item in news:
                  if item["type"]=="News":
                      date = datetime.datetime.today()
                      file_writing.write(item["type"] + " " + "----------------------------------\n")
                      file_writing.write(item["text"] + "\n")
                      file_writing.write(item["city"] + f" {date.strftime('%x')}, {date.strftime('%H.%M')} \n")
                  if item["type"]=="Fact":
                      file_writing.write("Fun fact of the day-------------------\n")
                      file_writing.write(item["text"] + "\n")
                      file_writing.write(item["rate"] + "/10")
     except FileNotFoundError:
                print(f"File '{self.file_path}' not found.")
     else: os.remove(self.file_path)

class XmlInput(NewsFeedContent):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def publish_content(self):
        try:
            with open(self.file_path, 'r') as xmlFile:
                with open("NewsFeed.txt", "a") as file_writing:
                  xmlContent = ET.parse(xmlFile).getroot()
                  for news_item in xmlContent.findall("news_item"):
                   for type in news_item.iter("type"):
                     if type.text=="News":
                         date = datetime.datetime.today()
                         file_writing.write(type.text + " " + "----------------------------------\n")
                     for text in news_item.iter("text"):
                       file_writing.write(text.text + "\n")
                     for city in news_item.iter("city"):
                        file_writing.write(city.text + f" {date.strftime('%x')}, {date.strftime('%H.%M')} \n")
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
        else: os.remove(self.file_path)

if __name__ == "__main__":
    newContent = NewsFeedContent()
    newContent.choose_content_type()
    if newContent.content_type == "News":
        news = News()
        news.write_content()
        news.publish_content()
    elif newContent.content_type == "Private Ad":
        ad = Advertising()
        ad.write_content()
        ad.publish_content()
    elif newContent.content_type == "Fun fact of the day":
        fact = FunFact()
        fact.write_content()
        fact.publish_content()
    elif newContent.content_type == "File Input":
        file_input = InputFile("C:/Users/Yulia_Klimova/Python for DQE Basics/pythonProject/PyForDQE/News_to_read.txt")
        file_input.publish_content()
    elif newContent.content_type == "Json Input":
        json_input = InputJson("C:/Users/Yulia_Klimova/Python for DQE Basics/pythonProject/PyForDQE/json_to_read.json")
        json_input.publish_content()
    elif newContent.content_type == "XML Input":
        xml_input = XmlInput("C:/Users/Yulia_Klimova/Python for DQE Basics/pythonProject/PyForDQE/news.xml")
        xml_input.publish_content()

