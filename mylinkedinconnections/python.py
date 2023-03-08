from bs4 import BeautifulSoup
file = open("linkedin2.txt", "r",encoding='utf-8')
contents = file.read()
contents = contents.replace("app-aware-link  update-components-actor__container-link relative display-flex flex-grow-1","jjjjj")
soup = BeautifulSoup(contents, 'html.parser')
# tags = soup.select(".jjjjj")
# tags = soup.find_all("")
tags = soup.find_all("a", class_="jjjjj")

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
for tag in tags:
    file1 = open("items2.html","a")
    item = f'''
    <div class="icon">
    <div class="label">
    </div>
    

    <a href='{tag.get("href")}' target="_blank">
      <button  class="my-button">
          Click Here
      </button>
  </a>
    
    
    </div>
    '''
    items += item 
file1.writelines(items)
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
file1.writelines(footer)
file1.close() 

# Open the file in read mode
# with open('linkedin.txt','r',encoding='utf-8') as file:

#     # Read the contents of the file line by line
#     lines = file.readlines()

#     # Get the fourth line and all subsequent lines
#     selected_lines = lines[3]
#     print(selected_lines)
#     # # Print the selected lines
#     # for line in selected_lines:
#     #     print(line.strip())

        
    