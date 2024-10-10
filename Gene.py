incomingNotifications=[]#queue
recentNotifications=[]#stack
oldNotifications=[ ]#list
def addNewNotification(notification):
    incomingNotifications.append(notification)
def processNotificationtoRecent():
    if incomingNotifications:
        notification =  incomingNotifications.pop(0)
    recentNotifications.append(notification)
addNewNotification('twin send me message')
addNewNotification('sandra send me it again')
print(incomingNotifications)
processNotificationtoRecent()
print("update on the queue and stack:  ")
print("incomingNotifications are: ")
print(incomingNotifications)
print("recent notifications are: ")
print(recentNotifications)
  
def processNotificationstoold():
    if recentNotifications.append():
        print(recentNotifications)
    



        
            
    
    