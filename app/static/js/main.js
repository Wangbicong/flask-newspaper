var NEWS_ID = 0;
var USER_ID = 0;
var LAST_NEWS_ITEM=Object();
LAST_NEWS_ITEM.style=Object();
var LAST_USER_ITEM=Object();
LAST_USER_ITEM.style=Object();


function add_newspaper() {
    
    var $title = $('<label>添加报纸</label>');
        BootstrapDialog.show({
            title: $title,
            message: function (dialogItself) {
                var $form = $('<form class="form-horizontal" role="form" action="/newspaper/" method="post"> \
    <div class="form-group"> \
        <label for="name" class="col-sm-2 control-label">报纸名称（必填）</label>\
        <div class="col-sm-10">\
            <input type="text" class="form-control" id="name" name="name">\
        </div>\
    </div>\
    <div class="form-group"> \
        <label for="jou_id" class="col-sm-2 control-label">总期数（必填）</label>\
        <div class="col-sm-10">\
            <input type="text" class="form-control" id="jou_id" name="jou_id">\
        </div>\
    </div>\
    <div class="form-group"> \
        <label for="sub_jou_id" class="col-sm-2 control-label">期数（必填）</label>\
        <div class="col-sm-10">\
            <input type="text" class="form-control" id="sub_jou_id" name="sub_jou_id">\
        </div>\
    </div>\
    <div class="form-group"> \
        <label for="pub_date" class="col-sm-2 control-label">发行日期（必填）</label>\
        <div class="col-sm-10">\
            <input type="text" class="form-control" id="pub_date" name="pub_date">\
        </div>\
    </div>\
    <div class="form-group">\
        <div class="col-sm-offset-2 col-sm-10">\
            <button type="submit" class="btn btn-default">确认</button>\
        </div>\
    </div>\
</form>');
                return $form;
            }
        })
}

function add_user() {
    
    var $title = $('<label>添加用户</label>');
        BootstrapDialog.show({
            title: $title,
            message: function (dialogItself) {
                var $form = $('<form class="form-horizontal" role="form" action="/user/" method="post"> \
    <div class="form-group"> \
        <label for="name" class="col-sm-2 control-label">姓名</label>\
        <div class="col-sm-10">\
            <input type="text" class="form-control" id="name" name="name">\
        </div>\
    </div>\
    <div class="form-group"> \
        <label for="phone_num" class="col-sm-2 control-label">手机号（必填）</label>\
        <div class="col-sm-10">\
            <input type="text" class="form-control" id="phone_num" name="phone_num">\
        </div>\
    </div>\
    <div class="form-group"> \
        <label for="age" class="col-sm-2 control-label">年龄</label>\
        <div class="col-sm-10">\
            <input type="text" class="form-control" id="age" name="age">\
        </div>\
    </div>\
    <div class="form-group"> \
        <label for="sex" class="col-sm-2 control-label">性别</label>\
        <div class="col-sm-10">\
            <input type="text" class="form-control" id="sex" name="sex">\
        </div>\
    </div>\
    <div class="form-group"> \
        <label for="address" class="col-sm-2 control-label">住址</label>\
        <div class="col-sm-10">\
            <input type="text" class="form-control" id="address" name="address">\
        </div>\
    </div>\
    <div class="form-group">\
        <div class="col-sm-offset-2 col-sm-10">\
            <button type="submit" class="btn btn-default">确认</button>\
        </div>\
    </div>\
</form>');
                return $form;
            }
        })
}

function del_newspaper() {
    if(NEWS_ID){
        $.ajax({
            url: '/newspaper/' + NEWS_ID +'/',
            type: 'DELETE',
            success: function(result) {
                window.location.reload();
                // Do something with the result
            }
        });
    }
}

function del_user() {
    if(USER_ID){
        $.ajax({
            url: '/user/' + USER_ID +'/',
            type: 'DELETE',
            success: function(result) {
                window.location.reload();
                // Do something with the result
            }
        });
    }
}

