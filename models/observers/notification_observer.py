from .observer_interfaces import Observer
from models.models import Post, Poll

class NotificationObserver(Observer):
    def update(self, subject):
        if isinstance(subject, Post):
            print(f"\n[NOTIFICATION]: New Post created: '{subject.title}'")
        elif isinstance(subject, Poll):
            print(f"\n[NOTIFICATION]: New Poll created: '{subject.title}'")
        else:
            print(f"\n[NOTIFICATION]: New social event added.")