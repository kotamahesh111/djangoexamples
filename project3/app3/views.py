from django.http import HttpResponse
def showindex(httprequest):
    message='''
    <html>
    <body>
        <form action="#">
            <input type="password" placeholder="password" pattern="^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s).*$" required><br><br>
            <input type="file"><br><br>
            <input type="search" placeholder="search"><br><br>
            <input type="range"><br><br>
            <textarea placeholder="address" rows="4" cols="4"></textarea><br><br>
            <button type="submit">Register</button>
        </form>
    </body>
</html>
    '''
    return HttpResponse(message)