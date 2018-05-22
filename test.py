#!/usr/bin/python3

# Turn on debug mode.

import cgitb
cgitb.enable()

# Print necessary headers.
# print("Content-Type: text/html")
# print()

# Connect to the database.
import pymysql
conn = pymysql.connect(
    db='example',
    user='root',
    passwd='12345678',
    host='localhost')
c = conn.cursor()

# Insert some example data.
# c.execute("SELECT * FROM numbers")
# l = len(c.fetchall())
# c.execute("INSERT INTO numbers VALUES ("+str(l)+", 'Hurray!')")
# conn.commit()

# Print the contents of the database.
# c.execute("SELECT * FROM numbers")
# print([(r[0], r[1]) for r in c.fetchall()])

# Print HTML body
import webapp2
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
            <html>
            <head>
            <meta charset="utf-8">
            <title>選歌系統</title>

            <script>
            	function check(){
            		var user,passw;
            		user=document.getElementById("user").value;
            		passw=document.getElementById("pwd").value;
            		if(user=="" || passw ==""){
            	  		alert("Account or Password Can not be blank !");
            		}else{
            			document.getElementById("login").submit();
            		}
             	}
            	function signin(){
            		var user,passw;
            		user=document.getElementById("user").value;
            		passw=document.getElementById("pwd").value;
            		if(user=="" || passw ==""){
            	  		alert("Account or Password Can not be blank !");
            		}else{
            			document.getElementById("signin").submit();
            		}
             	}
            	function Inputsong(){

             	}
            	function Selectsong(){

             	}

              </script>

            </head>
            <body>

            <tr height=200><td width=200 align=center >             <! 登入>
            <form method=post action=Login.php id="login" align="center">
            	 會員登入<p>
            	帳號  : <input type=text id=user name=user size=10 ><p>
            	密碼 :<input type=password id=pwd name=pwd size=10><p>
            <p>
            	<input type=button value=送出 onclick="check()">&nbsp;
            	<input type=reset  value="重設" >&nbsp;
            	<input type=button value="註冊" id="signin" onClick="signin()" >
            </form>
            	</form></td></tr>

            <tr height=200><td width=200 align=center >              <! 放歌曲>
            <form method=post action=inputsong.php id="inputsong">
            	 放入歌曲<p>
            	歌曲名稱 : <input type=text id=songname name=songname size=10 >
            	歌手/樂團/教會 :<input type=text id=band name=band size=10>
            	主題性質 :<input type=text id=theme name=theme size=10>
            	歌曲Key :<input type=text id=key name=key size=10>
            	歌曲最高音 :<input type=text id=highest name=highest size=10>
            	歌曲最低音 :<input type=text id=bass name=bass size=10><p>
            <p>
            	<input type=button value=放入 onclick="Inputsong()">
            	<input type=reset value="重設" >
            </form>

            	<tr height=200><td width=200 align=center >              <! 搜尋歌曲>
            <form method=get action=selectsong.php id="selectsong">
            	 尋找歌曲<p>
            	歌曲名稱 : <input type=text id=songname name=songname size=10 >
            	歌手/樂團/教會 :<input type=text id=band name=band size=10>
            	主題性質 :<input type=text id=theme name=theme size=10>
            	歌曲Key :<input type=text id=key name=key size=10>
            	歌曲最高音 :<input type=text id=highest name=highest size=10>
            	歌曲最低音 :<input type=text id=bass name=bass size=10><p>
            <p>
            	<input type=button value=搜尋 onclick="Selectsong()">
            	<input type=reset value="重設" >
            </form>

            </body>
            </html>""")


class Greeting(webapp2.RequestHandler):
    def post(self):
        username = self.request.get("my_name")
        welcome_string = """<html><body>
                          Hi there, {}!
                          </body></html>""".format(username)
        self.response.headers["Content-Type"] = "text/html"
        self.response.write(welcome_string)


routes = [('/', MainPage), ('/welcome', Greeting)]
my_app = webapp2.WSGIApplication(routes, debug=True)
