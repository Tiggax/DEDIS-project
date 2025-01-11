from api.models import ClimbUser
from pages.models import Report, Route, NewsPost


def reports(author, route, count = 50):
    for i in range(count):
        r = Report()
        r.title = f"Report title {i}"
        r.content = "content"
        r.report_creator = author
        r.route = route
        r.save()

def news(author, count = 50):
    for i in range(count):
        n = NewsPost()
        n.title = f"News post {i}"
        n.content = "content"
        n.post_author = author
        n.save()
