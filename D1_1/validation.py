import json
import os
import sys
import jsonschema

if len(sys.argv) > 1:
    resolver = jsonschema.RefResolver('file://%s/' % os.path.abspath(os.path.dirname(__file__)), None)
else:
    resolver = None

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

file1 = os.path.join(__location__, 'array2.schema.json')
file2 = os.path.join(__location__, 'array3.schema.json')

with open(os.path.join(__location__, 'coordinates.json')) as fp:
    json_document = json.load(fp)

with open(os.path.join(__location__, 'coordinates.schema.json')) as fp:
    schema = json.load(fp)

resolver1 = jsonschema.RefResolver(file1, file2, store=(), cache_remote=False, handlers=(), urljoin_cache=None, remote_cache=None)
try:
    jsonschema.validate(json_document, schema, resolver=resolver)
    print("Passed base schema.")
except Exception as ex:
    print("Failed base schema: %s" % ex)

#try:
  #  jsonschema.validate(data, derived, resolver=resolver)
   # print("Passed derived schema.")
#except Exception as ex:
 #   print("Failed derived schema: %s" % ex)