$(document).ajaxSend(()=>{
  loadStart();
})
$(document).ajaxSuccess(()=>{
  loadEnd(true);
})
$(document).ajaxError(()=>{
  loadEnd(false)
})

function loadStart(){
  $(".loading-head").show();
  $(".loading-head").animate({
    background: "rgba(64,225,225,0.7)",
    right:"5%"
  },500);
}

function loadEnd(success){
  if(success){
    $(".loading-head").animate({
      right:"0",
      backgroundColor: "rgba(103,194,58,0.7)"
    },1000,()=>{
      $(".loading-head").hide();
      $(".loading-head").css("right","100%");
      $(".loading-head").css("backgroundColor","rgba(103,194,58,0.7)");
    })
  }else{

    $(".loading-head").animate({
      right:"0",
      backgroundColor: "rgba(226,16,16,0.7)"
    },1000,()=>{
      $(".loading-head").hide();
      $(".loading-head").css("right","100%");
      $(".loading-head").css("backgroundColor","rgba(226,16,16,0.7)");
      alert("请求失败，请稍后再试");
    })
  }

}
