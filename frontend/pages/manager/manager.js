// pages/manager/manager.js
Page({
    addMember: function(e){
        wx.navigateTo({
          url: '/pages/addMember/addMember',
        })
      },
      delMember: function(e){
        wx.navigateTo({
          url: '/pages/delMember/delMember',
        })
      },
      allMembers: function(e){
        wx.navigateTo({
            url: '/pages/allMembers/allMembers',
          })
      },
      fileAddress: function(e){
        wx.navigateTo({
          url: '/pages/home/home',
        })
      },
      setAdmin: function(e){
        wx.navigateTo({
          url: '/pages/setAdmin/setAdmin',
        })
      },
    
})