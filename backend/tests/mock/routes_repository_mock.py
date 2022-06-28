from backend.domain.route.bus_departure import BusDeparture
from backend.domain.route.route import Route
import datetime

class RoutesRepositoryMock:
    
    def return_trips_from_route_impl(self, route_id):
        if(route_id == '609-01'):
            return [
                BusDeparture(datetime.time(7, 10), '609-01', '112845400545', '609   011010130710'),
                BusDeparture(datetime.time(9, 10), '609-01', '112845400545', '609   011010130910'),
                BusDeparture(datetime.time(14, 40), '609-01', '112845400545', '609   011010130910')
            ]
        return 'Invalid Route'

    def return_one_route_by_id_impl(self, route_id):
        if(route_id == '609-01'):
            return Route('609-01', '609', 'Serra Verde/Santa Monica (Principal)', '609-01I', '112845400545', '112845400545')
        if(route_id == '609-02'):
            return Route('609-02', '609', 'Serra Verde/Santa Monica (Cid.Admin-Sentido Serra Verde)', '609-02I', '112845400545', '112845400545')
        if(route_id == '609-03'):
            return Route('609-03', '609', 'Serra Verde/Santa Monica (Cid.Admin-Sentido Sta Monica)', '609-03I', '112845400545', '112845400545')
        return 'Invalid Route'
    
    def return_route_conversion_impl(self, route_id):
        if(route_id == '5102-01'):
            return 394
        return 'Invalid Route'

    def return_all_routes_impl(self):
        return [
            Route('4801A-01', '4801A', 'Jardim Filadelfia/Boa Vista A (Principal)', '4801A-01I', '109207300780', '106312000753'),
            Route('9550-01', '9550', 'Casa Branca/Sao Francisco Via Est. Jose Candido (Principal)', '9550-01I', '111617000759', '106161701501'),
            Route('4205-01', '4205', 'Ermelinda/Salgado Filho (Principal)', '4205-01V', '100213500140', '108136000278')
        ]

    def return_route_by_id_impl(self, route_id):
        if(route_id == '609-03'):
            return Route('609-03', '609', 'Serra Verde/Santa Monica (Cid.Admin-Sentido Sta Monica)', '609-03I', '112845400545', '112845400545')
        return 'Invalid Route'