Page({
  data:{
    content:'',
    users:''
  },
  inputContent:function(e){
    this.setData({
      content: e.detail.value
    })
  },
  inputUsers:function(e){
    this.setData({
      users: e.detail.value
    })
  },
  add: function(e){
    wx.request({
      url: 'http://127.0.0.1:8000/wx/wx_addTask/',
      method: 'POST',
      header:{
        "content-type": "application/x-www-form-urlencoded"
      },
      data: {
        content: this.data.content,
        users: this.data.users
      },
      success: res => {
      },
    }),
    wx.switchTab({
      url: '/pages/home/home',
    });
  }
})