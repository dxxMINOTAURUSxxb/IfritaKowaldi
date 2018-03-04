from html.parser import HTMLParser
from urllib.request import urlopen

CODEFORCES_URL = "http://codeforces.com"
CONTEST_URL = "/contest/"


class ProblemsLinkParser(HTMLParser):
    def error(self, message):
        pass

    def __init__(self, contest, *args, **kwargs):
        self.problems = dict()
        self.contest = contest
        super().__init__(*args, **kwargs)
        self.feed(self.read_site_content())

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    if attr[1].find('/problem/') != -1:
                        self.problems[attr[1].split('/')[-1]] = TaskTestParser(attr[1]).tests

    def read_site_content(self):
        return str(urlopen(CODEFORCES_URL + CONTEST_URL + str(self.contest)).read())


class TaskTestParser(HTMLParser):
    def error(self, message):
        pass

    def __init__(self, task_link, *args, **kwargs):
        self._start_write = None
        self._start = False
        self.tests = []
        self.current_task = dict()
        self.task_link = task_link
        super().__init__(*args, **kwargs)
        self._task_number = 0
        self.feed(self.read_site_content())

    def read_site_content(self):
        return str(urlopen(CODEFORCES_URL + self.task_link).read())

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            for attr in attrs:
                if attr[0] == "class" and (attr[1] == "input" or attr[1] == "output"):
                    self._start_write = attr[1]
                    if attr[1] == "input":
                        self._task_number += 1
                    self.current_task["name"] = "Test%d" % self._task_number
        if tag == "pre":
            self._start = True

    def handle_data(self, data):
        data = str(data).replace("\\xc2\\xa0", " ").replace("\\'", "'")
        if self._start_write and self._start:
            if self.current_task.get(self._start_write):
                self.current_task[self._start_write].append(data)
            else:
                self.current_task[self._start_write] = [data]

    def handle_endtag(self, tag):
        if tag == "pre":
            self._start = False
            if self._start_write == "output":
                self.current_task["input"] = " ".join(self.current_task["input"]).strip()
                self.current_task["output"] = " ".join(self.current_task["output"]).strip()
                self.tests.append(self.current_task)
                self.current_task = dict()
                self._start_write = None
