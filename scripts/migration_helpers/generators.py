from api.models import ClimbUser
from pages.models import Report, NewsPost, Comment, GalleryImage

from pathlib import Path
import os
from django.core.files import File
from django.utils.timezone import now


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


def populate_comments(author, per_report = 5):
    reports = Report.objects.all()
    for report in reports:
        for i in range(per_report):
            c = Comment()
            c.comment_creator = author
            c.content = f"content {i}"
            c.report_id = report
            c.save()

def populate_gallery(author, image_folder):
    reports = Report.objects.all()

    images = []
    
    for filename in os.listdir(image_folder):
        if filename.endswith(".png"):
            path = os.path.join(image_folder, filename)
            images.append(path)
            
    print(images)

    for report in reports:
        for img in images:
            g = GalleryImage(image = File(open(img, "rb")))
            g.gallery = report
            g.created = now()
            g.save()