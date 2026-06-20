
from db.mongodb import connection
from settings import Settings
from typing import Type, TypeVar
from loguru import logger

_database = connection.get_database(Settings.DATABASE_NAME)

TypeOfUser = TypeVar("T", bound="UserDocument")

class UserDocument():
    first_name: str
    last_name: str

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    @classmethod
    def from_mongo(cls: Type[TypeOfUser], data: dict) -> TypeOfUser:
        """Convert "_id" (str object) into "id" (UUID object)."""

        if not data:
            raise ValueError("Data is empty.")

        id = data.pop("_id")

        return cls(**dict(data, id=id))


    @classmethod
    def get_or_create(cls: Type[TypeOfUser], **filter_options) -> TypeOfUser:
        collection = _database[cls.get_collection_name()]
        try:
            #if in MongoDB exists a document
            instance = collection.find_one(filter_options)
            if instance:
                return cls.from_mongo(instance)

            new_instance = cls(**filter_options)
            new_instance = new_instance.save()

            return new_instance
        except Exception:
            logger.exception(f"Failed to retrieve document with filter options: {filter_options}")

            raise