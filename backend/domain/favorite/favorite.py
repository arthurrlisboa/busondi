class Favorite:
    id = ''
    email = ''
    route_id = ''
    stop_id = ''
    time = ''

    def __init__(self, email, route_id, stop_id, id=None, time=None):
        self.email = email
        self.route_id = route_id
        self.stop_id = stop_id

        if(id is None):
            self.id = ''
        else:
            self.id = id

        if(time is None):
            self.time = ''
        else:
            self.time = time