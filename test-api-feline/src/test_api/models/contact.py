from test_api.models.base_model_ import Model


class Contact(Model):
    def __init__(self, email, stadt_plz, bundesland_heimat, instagram, facebook):
        self.swagger_types = {'email': str, stadt_plz: int, bundesland_heimat: str, instagram: str, facebook: str}
        self.attribute_map = {"email": "email",
                              "stadt_plz": "stadt_plz",
                              "bundesland_heimat": "bundesland_heimat",
                              "instagram": "instagram",
                             "facebook": "facebook"}

        self.email = email
        self.stadt_plz = stadt_plz
        self.instagram = instagram
        self.facebook = facebook
        self.bundesland_heimat = bundesland_heimat
