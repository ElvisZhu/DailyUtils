<?php   
   function get_url_content($url){      
    $user_agent = "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)";       
    $ch = curl_init();      
    //curl_setopt ($ch, CURLOPT_PROXY, $proxy);      
    curl_setopt ($ch, CURLOPT_URL, $url);//设置要访问的IP      
    curl_setopt ($ch, CURLOPT_USERAGENT, $user_agent);//模拟用户使用的浏览器       
    @curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1 ); // 使用自动跳转        
    curl_setopt ($ch, CURLOPT_TIMEOUT, 60); //设置超时时间      
    curl_setopt ($ch, CURLOPT_AUTOREFERER, 1 ); // 自动设置Referer        
    curl_setopt ($ch, CURLOPT_COOKIEJAR, 'cookie.txt');      
    curl_setopt ($ch, CURLOPT_HEADER,0); //显示返回的HEAD区域的内容      
    curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1);      
    curl_setopt ($ch, CURLOPT_FOLLOWLOCATION, 1);      
    curl_setopt ($ch, CURLOPT_TIMEOUT, 10); 
    $result = curl_exec($ch);      
    curl_close($ch);      
    return $result;      
}  
print_r(get_url_content('www.ishadowsocks.mobi'));  
?>  