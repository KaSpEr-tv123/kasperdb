import json

class Json:
  @staticmethod
  def get(filename):
    with open(filename, encoding="utf-8") as infile:
      return json.load(infile)


  @staticmethod
  def set(filename, content):
    with open(filename, "w") as outfile:
      json.dump(content, outfile, ensure_ascii=True, indent=2)