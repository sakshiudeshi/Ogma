import API_KEYS
from uclassify import uclassify

a = uclassify()
a.setReadApiKey(str(API_KEYS.UCLASSIFY_API_KEY_READ))
a.setWriteApiKey(str(API_KEYS.UCLASSIFY_API_KEY_WRITE))
# print str(API_KEYS.UCLASSIFY_API_KEY)

a.create("IABTaxonomyV2")

d = a.classify(["sample text1","sample text2"],"IABTaxonomyV2")