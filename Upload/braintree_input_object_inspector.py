import requests

BRAINTREE_TOKEN = "YOUR_BRAINTREE_TOKEN"
ENDPOINT = "https://payments.sandbox.braintree-api.com/graphql"
HEADERS = {
    "Authorization": f"Bearer {BRAINTREE_TOKEN}",
    "Content-Type": "application/json",
    "Braintree-Version": "2019-01-01"
}

def fetch_mutations():
    query = '''
    {
      __schema {
        mutationType {
          fields {
            name
            args {
              name
              type {
                kind
                name
                ofType {
                  kind
                  name
                }
              }
            }
          }
        }
      }
    }
    '''
    response = requests.post(ENDPOINT, json={"query": query}, headers=HEADERS)
    response.raise_for_status()
    return response.json()["data"]["__schema"]["mutationType"]["fields"]

def introspect_input_object(name):
    query = '''
    query GetInputObjectDetails($name: String!) {
      __type(name: $name) {
        name
        kind
        inputFields {
          name
          type {
            kind
            name
            ofType {
              kind
              name
              ofType {
                kind
                name
              }
            }
          }
        }
      }
    }
    '''
    response = requests.post(ENDPOINT, json={"query": query, "variables": {"name": name}}, headers=HEADERS)
    response.raise_for_status()
    return response.json()["data"]["__type"]

def print_input_object_details():
    mutations = fetch_mutations()
    seen = set()
    for mutation in mutations:
        for arg in mutation["args"]:
            arg_type = arg["type"]
            type_kind = arg_type["kind"]
            type_name = arg_type["name"] or (arg_type["ofType"] or {}).get("name")

            if type_kind == "NON_NULL":
                arg_type = arg_type["ofType"]
                type_kind = arg_type["kind"]
                type_name = arg_type["name"]

            if type_kind == "INPUT_OBJECT" and type_name and type_name not in seen:
                seen.add(type_name)
                obj = introspect_input_object(type_name)
                print(f"Input Object: {obj['name']}")
                for field in obj["inputFields"]:
                    f_type = field["type"]
                    required = f_type["kind"] == "NON_NULL"
                    print(f"  - {field['name']} {'(required)' if required else ''}")
                print()

if __name__ == "__main__":
    print_input_object_details()
