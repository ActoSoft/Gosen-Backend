from accounts.models import Profile


class Client(Profile):

    def __str__(self):
        return self.user.first_name
