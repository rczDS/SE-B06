Page({
  data:{
    id:'',
    passwd:''
  },
  login: function(e){
    wx.request({
      url: 'http://127.0.0.1:8000/wx/wx_login/',
      method: "POST",
      header:{
        "content-type": "application/x-www-form-urlencoded"
      },
      data: {
        id: this.data.id,
        passwd: this.data.passwd
      },
      success: res => {
        console.log(this.mname)
        if (res.statusCode == 200) {
          console.log(res)
          this.setData({
            result: res.data
          })
        } 
      },
    }),
    wx.switchTab({
      url: '/pages/home/home',
    })
  },
  inputId:function(e){
    this.setData({
      id: e.detail.value
    })
  },
  inputPasswd:function(e){
    this.setData({
      passwd: e.detail.value
    })
  }
})