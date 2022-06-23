class RealTimeRepositoryMock:
    
    def get_real_time_bus_coords_impl(self, route_number):
        if(route_number == 394):
            return [
                (-43.962638, -19.908195), 
                (-43.979139, -19.885632), 
                (-43.969587, -19.870928), 
                (-43.979224, -19.885632), 
                (-43.966019, -19.89857), 
                (-43.941044, -19.937846), 
                (-43.960387, -19.864423)]
        return 'Invalid Route Number'
