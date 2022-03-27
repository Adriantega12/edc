import argparse

args = None
data = None

def parse_arguments():
  global args
  parser = argparse.ArgumentParser()
  parser.add_argument("--file-path", dest="file_path", action="store")
  args = parser.parse_args()

def read_file():
  global args
  file_path = args.file_path
  with open(file_path) as file:
    parse_file(file)
      
def parse_file(file):
  global data
  data = {}
  group_name = None
  for line in file:
    raw_data = line.split(" ")
    if (raw_data[0] == "#"):
      group_name = " ".join(raw_data[1:]).replace("\n", "")
      data[group_name] = 0.0
      continue
    
    index = raw_data.index("$") + 1
    data[group_name] += float(raw_data[index].replace(",", ""))

def handle_data():
  global data
  total = 0
  for key in data:
    concept_total = data[key]
    concept_total_str = str("{:.2f}".format(concept_total))
    total += concept_total
    print("{concept}: ${concept_total}".format(
      concept = key, 
      concept_total = concept_total_str,
      )
    )
  print("Total: ${}".format(str(total)))

def main():
  parse_arguments()
  read_file()
  handle_data()

if __name__ == "__main__":
  main()