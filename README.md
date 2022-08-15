# NoWall
Remove paywall and read/get content for free

So the main code:

```
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
```
