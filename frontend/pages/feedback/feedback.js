Page({
  data:{
    fbtext:''
  },
  fb: function(e){
    wx.request({
      url: 'http://127.0.0.1:8000/wx/wx_feedback/',
      header:{
        "content-type": "application/x-www-form-urlencoded"
      },
      method: 'POST',
      data: {
        feedback: this.data.fbtext
      },
      success: (res) => {
        console.log("post success");
        console.log(res);
        wx.showToast({
          title: '提交成功',
          icon: 'success',
          duration: 2000
        });
        wx.switchTab({
          url: '/pages/manage/manage',
        });
      },
    });
  },
  inputFB:function(e){
    this.setData({
      fbtext: e.detail.value
    })
  }
})