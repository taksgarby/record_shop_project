import pdb
from models.artist import Artist
from models.record import Record

import repositories.artist_repository as artist_repository
import repositories.record_repository as record_repository

record_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist('Joni', 'Mitchell', 'Canada')
artist_repository.save(artist1)
artist2 = Artist('Fiona', 'Apple', 'USA')
artist_repository.save(artist2)
artist3 = Artist('John', 'Coltrane', 'USA')
artist_repository.save(artist3)
artist4 = Artist('Henri', 'Salvador', 'France')
artist_repository.save(artist4)

record1 = Record('Blue', artist1, 'Folk', 1971, 15.00, 30.00)
record_repository.save(record1)
record2 = Record('Extraordinary Machine', artist2, 'Pop & Rock', 2005, 10.50, 20.00)
record_repository.save(record2)
record3 = Record('Room With A View', artist4, 'Jazz', 2000, 13.50, 25.00)
record_repository.save(record3)
record4 = Record('Blue Train', artist3, 'Jazz', 2022, 15.50, 35.00)
record_repository.save(record4)
record5 = Record('Both Sides Now', artist1, 'Folk', 12.00, 25.00)
record_repository.save(record5)