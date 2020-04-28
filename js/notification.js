var wNotification = function(config){
	this.config={
		delay: 3000,
		title: "提示",
		msg: "消息内容",
		id: ""
	}
	if(config && $.isPlainObject(config)){
		$.extend(this.config,config);
	}
	this.NotificationBox = $(`<div class="w-notification" style="z-index:2002;bottom:16px"></div>`);
	this.NotificationGroup = $(`<a class="w-notification_group"  href="newsDetail.htm?id=${this.config.id}"></a>`)
	this.NotificationTitle = $(`<h2 class="w-notification_title">${this.config.title}</h2>`);
	this.content = $(`<div class="w-notification_content"><p>${this.config.msg}</p></div>`);
	this.closeBtn = $(`<div class="w-notification_closeBtn" id="closeNote"></div>`);
}
wNotification.prototype = {
	creat:function(){
		var Config = this.config,
			Box = this.NotificationBox,
			Group = this.NotificationGroup,
			Title = this.NotificationTitle,
			Msg = this.content,
			CloseBtn = this.closeBtn;
			Group.append(Title);
			Group.append(Msg);
			Box.append(Group);
			Box.append(CloseBtn)
			$("body").append(Box);
			$(".w-notification").animate({right: '30px'},.3)
	},
	close:function(){
		$("#closeNote").on("click",function(){
			$(".w-notification").remove();
		})
	}
}
function noteOpen(title,msg,delay,id){
	var Note = new wNotification({title,msg,delay,id});
	Note.creat();
	Note.close();
}