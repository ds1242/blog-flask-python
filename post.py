class Post:
    def __init__(self, post_id, title, subtitle, text, date, author, image_url, image_alt):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = text
        self.date = date
        self.author = author
        self.image_url = image_url
        self.image_alt = image_alt