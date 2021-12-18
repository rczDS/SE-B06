Page({
  
  manager: function(e){
    wx.navigateTo({
      url: '/pages/manager/manager',
      //todo:check if manager
    })
  },
  
  changePasswd: function(e){
    wx.navigateTo({
      url: '/pages/changePasswd/changePasswd',
    })
  },
  response: function(e){
    wx.navigateTo({
      url: '/pages/home/home',
    })
  }
})