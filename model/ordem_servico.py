import json
class OrdemServicoModel:
    def __init__(self, title, geojson, lat, lng, relator, date, status):
        self.title = title
        self.geojson = geojson
        self.lat = lat
        self.lng = lng
        self.relator = relator
        self.date = date
        self.status = status
        
    @classmethod
    def json_para_ordem_servico(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(
            json_dict['title'],
            json_dict['geojson'],
            json_dict['lat'],
            json_dict['lng'],
            json_dict['relator'],
            json_dict['date'],
            json_dict['status']
        )





