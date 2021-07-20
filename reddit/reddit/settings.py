# Scrapy settings for reddit project
BOT_NAME = 'reddit'

SPIDER_MODULES = ['reddit.spiders']
NEWSPIDER_MODULE = 'reddit.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'reddit (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

LOG_LEVEL = "INFO"

ITEM_PIPELINES = ['stack.pipelines.MongoDBPipeline']

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "reddit"
MONGODB_COLLECTION = "items"

# MONGO DB integration
ITEM_PIPELINES = {
   'reddit.pipelines.MongoDBPipeline': 300,
}

