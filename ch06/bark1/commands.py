import datetime
import sys
from database import DatabaseManager

db = DatabaseManager("bookmarks.db")


class CreateBookmarksTableCommand:
    def execute(self):
        db.create_table(
            "bookmarks",
            columns={
                "id": "integer primary key autoincrement",
                "title": "text not null",
                "url": "text not null",
                "memo": "text",
                "date_added": "text not null",
            },
        )


class AddBookmarkCommand:
    def execute(self, data):
        data["date_added"] = datetime.datetime.utcnow().isoformat()
        db.add("bookmarks", data)
        return "Successfully added a new bookmark!!!"


class ListBookmarksCommand:
    def __init__(self, order_by="date_added"):
        self.order_by = order_by

    def execute(self, criteria):
        return db.select("bookmarks", self.order_by).fetchall()


class DeleteBookmarkCommand:
    def execute(self, data):
        db.delete("bookmarks", {"id": data})
        return "Successfully deleted the bookmark!!!"


class QuitCommand:
    def execute(self):
        sys.exit()
