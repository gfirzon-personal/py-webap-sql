from factories.connection_factory import ConnectionFactory


class VendorService:
    @staticmethod
    def get_vendors():
        try:
            conn = ConnectionFactory.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Vendors")  # Adjust the query as needed
            rows = cursor.fetchall()
            return [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
        except Exception as e:
            raise e
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_vendor_by_id(vendor_id):
        try:
            conn = ConnectionFactory.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Vendors WHERE VendorID = ?", vendor_id)  # Adjust the query as needed
            row = cursor.fetchone()
            if row:
                return dict(zip([column[0] for column in cursor.description], row))
            else:
                return None
        except Exception as e:
            raise e
        finally:
            if conn:
                conn.close()

    @staticmethod
    def create_vendor(vendor_data):
        try:
            conn = ConnectionFactory.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Vendors (VendorName, VendorPhone, Email) OUTPUT INSERTED.VendorID VALUES (?, ?, ?)",
                vendor_data['Name'], vendor_data['Phone'], vendor_data['Email']
            )
            row = cursor.fetchone()
            conn.commit()
            return row[0] if row else None
        except Exception as e:
            raise e
        finally:
            if conn:
                conn.close()

    @staticmethod
    def update_vendor(vendor_id, vendor_data):
        try:
            conn = ConnectionFactory.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE Vendors SET VendorName = ?, VendorPhone = ?, Email = ? WHERE VendorID = ?",
                vendor_data['Name'], vendor_data['Phone'], vendor_data['Email'], vendor_id
            )
            conn.commit()
            return cursor.rowcount  # Returns the number of rows updated
        except Exception as e:
            raise e
        finally:
            if conn:
                conn.close()