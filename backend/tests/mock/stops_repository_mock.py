from backend.domain.bus_stop.bus_stop import BusStop

class StopsRepositoryMock:

    def return_all_stops_impl(self):
        mock_response = [
            BusStop('10100130600640', 'Estacao Move  Barreiro', -19.97477301931237, -44.0220132041767),
            BusStop('10100446100580', 'Estacao Move Senai', -19.90639647366688, -43.94348498583775),
            BusStop('10100446100880', 'Estacao Move Hospital Odilon Behrens', -19.90394540382196, -43.94459982011109)
        ]
        return mock_response

    def return_stop_by_id_impl(self, stop_id):
        if stop_id == '104787000120':
            mock_response = BusStop('104787000120', 'Rua Norte 120', -19.8305153133411, -43.9687279827209)
        else:
            mock_response = 'Invalid Stop ID'
        return mock_response

    def return_all_stops_in_list_impl(self, stops_list):
        if stops_list == ['10100130600640', '10100446100580']:
            mock_response = [
                BusStop('10100130600640', 'Estacao Move  Barreiro', -19.97477301931237, -44.0220132041767),
                BusStop('10100446100580', 'Estacao Move Senai', -19.90639647366688, -43.94348498583775)
            ]
        else:
            mock_response = 'Invalid Stop ID'
        return mock_response