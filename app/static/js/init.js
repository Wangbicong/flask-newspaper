var news_id;
var user_id;


function add_newspaper() {
    
            var $title = $('<label>添加用户</label>');
            BootstrapDialog.show({
                title: $title,
                message:function(dialogItself){
                    var $form=$('<form></form>');
                    var $titleDrop=$('<input type="text"/>');//添加input控件
                    dialogItself.setData('input-data',$titleDrop);//为一个input绑定一个变量
                    $form.append('<label>脚本名称：</label>').append($titleDrop);//将该input添加到视图中
                    return $form;
                },
                buttons: [
                    {
                        label: '确定',
                        cssClass: 'btn-default',
                        action: function (dialogItself) {
                        //测试所填内容是否有空
                            if(dialogItself.getData('input-data').val().length==0){
                                alert("内容不能为空！");
                            }
                            else{
                            //将dialog中的input值取出
                                var scriptName = dialogItself.getData('input-data').val();
                             
                                dialogItself.close();
                            }

                        }
                    },
                    {
                        label: '取消',
                        action: function (dialogItself) {
                            dialogItself.close();
                        }
                    }
                ]
            })
}