# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Child class (Smartphone inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera):
        # Call parent constructor
        super().__init__(brand, model)
        self.storage = storage
        self.camera = camera

    def make_call(self, number):
        return f"Calling {number} from {self.device_info()}..."

    def take_photo(self):
        return f"📸 Taking a photo with {self.camera} camera!"


# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S24", "256GB", "108MP")
phone2 = Smartphone("Apple", "iPhone 15", "512GB", "48MP")

# Using methods
print(phone1.make_call("+254712345678"))
print(phone2.take_photo())
