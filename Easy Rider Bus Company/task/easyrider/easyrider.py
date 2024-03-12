import json
from collections import defaultdict


class BusCompany:
    def __init__(self, data: str) -> None:
        self.data = json.loads(data).get("data", [])
        self.stops = defaultdict(list)
        self.arrival_times = defaultdict(list)

    def find_stop_types(self):
        for instance in self.data:
            self.stops[instance["stop_name"]].append(instance["stop_type"])

    def on_demand_stop_test(self):
        self.find_stop_types()
        print("On demand stops test:")
        ok = True
        wrong_stops = []
        for key, value in self.stops.items():
            if len(value) > 1 and 'O' in value:
                wrong_stops.append(key)
                ok = False
        print(f"Wrong stop type: {sorted(wrong_stops)}" if not ok else "OK")


if __name__ == "__main__":
    input_data = '{"data": ' + input() + '}'
    bus_company = BusCompany(input_data)
    bus_company.on_demand_stop_test()
