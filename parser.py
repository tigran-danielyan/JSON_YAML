import json
import yaml


def json_to_yaml_parser(json_file,yaml_file):
    
    if len(json_file) == 0 or len(yaml_file) == 0:
        raise ValueError("File name can't be empty") 

    # JSON file managment
    try:
        with open(json_file,"r") as file_to_convert:
            data = json.load(file_to_convert)
            file_to_convert.close()

        with open(yaml_file, "w") as file_to_fill:
            yaml.dump(data,file_to_fill,sort_keys=False)
            file_to_fill.close() 

        return "\nDone"

    except FileNotFoundError:
        return F"JSON file with name {json_file} isn't found"
    except json.JSONDecodeError:
        return "The Json file is misconfigured"
    except:
        return "Something went wrong"



print("\nJSON TO YAML convertor\n")

json_file_name = input("Input JSON file name:(ex. some_json.json) ")
yaml_file_name = input("Input YAML file name:(ex. some_yaml.yml or some_yaml.yaml) ")
  
result = json_to_yaml_parser(json_file_name,yaml_file_name)

print(result)


