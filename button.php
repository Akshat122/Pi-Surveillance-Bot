<?php
$file1 = "buttonStatus1.txt";
$file2 = "buttonStatus2.txt";
$file3 = "buttonStatus3.txt";
$file4 = "buttonStatus4.txt";


if (isset($_POST['on1']))
{
$handle = fopen($file1,'w+');
$onstring = "ON";
fwrite($handle,$onstring);
fclose($handle);

print "
<html>
<body>
<title>Home Automation</title>
<style type=text/css>
h1{
	padding-left: 50px;
}
h2{
	padding-left: 50px;
}
</style>
<h1>Home Automation</h2>
<h2>Device Turned ON </h2>
</body>
</html>

";
header( "refresh:3; index.html" );
}
else if(isset($_POST['off1']))
{
$handle = fopen($file1,'w+');
$offstring = "OFF";
fwrite($handle, $offstring);
fclose($handle);
print "
<html>
<body>
<title>Home Automation</title>
<style type=text/css>
h1{
	padding-left: 50px;
}
h2{
	padding-left: 50px;
}
</style>
<h1>Home Automation</h2>
<h2>Device Turned OFF </h2>
</body>
</html>

";
header( "refresh:3; index.html" );
}

else if (isset($_POST['on2']))
{
$handle = fopen($file2,'w+');
$onstring = "ON";
fwrite($handle,$onstring);
fclose($handle);
print "
<html>
<body>
<title>Home Automation</title>
<style type=text/css>
h1{
	padding-left: 50px;
}
h2{
	padding-left: 50px;
}
</style>
<h1>Home Automation</h2>
<h2>Device Turned ON </h2>
</body>
</html>
";
header( "refresh:3; index.html" );
}
else if(isset($_POST['off2']))
{
$handle = fopen($file2,'w+');
$offstring = "OFF";
fwrite($handle, $offstring);
fclose($handle);
print "
<html>
<body>
<title>Home Automation</title>
<style type=text/css>
h1{
	padding-left: 50px;
}
h2{
	padding-left: 50px;
}
</style>
<h1>Home Automation</h2>
<h2>Device Turned OFF </h2>
</body>
</html>
";
header( "refresh:3; index.html" );
}

else if (isset($_POST['on3']))
{
$handle = fopen($file3,'w+');
$onstring = "ON";
fwrite($handle,$onstring);
fclose($handle);
print "
<html>
<body>
<title>Home Automation</title>
<style type=text/css>
h1{
	padding-left: 50px;
}
h2{
	padding-left: 50px;
}
</style>
<h1>Home Automation</h2>
<h2>Device Turned ON </h2>
</body>
</html>
";
header( "refresh:3; index.html" );
}
else if(isset($_POST['off3']))
{
$handle = fopen($file3,'w+');
$offstring = "OFF";
fwrite($handle, $offstring);
fclose($handle);
print "
<html>
<body>
<title>Home Automation</title>
<style type=text/css>
h1{
	padding-left: 50px;
}
h2{
	padding-left: 50px;
}
</style>
<h1>Home Automation</h2>
<h2>Device Turned OFF </h2>
</body>
</html>
";
header( "refresh:3; index.html" );
}

else if (isset($_POST['on4']))
{
$handle = fopen($file4,'w+');
$onstring = "ON";
fwrite($handle,$onstring);
fclose($handle);
print "
<html>
<body>
<title>Home Automation</title>
<style type=text/css>
h1{
	padding-left: 50px;
}
h2{
	padding-left: 50px;
}
</style>
<h1>Home Automation</h2>
<h2>Device Turned ON </h2>
</body>
</html>
";
header( "refresh:3; index.html" );
}
else if(isset($_POST['off4']))
{
$handle = fopen($file4,'w+');
$offstring = "OFF";
fwrite($handle, $offstring);
fclose($handle);
print "
<html>
<body>
<title>Home Automation</title>
<style type=text/css>
h1{
	padding-left: 50px;
}
h2{
	padding-left: 50px;
}
</style>
<h1>Home Automation</h2>
<h2>Device Turned OFF </h2>
</body>
</html>
";
header( "refresh:3; index.html" );
}

?>