from factories.connection_factory import ConnectionFactory
from models.vendor_model import VendorModel

class VendorService:
    @staticmethod
    def get_vendors() -> list[VendorModel]:
        try:
            conn = ConnectionFactory.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Vendors")  # Adjust the query as needed
            rows = cursor.fetchall()
            return [VendorModel(**dict(zip([column[0] for column in cursor.description], row))) for row in rows]
        except Exception as e:
            raise e
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_vendor_by_id(vendor_id) -> VendorModel | None:
        try:
            conn = ConnectionFactory.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Vendors WHERE VendorID = ?", vendor_id)  # Adjust the query as needed
            row = cursor.fetchone()
            if row:
                # The ** is Python's dictionary unpacking operator.
                return VendorModel(**dict(zip([column[0] for column in cursor.description], row)))
            else:
                return None
        except Exception as e:
            raise e
        finally:
            if conn:
                conn.close()

    @staticmethod
    def create_vendor(vendor: VendorModel):
        try:
            conn = ConnectionFactory.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Vendors (VendorName, VendorPhone, Email) OUTPUT INSERTED.VendorID VALUES (?, ?, ?)",
                vendor.VendorName, vendor.VendorPhone, vendor.Email
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
    def update_vendor(vendor: VendorModel):
        try:
            conn = ConnectionFactory.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE Vendors SET VendorName = ?, VendorPhone = ?, Email = ? WHERE VendorID = ?",
                vendor.VendorName, vendor.VendorPhone, vendor.Email, vendor.VendorID
            )
            conn.commit()
            return cursor.rowcount  # Returns the number of rows updated
        except Exception as e:
            raise e
        finally:
            if conn:
                conn.close()

    @staticmethod
    def delete_vendor(vendor_id):
        try:
            conn = ConnectionFactory.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Vendors WHERE VendorID = ?", vendor_id)
            conn.commit()
            return cursor.rowcount  # Returns the number of rows deleted
        except Exception as e:
            raise e