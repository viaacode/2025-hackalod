import requests
req = requests.get('https://api.vam.ac.uk/v2/objects/search?id_person=A11661')

object_data = req.json()
object_info = object_data["info"]
object_records = object_data["records"]
for obj in object_records:
    print(obj["systemNumber"], obj["objectType"])
    print(obj["_images"]["_iiif_image_base_url"]+'full/max/0/default.jpg')
    print(obj["_primaryTitle"])

with open("CreativeWork-VA.nt", "w", encoding="utf-8") as f:
    for obj in object_records:
        f.write("<https://collections.vam.ac.uk/item/" + obj["systemNumber"] + ">" + " a <https://schema.org/CreativeWork> .\n")
        f.write("<https://collections.vam.ac.uk/item/" + obj["systemNumber"] + ">" + " <https://schema.org/name> " + f'"{obj["_primaryTitle"]}"' + " .\n")
        f.write("<https://collections.vam.ac.uk/item/" + obj["systemNumber"] + ">" + " <https://schema.org/url> " + f'"{obj["_images"]["_iiif_image_base_url"]}full/max/0/default.jpg"' + " .\n")
        f.write("<https://collections.vam.ac.uk/item/" + obj["systemNumber"] + ">" + " <https://schema.org/creator> " + "<http://www.wikidata.org/entity/Q12747855> .\n")


record_count = object_info["record_count"]
# print(object_records)


print(f"There are {record_count} objects that mention the term 'Jet' within materials and techniques fields")