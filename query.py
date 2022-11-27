import pymongo
import webbrowser

client = pymongo.MongoClient("mongodb+srv://root:mongoPass@cluster0.ddvbnxo.mongodb.net/?retryWrites=true&w=majority")
mydb = client["test"]
mycol = mydb["users"]

student = []

tbl = "<tr><td>Name</td><td>Str</td><td>Con</td><td>Dex</td><td>Wis</td><td>Int</td><td>Cha</td></tr>"
student.append(tbl)

for y in mycol.find({'userName': 'me'}):
    a = "<tr><td>%s</td>"%y['name']
    student.append(a)
    b = "<td>%s</td>"%y['str']
    student.append(b)
    c = "<td>%s</td>"%y['con']
    student.append(c)
    d = "<td>%s</td>"%y['dex']
    student.append(d)
    e = "<td>%s</td>"%y['wis']
    student.append(e)
    f = "<td>%s</td>"%y['int']
    student.append(f)
    g = "<td>%s</td></tr>"%y['cha']
    student.append(g)

contents = '''<!DOCTYPE html>
<html>
    <style>
            .topnav {
                background-color: #333;
                overflow: hidden;
            }

            /* Style the links inside the navigation bar */
            .topnav a {
                float: left;
                color: #f2f2f2;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
                font-size: 17px;
            }

            /* Change the color of links on hover */
            .topnav a:hover {
                background-color: #ddd;
                color: black;
            }

            /* Add a color to the active/current link */
            .topnav a.active {
                background-color: #04AA6D;
                color: white;
            }
    </style>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title>Python Webbrowser</title>
</head>
<nav class="topnav">
        <a href='pages/home.html'>Home</a>
        <a href='pages/index.html'>Roll Stats</a>
        <a class="active" href='pages/grab.html'>Retrieve Character</a>
    </nav>
<body>
<table>
%s
</table>
</body>
</html>
'''%(student)

filename = 'info.html'

def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

main(contents, filename)    
webbrowser.open(filename)