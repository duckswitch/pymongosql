# coding: utf-8
"""
This file contains AbstractSerializer class.
"""
from .abstract_api_serializer import AbstractApiSerializer
from pymongosql.serializer.api.api_serializer_types import (
    Value,
    Field,
    Operator
)

class MongodbSerializer(AbstractApiSerializer):
    """
    Defines the MongoDB Api serializer.
    """

    def decode_query(self, filters, parent=None):
        """
        Parse a filter from the API.
        Args:
            filters (dict): The filters to parse.
            parent (unicode): The parent operator to join filters ($and or $or).
        """
        if not parent:
            parent = Operator(u"and")

        if not isinstance(filters, list):
            filters = [filters]
        
        translated = []

        for filt in filters:
            for key, value in filt.items():
                translated += [Field(key), Operator(u"="), Value(value)]

        return translated
