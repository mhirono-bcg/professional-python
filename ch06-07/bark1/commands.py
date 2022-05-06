import datetime
import sys
import requests
from database import DatabaseManager
from abc import ABC, abstractmethod

db = DatabaseManager("bookmarks.db")


class Command(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError("コマンドは必ずメソッドexecuteを実装してください")


class CreateBookmarksTableCommand(Command):
    def execute(self, data=None):
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


class AddBookmarkCommand(Command):
    def execute(self, data, timestamp=None):
        data["date_added"] = timestamp or datetime.datetime.utcnow().isoformat()
        db.add("bookmarks", data)
        return True, None


class ListBookmarksCommand(Command):
    def __init__(self, order_by="date_added"):
        self.order_by = order_by

    def execute(self, data=None):
        return True, db.select("bookmarks", self.order_by).fetchall()


class DeleteBookmarkCommand(Command):
    def execute(self, data):
        db.delete("bookmarks", {"id": data})
        return "Successfully deleted the bookmark!!!"


class QuitCommand(Command):
    def execute(self, data=None):
        sys.exit()


class ImportGitHubStarsCommand(Command):
    def _extract_bookmark_info(self, repo):
        return {
            "title": repo["name"],
            "URL": repo["html_url"],
            "memo": repo["description"],
        }

    def execute(self, data):
        bookmarks_imported = 0
        github_username = data["github_username"]
        next_page_of_results = f"https://api.github.com/users/{github_username}/starred"

        while next_page_of_results:
            stars_response = requests.get(
                next_page_of_results,
                headers={"Accept": "application/vnd.github.v3.star+json"},
            )
            next_page_of_results = stars_response.links.get("next", {}).get("url")

            for repo_info in stars_response.json():
                repo = repo_info["repo"]

                if data["preserve_timestamps"]:
                    timestamp = datetime.strptime(
                        repo_info["starred_at"], "%Y-%m-%dT%H:%M:%SZ"
                    )
                else:
                    timestamp = None
                bookmarks_imported += 1
                AddBookmarkCommand.execute(
                    self._extract_bookmark_info(repo), timestamp=timestamp
                )
        return f"{bookmarks_imported} Bookmarks are now imported!!!"


class EditBookmarkCommand(Command):
    def execute(self, data):
        db.update("bookmarks", {"id": data["id"]}, data["update"])
        return "Update the Bookmarks!!!"
