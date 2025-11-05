import services.services as sv

class SocialMediaFacade:

    def create_poll(self):
        sv.create_poll()

    def create_post(self):
        sv.create_post()

    def list_polls(self):
        sv.list_polls()

    def list_posts(self):
        sv.list_posts()

    def delete_poll(self):
        sv.delete_poll()

    def delete_post(self):
        sv.delete_post()