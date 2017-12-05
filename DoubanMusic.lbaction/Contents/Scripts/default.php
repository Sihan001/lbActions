<?php
require_once('workflows.php');
$w = new Workflows();
$query = urlencode( "{query}" );
$api = "01068bdd0c3168a70313a397249439f5";
$url = "https://api.douban.com/v2/music/search?count=20&apikey=$api&q=$query";
$suggestions = $w->request( $url );
$suggestions = json_decode( $suggestions );
function get_name($i) {
   return $i->name;
}
foreach( $suggestions->musics as $suggest ):
   $w->result( $suggest->id, $suggest->alt, $suggest->title, '表演者: '. implode(",", $suggest->attrs->singer) .' 评分: '. $suggest->rating->average .'/'. $suggest->rating->numRaters .' 标签: '. implode(",", array_map('get_name', $suggest->tags)), '67BE2A80-D1E6-4A47-B82A-E140CBA759A0.png' );
endforeach;

if ( count( $w->results() ) == 0 ):
         $w->result( 'dobanmusic', 'http://music.douban.com/subject_search?search_text='. $query, '糟糕...', '没找到符合条件的音乐, 去豆瓣搜搜看？', 'icon.png', 'yes' );
endif;   

echo $w->toxml();