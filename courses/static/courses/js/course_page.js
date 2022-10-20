var player1;
var video_list1;
document.onreadystatechange = function(){
if(document.readyState == 'interactive')
{
player1 = document.getElementById('player')
video_list1 = document.getElementById('video_list')
maintainRatio()
}
}
window.addEventListener('resize', maintainRatio)
function maintainRatio(){
console.log({
width : player1.width,
cw : player1.clientWidth,
h : player1.height,
ch : player1.clientHeight,

})
var w = player1.clientWidth
var h = (w*9)/16
console.log(w,h);
player1.height = h
video_list1.style.maxHeight = h + "px"
}