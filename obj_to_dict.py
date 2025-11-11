
import json

class Handler:
    def __init__(self):
        self.Master = [] 


class objects:
    def __init__(self,num):
        self.number = num
        self.attr2 = "uid"
        self.attr3 = "phome"
        self.attr4 = 45645
        self.attr5 = [1,2,3,4]

    def flatten(self):
        obj_dict = {
            "number" : self.number,
             "shalom" : self.attr2,
             "od_shem" : self.attr3,
             "sem" : self.attr4,
             "aharon" : self.attr5,
                             }
        return obj_dict


master = Handler()

for i in range(15,50):
    master.Master.append(objects(i))

# print(master.Master[30].number)
master_dict = []

for obj in master.Master:
    flattened = obj.flatten()
    master_dict.append(flattened)

print(master_dict)

def save_to_json(data, filename):
    """
    Save Python data to a JSON file.
    
    Args:
        data (dict | list): Data to save (must be JSON serializable).
        filename (str): Path to the JSON file.
    """
        
    # Write JSON with indentation and UTF-8 encoding
    with open(filename, "w") as f:
        json.dump(data, f,indent=4)
    
    print(f"Data successfully saved to '{filename}'")


save_to_json(master_dict, "output.json")
