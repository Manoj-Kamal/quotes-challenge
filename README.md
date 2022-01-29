# Coding Assignment - 2.2
**Summary:**

This spider will scrape the below fields from http://quotes.toscrape.com/js/ website using Scrapy and Splash:

Quote
Author Name and 
Tags


To run this spider, please ensure you have a running docker splash instance. You can run the docker splash instance using the below command

```
docker run -it -p 8050:8050 scrapinghub/splash
```

To install the pre-requisites for the spider run the below commands.

```
pip install scrapy

pip install scrapy_splash
```

To export the data into a CSV or JSON format, please execute the below command

```
scrapy crawl quotes -o Quotes_Output.json
```

Happy Scraping!