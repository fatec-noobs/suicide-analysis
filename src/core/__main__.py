from more_itertools import seekable

from src.core.suicide_data_service import SuicideDataService

service = SuicideDataService({'Arquivos': ['obtsp11.dbf', 'obtsp05.dbf', 'obtsp00.dbf']})
print(service.search())