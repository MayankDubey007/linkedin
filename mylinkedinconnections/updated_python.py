
from bs4 import BeautifulSoup
file = open("linkedin2.txt", "r", encoding='utf-8')
contents = file.read()
contents = contents.replace(
    "app-aware-link  update-components-actor__container-link relative display-flex flex-grow-1", "jjjjj")
contents = contents.replace('''<span class="update-components-actor__supplementary-actor-info t-14 t-normal ml1
              t-black--light">''','''<span class="c_connection">''')
soup = BeautifulSoup(contents, 'html.parser')
# tags = soup.select(".jjjjj")
# tags = soup.find_all("")
tags = soup.find_all("a", class_="jjjjj")
connections = soup.find_all("span", class_="c_connection")

only_connection = []
for connection in tags[:-2]:
  var = connection.find("span",class_="update-components-actor__supplementary-actor-info")
  
  try:
    connection = var.find('span',attrs={'aria-hidden': 'true'}).text[3:6]
    only_connection.append(connection)
  except:
    pass
# print(type(only_connection))
# print(type(list(tags)))

    
with open('items2.html','w') as file:
  head = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>bootstrap-icons</title>

  <style>
    .icons {
      display: grid;
      max-width: 100%;
      grid-template-columns: repeat(auto-fit, minmax(100px, 1fr) );
      gap: 1.25rem;
    }
    .icon {
      background-color: var(--bs-light);
      border-radius: .25rem;
    }
    .bi {
      margin: .25rem;
      font-size: 2.5rem;
    }
    .label {
      font-family: var(--bs-font-monospace);
    }
    .label {
      display: inline-block;
      width: 100%;
      overflow: hidden;
      padding: .25rem;
      font-size: .625rem;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .clicked {
      color: black;
      background-color: red
    }
  </style>

  <link rel="stylesheet" href="/assets/css/bootstrap.min.css">
  <link rel="stylesheet" href="bootstrap-icons.css">
</head>
<body class="text-center">

  <h1>bootstrap-icons</h1>

  <div class="icons">'''
  file.writelines(head)

items =""
def infinite_numbers():
    num = 1
    while True:
        yield num
        num += 1
numbers = infinite_numbers()
for c,t,num in zip(only_connection,tags,numbers):
    item = f'''
    <div class="icon">{c}
    <div class="label"><h1>{num}<h2>
    </div>
    

    <a href='{t.get("href")}' target="_blank">
      <button  class="my-button">
          Click Here
      </button>
  </a>
    
    
    </div>
    '''
    items += item
    # print(c,"&&&&&&&&&&&&&&&&",t)
with open("items2.html", "a") as file:
    file.writelines(items)
    
    footer = '''
</div>
</body>

  <script>
    var buttons = document.getElementsByClassName("my-button");
    
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].addEventListener("click", function() {

        this.classList.add("clicked");
      });
    }
  </script>

</html>'''
    file.writelines(footer)
    file.close() 
