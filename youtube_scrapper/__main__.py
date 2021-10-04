from Web_Scraping_Project.youtube_scrapper.scrapper.video_data import VideoData

print('This is a Web_scrapper package for Youtube')
print('Input the youtube channel you want to scrape data from, number of videos you want to scrape and the path to '
      'your chromedriver')
channel = (input('Youtube channel: '))
height = int(input('Number of videos: '))
driver_path = (input('Path to chromedriver: '))
scraper = VideoData(channel, height, driver_path)
data = scraper.get_yt_data()
print("thank you for using YT scrapper")
