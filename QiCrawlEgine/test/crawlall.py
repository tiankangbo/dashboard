import os
from scrapy.commands import ScrapyCommand
from scrapy.utils.conf import arglist_to_dict
from scrapy.utils.python import without_none_values
from scrapy.exceptions import UsageError

class Command(ScrapyCommand):

    def run(self, args, opts):

        spd_loader_list=self.crawler_process.spider_loader.list()

        for spname in spd_loader_list or args:
            self.crawler_process.crawl(spname, **opts.spargs)
            print('this spider is --> '+ spname)
        self.crawler_process.start()