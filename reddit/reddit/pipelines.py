import pymongo

from reddit import settings
from scrapy.exceptions import DropItem
import logging


class MongoDBPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler.settings.get('MONGODB_SERVER'),
            crawler.settings.get('MONGODB_PORT'),
            crawler.settings.get('MONGODB_DB'),
            crawler.settings.get('MONGODB_COLLECTION'),
        )

    def __init__(self, server, port, db, collection):
        connection = pymongo.MongoClient(
            server,
            port
        )
        db = connection[db]
        self.collection = db[collection]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            logging.debug("Item added to MongoDB database!")
        return item
