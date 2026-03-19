from database import engine, Base
import models
from managers import UserManager, AddressManager, CarManager


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables verified/created correctly.")

def run_demo():
    user_manager = UserManager()
    address_manager = AddressManager()
    car_manager = CarManager()

    user1 = user_manager.create_user("Wilmer", "wilmer@email.com")
    user2 = user_manager.create_user("Ana", "ana@email.com")

    print("\nCreated Users:")
    print(user1)
    print(user2)

    address1 = address_manager.create_address("Calle 1", "Heredia", "Costa Rica", user1.id)
    address2 = address_manager.create_address("Avenida 2", "San José", "Costa Rica", user2.id)

    print("\nCreated Addresses:")
    print(address1)
    print(address2)

    car1 = car_manager.create_car("Toyota", "Corolla", "ABC123")
    car2 = car_manager.create_car("Honda", "Civic", "XYZ789", user1.id)

    print("\nCreated Cars:")
    print(car1)
    print(car2)

    car_manager.assign_car_to_user(car1.id, user2.id)

    print("\nAll Users:")
    for user in user_manager.get_all_users():
        print(user)

    print("\nAll Cars:")
    for car in car_manager.get_all_cars():
        print(car)

    print("\nAll Addresses:")
    for address in address_manager.get_all_addresses():
        print(address)


if __name__ == "__main__":
    create_tables()
    run_demo()