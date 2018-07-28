# -*- coding: utf-8 -*-

"""
# import os
# import json
import requests
from utilities.logs import get_logger

log = get_logger(__name__)
log.debug("Package: %s", requests.__name__)
log.info("Hello world!")
"""

import graphene


class Query(graphene.ObjectType):
    hello = graphene.String()
    test = graphene.Int()

    def resolve_hello(self, info):
        return 'World'

    def resolve_test(self, info):
        return 3


schema = graphene.Schema(query=Query)

results = schema.execute('''
  query {
    hello
    test
  }
''')

print(results.data)
