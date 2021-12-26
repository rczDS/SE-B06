Page({
  data:{
    address:''
  },
  inputName:function(e){
    this.setData({
      address: e.detail.value
    })
  },
  setAdmin: function(e){
    wx.request({
      url: 'http://127.0.0.1:8000/wx/wx_setAddress/',
      method: 'POST',
      header:{
        "content-type": "application/x-www-form-urlencoded"
      },
      data: {
        address: this.data.address
      },
      success: res => {
        if (res.statusCode == 200) {
          wx.showToast({
            title: '修改成功',
            icon: 'success',
            duration: 2000
          });
          wx.navigateTo({
            url: '/pages/manager/manager',
          });
        }
      },
    })
  }
})