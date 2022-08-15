# NoWall
Remove paywall and read/get content for free

# How it works?

It is simple to understand, basically every sites want Google to index their content, so they don't show ads to google crawler, and this helps us as everytime google crawls the content of site it caches a copy of site and NoWall shows you the caches version of site with no paywall!

Main code:

```
<?php

$link = "<link_with_paywall>"
$url = "http://webcache.googleusercontent.com/search?q=cache:" . $link . "&strip=0&vwsrc=1";
$ch = curl_init();
$optArray = array(CURLOPT_URL => $url, CURLOPT_RETURNTRANSFER => true);
curl_setopt_array($ch, $optArray);
$res = curl_exec($ch);
curl_close($ch);

$start = stripos($res, '<pre>');
$end = stripos($res, '</pre>', $offset = $start);

$length = $end - $start;

$res = substr($res, $start, $length);
$res =str_replace("<pre>", "", $res);
$res =str_replace("</pre>", "", $res);
$res = html_entity_decode($res);
$res = str_replace("<script>window.main();</script>", "", $res);

echo $res;

?>
```
