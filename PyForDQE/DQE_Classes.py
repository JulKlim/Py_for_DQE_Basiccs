import datetime
class NewsFeedContent:
    def __init__(self):
        self.content_type = None

    def choose_content_type(self):
        print('Please select the content type\n 1. News \n 2. Private Advertisment\n 3. Fun fact of the day')
        self.content_type = input("Enter the number of the content (1, 2 or 3):\n")
        if self.content_type == '1':
         self.content_type = "News"
        elif self.content_type == '2':
            self.content_type = "Private Ad"
        elif self.content_type == "3":
            self.content_type = "Fun fact of the day"
        else:
            print("Incorrect choice of the content type. Plese enter '1', '2' or '3'")
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

class main:
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

