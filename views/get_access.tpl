<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Capa</title>
</head>
<body>
    <p>
        Ok, almost finished <br>
        your ip {{ip}} <br>
        your mac {{mac}} <br>
        your passkode {{passkode}} <br>
    </p>
    <p>
        Now enter your code in form: <br>
        <form action="/go/{{phone}}" method="post">
            <input type="text" name="passkode"> <br>
            <input type="submit" name="submit" value="Finish">
        </form>
    </p>
</body>
</html>
