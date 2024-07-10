from lib.bookings import Bookings

class BookingsRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        
    def get_all(self):
        rows = self.db_connection.execute("SELECT * FROM bookings")
        print(rows)
        return [Bookings(row['id'], row['spaces_id'], row['requester_id'], row['requested_dates'], row['status']) for row in rows]
    
    def create(self, Bookings):
        self.db_connection.execute("INSERT INTO Bookings(spaces_id, requester_id, requested_dates, status) VALUES (%s, %s, %s, %s)", [Bookings.spaces_id, Bookings.requester_id, Bookings.requested_dates, Bookings.status])
      
    def get_by_id(self,id):
        rows = self.db_connection.execute("SELECT * FROM bookings WHERE id = %s",[id])
        return Bookings(rows[0]['id'], rows[0]['spaces_id'], rows[0]['requester_id'], rows[0]['requested_dates'], rows[0]['status'])

    def delete(self, id):
        self.db_connection.execute("DELETE FROM bookings WHERE id = %s", [id])
    
    def get_by_spaces_id(self, spaces_id):
        rows = self.db_connection.execute("SELECT * FROM bookings WHERE spaces_id = %s",[spaces_id])
        return [Bookings(row['id'], row['spaces_id'], row['requester_id'], row['requested_dates'], row['status']) for row in rows]
    
    def get_by_requester_id(self, requester_id):
        rows = self.db_connection.execute("SELECT * FROM bookings WHERE requester_id = %s",[requester_id])
        return [Bookings(row['id'], row['spaces_id'], row['requester_id'], row['requested_dates'], row['status']) for row in rows]
    
    def get_by_status(self, status):
        rows = self.db_connection.execute("SELECT * FROM bookings WHERE status = %s",[status])
        return [Bookings(row['id'], row['spaces_id'], row['requester_id'], row['requested_dates'], row['status']) for row in rows]
    
    def approve(self,id):
        self.db_connection.execute("UPDATE bookings SET status = 'Approved' WHERE id = %s",[id])

    def reject(self,id):
        self.db_connection.execute("UPDATE bookings SET status = 'Rejected' WHERE id = %s",[id])
        