# #Calculate number of words and letters from previous Homeworks 5/6 output test file.
# # Create two csv:
# # 1.word-count (all words are preprocessed in lowercase)
# # 2.letter, coutcall, count_uppercase, percentage (add header, spacecharacters are not included)
# # CSVs should be recreated each time new record added.
import csv
from collections import defaultdict
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("NewsFeed.txt"):
            process_news_feed()

def process_news_feed():
  with open("Word_Count.csv", "w") as csvfile1:
    writer = csv.writer(csvfile1, delimiter="-")

    with open("NewsFeed.txt", "r") as file_to_read:
        content = file_to_read.read()
        for line in content.split("\n"):
            edited_line = line.strip()
            for word in edited_line.split(" "):
                word_length_str = str(len(word))
                writer.writerow([word, word_length_str])

  with open("Dict_CSV_file.csv", "w", newline="") as csvfile2:
    headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
    writer = csv.DictWriter(csvfile2, fieldnames=headers)
    writer.writeheader()
    letter_count = defaultdict(int)
    upper_letter_count = defaultdict(int)
    count_all_letters = 0

    with open("NewsFeed.txt", "r") as file_to_read:
        content = file_to_read.read()
        for line in content.split("\n"):
            edited_line = line.strip()
            for word in edited_line.split(" "):
                for letter in word:
                    count_all_letters+=1
                    letter_count[letter] += 1
                    if letter.isupper():
                        upper_letter_count[letter] += 1
        for letter, count in letter_count.items():
            percentage = round((count / count_all_letters) * 100, 2)
            writer.writerow({'letter': letter, 'count_all': count, 'count_uppercase': upper_letter_count[letter], 'percentage': percentage})

if __name__ == "__main__":
    process_news_feed()
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=".")
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
        observer.join()