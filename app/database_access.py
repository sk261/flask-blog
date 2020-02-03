import sqlite3
_DB_FullPath = 'app/webpages.db'
_Connection = sqlite3.connect(_DB_FullPath)
_Cusor = _Connection.cursor()

'''
DB Layout
Key:
PID - PageID
UID - UserID
TID - Thread ID
P_ID - Post ID
DOC - Date of Creation
Icon - Path to Icon image
    PAGES:PID|Name
        PAGES_DATA:PID|Path|LoginReq|Description|Icon
        PAGES_CONTENT:PID|Content
        PAGES_HISTORY:PID|UID|ChangeDTG|Content
    USERS:UID|Username
        USERS_DATA:UID|PW|Email|Verified|DOC|Admin
    FORUM:TID|ThreadName
        FORUM_THREAD_DATA:TID|Visible|DOC|UID|Content
        FORUM_POSTS:TID|P_ID|UID
            FORUM_POST_DATA:P_ID|UID|DOC|Content|Visible
'''

def get_data(table, ID):
    _Cursor.execute('')
    return ""