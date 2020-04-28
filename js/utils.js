var search = window.location.search; //获取带？的参数

//获取页面参数的函数
function getSearchString(key, Url) {
  var str = Url;
  str = str.substring(1, str.length); // 获取URL中?之后的字符（去掉第一位的问号）
  // 以&分隔字符串，获得类似name=xiaoli这样的元素数组
  var arr = str.split("&");
  var obj = new Object();
  // 将每一个数组元素以=分隔并赋给obj对象
  for (var i = 0; i < arr.length; i++) {
    var tmp_arr = arr[i].split("=");
    obj[decodeURIComponent(tmp_arr[0])] = decodeURIComponent(tmp_arr[1]);
  }
  return obj[key];
}
/*
 ***实例：
 *获取id -> getSearchString("id",search)
 *
 */

 //是否兼容性浏览器，可直接调用
function IEVersion() {
  var userAgent = navigator.userAgent; //取得浏览器的userAgent字符串
  var isIE = userAgent.indexOf("compatible") > -1 && userAgent.indexOf("MSIE") > -1 && !isOpera; //判断是否IE浏览器
  var isEdge = userAgent.indexOf("Windows NT 6.1; Trident/7.0;") > -1 && !isIE; //判断是否IE的Edge浏览器
  if (isIE) {
    var reIE = new RegExp("MSIE (\\d+\\.\\d+);");
    reIE.test(userAgent);
    var fIEVersion = parseFloat(RegExp["$1"]);
    if (fIEVersion == 7) {
      return "IE7";
    } else if (fIEVersion == 8) {
      return "IE8";
    } else if (fIEVersion == 9) {
      return "IE9";
    } else if (fIEVersion == 10) {
      return "IE10";
    } else if (fIEVersion == 11) {
      return "IE11";
    } else {
      return "0"
    } //IE版本过低
  } else if (isEdge) {
    return "Edge";
  } else {
    return "-1"; //非IE
  }
}
//时间格式转换
//格式化时间转换
function ChangeDateFormat(val) {
		let dateStr = ""
    if (val != null) {
        var date = new Date(parseInt(val.replace("/Date(", "").replace(")/", ""), 10));
        //月份为0-11，所以+1，月份小于10时补个0
        var month = date.getMonth() + 1 < 10 ? "0" + (date.getMonth() + 1) : date.getMonth() + 1;
        var currentDate = date.getDate() < 10 ? "0" + date.getDate() : date.getDate();
        dateStr =  date.getFullYear() + "-" + month + "-" + currentDate;
    }
    return dateStr;
}
