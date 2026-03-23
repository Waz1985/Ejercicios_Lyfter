from database import SessionLocal
from models import User, Address, Car


class UserManager:
    def create_user(self, name, email):
        session = SessionLocal()
        try:
            user = User(name=name, email=email)
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def update_user(self, user_id, name=None, email=None):
        session = SessionLocal()
        try:
            user = session.get(User, user_id)
            if not user:
                return None

            if name is not None:
                user.name = name
            if email is not None:
                user.email = email

            session.commit()
            session.refresh(user)
            return user
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete_user(self, user_id):
        session = SessionLocal()
        try:
            user = session.get(User, user_id)
            if not user:
                return False

            session.delete(user)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_all_users(self):
        session = SessionLocal()
        try:
            return session.query(User).all()
        finally:
            session.close()


class AddressManager:
    def create_address(self, street, city, country, user_id):
        session = SessionLocal()
        try:
            user = session.get(User, user_id)
            if not user:
                raise ValueError("User doesn't exists")

            address = Address(
                street=street,
                city=city,
                country=country,
                user_id=user_id
            )
            session.add(address)
            session.commit()
            session.refresh(address)
            return address
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def update_address(self, address_id, street=None, city=None, country=None, user_id=None):
        session = SessionLocal()
        try:
            address = session.get(Address, address_id)
            if not address:
                return None

            if user_id is not None:
                user = session.get(User, user_id)
                if not user:
                    raise ValueError("User doesn't exists")
                address.user_id = user_id

            if street is not None:
                address.street = street
            if city is not None:
                address.city = city
            if country is not None:
                address.country = country

            session.commit()
            session.refresh(address)
            return address
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete_address(self, address_id):
        session = SessionLocal()
        try:
            address = session.get(Address, address_id)
            if not address:
                return False

            session.delete(address)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_all_addresses(self):
        session = SessionLocal()
        try:
            return session.query(Address).all()
        finally:
            session.close()


class CarManager:
    def create_car(self, brand, model, plate, user_id=None):
        session = SessionLocal()
        try:
            if user_id is not None:
                user = session.get(User, user_id)
                if not user:
                    raise ValueError("User doesn't exists")

            car = Car(
                brand=brand,
                model=model,
                plate=plate,
                user_id=user_id
            )
            session.add(car)
            session.commit()
            session.refresh(car)
            return car
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def update_car(self, car_id, brand=None, model=None, plate=None, user_id=None):
        session = SessionLocal()
        try:
            car = session.get(Car, car_id)
            if not car:
                return None

            if brand is not None:
                car.brand = brand
            if model is not None:
                car.model = model
            if plate is not None:
                car.plate = plate

            if user_id is not None:
                user = session.get(User, user_id)
                if not user:
                    raise ValueError("User doesn't exists")
                car.user_id = user_id

            session.commit()
            session.refresh(car)
            return car
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete_car(self, car_id):
        session = SessionLocal()
        try:
            car = session.get(Car, car_id)
            if not car:
                return False

            session.delete(car)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def assign_car_to_user(self, car_id, user_id):
        session = SessionLocal()
        try:
            car = session.get(Car, car_id)
            if not car:
                raise ValueError("Car doesn't exists")

            user = session.get(User, user_id)
            if not user:
                raise ValueError("User doesn't exists")

            car.user_id = user_id
            session.commit()
            session.refresh(car)
            return car
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_all_cars(self):
        session = SessionLocal()
        try:
            return session.query(Car).all()
        finally:
            session.close()