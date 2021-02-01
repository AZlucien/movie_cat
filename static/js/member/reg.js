;
var member_reg_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $(".reg_wrap .do_reg").click(function(){
            var btn_target = $(this);
            if(btn_target.hasClass("disabled")){
                alert("请不要重复点击！");
                return;
            }


            var reg_name = $(".reg_wrap input[name=reg_name]").val();
            var reg_pwd = $(".reg_wrap input[name=reg_pwd]").val();
            var reg_pwd2 = $(".reg_wrap input[name=reg_pwd2]").val();
            if (reg_name == undefined || reg_name.length < 4) {
                alert("请输入正确的用户名！（不能小于4个字符）");
                return;
            }

            if (reg_pwd == undefined || reg_pwd.length < 6) {
                alert("请输入正确的密码（不能小于6个字符）！");
                return;
            }

            if(reg_pwd2 == undefined || reg_pwd2 != reg_pwd){
                alert("请输入正确的确认密码（必须和上面的密码一致）！")
                return;
            }

            btn_target.addClass("disabled");

            $.ajax({
               url:"/member/reg",
               type:"POST",
               data:{
                    reg_name:reg_name,
                    reg_pwd:reg_pwd,
               },
               datatype:'json',
               success:function(res){
                    btn_target.removeClass("disabled");
               }
            });


        });
    }
};

$(function(){
   member_reg_ops.init();
});