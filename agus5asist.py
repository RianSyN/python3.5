# -*- coding: utf-8 -*-
import JBRB
from JBRB.lib.curve.ttypes import *
from datetime import datetime, timedelta, date
from urlparse import urlparse
from bs4 import BeautifulSoup
from gtts import gTTS
import time,timeit,random,sys,json,codecs,urllib2,urllib,requests,threading,glob,os,subprocess,multiprocessing,re,calendar,ast
import wikipedia
#SB HNS
ki = JBRB.LINE()
ki.login(token="EsmBpUhs8p7RdQAawAZd.R+EQ0Zs81o6jUrU+x2fa3q.YUVa9PVcsleKwdJxuu7SIbAGs7n9jtObe9XrRY4KNWI=")#1
#cit
#ki = PSD.LINE()
#ki.login(token="EosErkc76fkYVpyk4Glb.+qGVb0LeIRctVAkiTcu7gW.a3wwieiP8LqX2uesDr2GCmGVQH+q+G46o5LG3Vcx/vA=")#1
#ki.loginResult()
ki1 = JBRB.LINE()
ki1.login(token='Esdg7QUoF8JxwKnnkvm8.dQE/yFGjwgIxgnSNY1xAoa.7uaTNMLaAQqXp9JQTPPpYflJCSWixcai/4EPURMCdwM=')

ki2 = JBRB.LINE()
ki2.login(token='EsykMuvdSwlpgrktqMxc.h3dIA84EIgOe2qyGKNqTJa.c1jxHrJHoLcAXvMIRBuWcN3coPqIJ32tZvG03ptG3NU=')

ki3 = JBRB.LINE()
ki3.login(token='Es5vZfmjejMwvvDwpGs5.qNeI0PcNOBhcVUEIonvrvq.fPMCGU7rBJgM7X0nM1w9QNdmv+Bi7dNx3cJNgUw5ytw=')

ki4 = JBRB.LINE()
ki4.login(token='EssP8qn1bsEoIlatSIk4.HsYU0Oj7cPyQIHIXautVLa.i5jiSeMNlnd9pTT5iCulaipDd1U1P2wCCh8XGRmJYy0=')

ki5 = JBRB.LINE()
ki5.login(token='EsdaC8SgoBYNouoiG20d.PaUZTP6yO8IznYKCHTkx7q.5PKx0CapJy3F9/b3ZV8uN820CGU68nIbHVlT8XfPbJ4=')
print 'done'
#last
reload(sys)
sys.setdefaultencoding('utf-8')

album = None
image_path = 'tmp/tmp.jpg'
P1=[ki1,ki2,ki3,ki4,ki5]
P2=[ki1,ki2,ki3,ki4,ki5]
P3=[ki1,ki2,ki3,ki4,ki5,]
mid = ki.getProfile().mid
ki1mid = ki1.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
Botsa=[ki1mid,ki2mid,ki3mid,ki4mid,ki5mid]
protectname = []
nzetUrl = []
nzetProtection = []
autoCancel = []
nzetAutoInvite = []
nzetTalkBan = []
nzetWellcome = []
admsa = "u0139dfffbd23f445b2e5380080f528aa" #isi
nZetsu = "u0139dfffbd23f445b2e5380080f528aa" #isi
admin = "u0139dfffbd23f445b2e5380080f528aa" #isi

wait = {
    "contact": False,
    "clock": False,
    "cloneContact": {},
    "autoJoin": True,
    "detectMention": False,
    "kickMention": False,
    "autoCancel": {"on": True,"members": 3},
    "leaveRoom": True,
    "setkey": "",
    "timeline": False,
    "autoAdd": False,
    "spam": "nZetz troops 👉 ▩▣ᴘ͓̽͟͟s͓̽͟͟ᴅ͓̽͟͟ ᴛ͓̽͟͟ᴇ͓̽͟͟ᴀ͓̽͟͟ᴍ͓̽͟͟ ʙ͓̽͟͟ᴏ͓̽͟͟ᴛ͓̽͟͟ ▣▩ 👈",
    "message": "",
    "pap": "http://mofsc.com.au/wp-content/uploads/2016/09/Welcome-02-web-version.jpg",
    "rname": "",
    "rbio": "",
    "autoaddpesan": "",
    "rpic": "0hq9VvwdPrLhZrDwGtUIlRQVdKIHscISheE2tidkgNI3RHOGxEXz4xdxkIeS8UOm0UXzpjchsOci5C",
    "blacklist": {},
    "bots": {},
    "talkblacklist": {},
    "left":"「Salam baper, masuk lg kick neh」\nStatus: Left♪",
    "talkban": True,
    "wblacklist": False,
    "talkwblacklist": False,
    "kick": False,
    "pname": {},
    "pro_name": {},
    "dblacklist": False,
    "talkdblacklist": False,
    "twblacklist": False,
    "sambutan": False,
    "tdblacklist": False,
    'lang':"JP",
    }

wait2 = {
    "readPoint": {},
    "readMember": {},
    "setTime": {},
    "copy": False,
    "target": {},
    "midsTarget": {},
    "ROM": {}
    }

wait["blacklist"] = {
    }

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
    }

settings = {
    "simiSimi":{}
    }

wait["bots"] = {
    "uebb6976ce05240ce3d9e0216234868f4": True, 
    "uaff7aad334bcd4ee89b91bbf5f6140dd": True, 
    "ua40bb3b69e98a3c89937291c86d297ed": True, 
    "u0ea7be61f80958689718db27cb55da38": True, 
    "u1f70e26bce1e886a04d9062092742d8c": True, 
    "u427122d290a7a1b1c2bee7a238d55155": True, 
    "u852caed2827b0a962a8a18b10144ef94": True

    }

mimic = {
    "status":False,
    "detectMention": False,
    "kickMention": False,
    "sambutan": False,
    "simiSimi":{},
    "target":{},
    "setkey":"",
    "pap":"http://s1.picswalls.com/wallpapers/2015/09/20/wallpaper-2015_111528356_269.jpg",
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time()
Bots = wait["bots"]

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "Juan Pradana"   
         s.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib.request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+70)
        end_content = s.find(',"ow"',start_content-70)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#cek waktu bot berjalan
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)    

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            page = page[end_content:]
    return items

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = ki.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki.rejectGroupInvitation(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki.cancelGroupInvitation(op.param1, matched_list)          
        if op.type == 22:
            if wait["leaveRoom"] == True:
                ki.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                ki.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if wait["talkban"] == True:
             if msg.from_ in wait["talkblacklist"]:
                try:
                    random.choice(P1).sendText(msg.to,ki.getContact(msg.from_).displayName + " Si tolol palah ngomong")
                    random.choice(P1).kickoutFromGroup(msg.to,[msg.from_])
                except:
                    try:
                        random.choice(P2).sendText(msg.to,ki.getContact(msg.from_).displayName + " Si tolol palah ngomong")
                        random.choice(P2).kickoutFromGroup(msg.to,[msg.from_])
                    except:
                        ki.sendText(msg.to,ki.getContact(msg.from_).displayName + " Si tolol palah ngomong")
                        ki.kickoutFromGroup(msg.to,[msg.from_])
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                text = msg.text
                if text is not None:
                    if msg.contentType == 1:
                        ki.sendImageWithURL(msg.to,mimic["pap"])
                    else:
                        ki.sendText(msg.to,text)
                else:
                    if msg.contentType == 7:
                        msg.contentType = 7
                        msg.text = None
                        msg.contentMetadata = {
                                              'STKID': "15597669",
                                              'STKPKGID': "1403270",
                                              'STKVER': "1" }
                        ki.sendMessage(msg)
                    if msg.contentType == 9:
                        msg.contentType = 9
                        msg.contentMetadata={'PRDTYPE': 'STICKER',
                                            'STKVER': '1',
                                            'MSGTPL': '5',
                                            'STKPKGID': '1380280'}
                        msg.text = None
                        ki.sendMessage(msg)
                    if msg.contentType == 13:
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
                        ki.sendMessage(msg)
                    if msg.contentType == 1:
                        ki.sendImageWithURL(msg.to,mimic["pap"])
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            print(
            " TO: {}\n".format(msg.to),
            "FROM: {}\n".format(msg.from_),
            "TEXT: {}\n".format(msg.text),
            "CONTENT TYPE: {}\n".format(msg.contentType),
            "METADATA: {}\n".format(msg.contentMetadata),
            "TYPE: {}\n".format(msg.toType),
            "MESSAGE ID: {}\n".format(msg.id),
            "DATE: {}\n\n".format(msg.createdTime)
            )
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                ki.like(url[25:58], url[66:], likeType=1001)
                ki.comment(url[25:58], url[66:], "Auto Like by :\nAGUS \n agus squad \n􀬁􀆆􏿿 ▩▣ᴘ͓̽͟͟s͓̽͟͟ᴅ͓̽͟͟ ᴛ͓̽͟͟ᴇ͓̽͟͟ᴀ͓̽͟͟ᴍ͓̽͟͟ ʙ͓̽͟͟ᴏ͓̽͟͟ᴛ͓̽͟͟ ▣▩􀬁􀆆􏿿\n\nhttp://line.me/ti/p/~agustri1990")
                ki1.like(url[25:58], url[66:], likeType=1001)
                ki1.comment(url[25:58], url[66:], "Auto Like by :\nAGUS \n agus squad \n􀬁􀆆􏿿 ▩▣ᴘ͓̽͟͟s͓̽͟͟ᴅ͓̽͟͟ ᴛ͓̽͟͟ᴇ͓̽͟͟ᴀ͓̽͟͟ᴍ͓̽͟͟ ʙ͓̽͟͟ᴏ͓̽͟͟ᴛ͓̽͟͟ ▣▩􀬁􀆆􏿿\n\nhttp://line.me/ti/p/~agustri1990")
                ki2.like(url[25:58], url[66:], likeType=1001)
                ki2.comment(url[25:58], url[66:], "Auto Like by :\nAGUS \n agus squad \n􀬁􀆆􏿿 ▩▣ᴘ͓̽͟͟s͓̽͟͟ᴅ͓̽͟͟ ᴛ͓̽͟͟ᴇ͓̽͟͟ᴀ͓̽͟͟ᴍ͓̽͟͟ ʙ͓̽͟͟ᴏ͓̽͟͟ᴛ͓̽͟͟ ▣▩􀬁􀆆􏿿\n\nhttp://line.me/ti/p/~agustri1990")
                ki3.like(url[25:58], url[66:], likeType=1001)
                ki3.comment(url[25:58], url[66:], "Auto Like by :\nAGUS \n agus squad \n􀬁􀆆􏿿 ▩▣ᴘ͓̽͟͟s͓̽͟͟ᴅ͓̽͟͟ ᴛ͓̽͟͟ᴇ͓̽͟͟ᴀ͓̽͟͟ᴍ͓̽͟͟ ʙ͓̽͟͟ᴏ͓̽͟͟ᴛ͓̽͟͟ ▣▩􀬁􀆆􏿿\n\nhttp://line.me/ti/p/~agustri1990")
                ki4.like(url[25:58], url[66:], likeType=1001)
                ki4.comment(url[25:58], url[66:], "Auto Like by :\nAGUS \n agus squad \n􀬁􀆆􏿿 ▩▣ᴘ͓̽͟͟s͓̽͟͟ᴅ͓̽͟͟ ᴛ͓̽͟͟ᴇ͓̽͟͟ᴀ͓̽͟͟ᴍ͓̽͟͟ ʙ͓̽͟͟ᴏ͓̽͟͟ᴛ͓̽͟͟ ▣▩􀬁􀆆􏿿\n\nhttp://line.me/ti/p/~agustri1990")
                ki5.like(url[25:58], url[66:], likeType=1001)
                ki5.comment(url[25:58], url[66:], "Auto Like by :\nAGUS \n agus squad \n􀬁􀆆􏿿 ▩▣ᴘ͓̽͟͟s͓̽͟͟ᴅ͓̽͟͟ ᴛ͓̽͟͟ᴇ͓̽͟͟ᴀ͓̽͟͟ᴍ͓̽͟͟ ʙ͓̽͟͟ᴏ͓̽͟͟ᴛ͓̽͟͟ ▣▩􀬁􀆆􏿿\n\nhttp://line.me/ti/p/~agustri1990")
            if msg.contentType == 13:
                if wait["kick"] == True:
                        random.choice(P1).kickoutFromGroup(msg.to,[msg.contentMetadata["mid"]])
                        wait["kick"] = False
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.sendText(msg.to,contact.displayName + " Sukses to Kick")
                if wait["talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["talkblacklist"]:
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.sendText(msg.to,contact.displayName + " Already in Talkban")
                        wait["talkwblacklist"] = False
                    else:
                        wait["talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["talkwblacklist"] = False
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.sendText(msg.to,contact.displayName + " Sukses Add to Talkban")
                elif wait["talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["talkblacklist"]:
                        del wait["talkblacklist"][msg.contentMetadata["mid"]]
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.sendText(msg.to,contact.displayName + " Sukses Delete from Talkban")
                        wait["talkdblacklist"] = False
                    else:
                        wait["talkdblacklist"] = False
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.sendText(msg.to,contact.displayName + " Not In Talkban")
                if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.sendText(msg.to,contact.displayName + " Already in Blacklist")
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        wait["wblacklist"] = False
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.sendText(msg.to,contact.displayName + " Sukses Add to Blacklist")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.sendText(msg.to,contact.displayName + " Sukses Delete from Blacklist")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.sendText(msg.to,contact.displayName + " Not In Blacklist")
                elif wait["twblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.sendText(msg.to,contact.displayName + " Already in Blacklist")
                        wait["twblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        wait["twblacklist"] = True
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.sendText(msg.to,contact.displayName + " Sukses Add to Blacklist")
                elif wait["tdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.sendText(msg.to,contact.displayName + " Sukses Delete from Blacklist")
                        wait["tdblacklist"] = True
                    else:
                        wait["tdblacklist"] = True
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.sendText(msg.to,contact.displayName + "Not In Blacklist")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = ki.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ki.sendText(msg.to,"[Display Name]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[Status Message]:\n" + contact.statusMessage + "\n[Picture Status]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[Cover]:\n" + str(cu))
                    else:
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = ki.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ki.sendText(msg.to,"Nama:" + contact.displayName + "\n\nUser ID:" + msg.contentMetadata["mid"] + "\n\nBio:\n" + contact.statusMessage)
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    ki.sendText(msg.to,"menempatkan URL\n" + msg.contentMetadata["postEndUrl"])
            elif msg.text is None:
                return
            elif msg.text.lower() == mimic["setkey"]+' help' or msg.text.lower() == mimic["setkey"]+'help':
                    profile = ki.getProfile()
                    ki.sendText(msg.to,"「" + mimic["setkey"].title() + "」\n" \
                    +mimic["setkey"].title()+"✨ help\n" \
                    +mimic["setkey"].title()+"✨ steal\n" \
                    +mimic["setkey"].title()+"✨ copy\n" \
                    +mimic["setkey"].title()+"✨ micall\n" \
                    +mimic["setkey"].title()+"✨ banall\n" \
                    +mimic["setkey"].title()+"✨ unbanall\n" \
                    +mimic["setkey"].title()+"✨ teamall\n" \
                    +mimic["setkey"].title()+"✨ unteamall\n" \
                    +mimic["setkey"].title()+"✨ ban\n" \
                    +mimic["setkey"].title()+"✨ ban repat\n" \
                    +mimic["setkey"].title()+"✨ unban\n" \
                    +mimic["setkey"].title()+"✨ unban repeat\n" \
                    +mimic["setkey"].title()+"✨ talkban\n" \
                    +mimic["setkey"].title()+"✨ untalkban\n" \
                    +mimic["setkey"].title()+"✨ abort\n" \
                    +mimic["setkey"].title()+"✨ ban\n" \
                    +mimic["setkey"].title()+"✨ mimic\n" \
                    +mimic["setkey"].title()+"✨ instagram\n" \
                    +mimic["setkey"].title()+"✨ youtube\n" \
                    +mimic["setkey"].title()+"✨ wikipedia\n" \
                    +mimic["setkey"].title()+"✨ lyric\n" \
                    +mimic["setkey"].title()+"✨ music\n" \
                    +mimic["setkey"].title()+"✨ image\n" \
                    +mimic["setkey"].title()+"✨ say@id\n" \
                    +mimic["setkey"].title()+"✨ autoadd\n" \
                    +mimic["setkey"].title()+"✨ autojoin\n" \
                    +mimic["setkey"].title()+"✨ me\n" \
                    +mimic["setkey"].title()+"✨ bot\n" \
                    +mimic["setkey"].title()+"✨ ourl\n" \
                    +mimic["setkey"].title()+"✨ invite:gcreator\n" \
                    +mimic["setkey"].title()+"✨ bio\n" \
                    +mimic["setkey"].title()+"✨ pictstatus\n" \
                    +mimic["setkey"].title()+"✨ getpictstatus\n" \
                    +mimic["setkey"].title()+"✨ pp\n" \
                    +mimic["setkey"].title()+"✨ sampul\n" \
                    +mimic["setkey"].title()+"✨ mid\n" \
                    +mimic["setkey"].title()+"✨ allbio:\n" \
                    +mimic["setkey"].title()+"✨ myname:\n" \
                    +mimic["setkey"].title()+"✨ mybio:\n" \
                    +mimic["setkey"].title()+"✨ name1: - name5:\n" \
                    +mimic["setkey"].title()+"✨ gn\n" \
                    +mimic["setkey"].title()+"✨ lurking\n" \
                    +mimic["setkey"].title()+"✨ gcreator\n" \
                    +mimic["setkey"].title()+"✨ groups\n" \
                    +mimic["setkey"].title()+"✨ mcheck\n" \
                    +mimic["setkey"].title()+"✨ tcheck\n" \
                    +mimic["setkey"].title()+"✨ mlist\n" \
                    +mimic["setkey"].title()+"✨ friend\n" \
                    +mimic["setkey"].title()+"✨ gcancel1-5 \n" \
                    +mimic["setkey"].title()+"✨ clear ban\n" \
                    +mimic["setkey"].title()+"✨ pesan set:\n" \
                    +mimic["setkey"].title()+"✨ pesan cek\n" \
                    +mimic["setkey"].title()+"✨ welcomemessage pict set\n" \
                    +mimic["setkey"].title()+"✨ spam add:\n" \
                    +mimic["setkey"].title()+"✨ spam:<number>\n" \
                    +mimic["setkey"].title()+"✨ spam on <number> <query>\n" \
                    +mimic["setkey"].title()+"✨ spam off <number> <query>\n" \
                    +mimic["setkey"].title()+"✨ spam cek\n" \
                    +mimic["setkey"].title()+"✨ url\n" \
                    +mimic["setkey"].title()+"✨ tr id@en\n" \
                    +mimic["setkey"].title()+"✨ tr en@id\n" \
                    +mimic["setkey"].title()+"✨ tr id@jp\n" \
                    +mimic["setkey"].title()+"✨ tr jp@id\n" \
                    +mimic["setkey"].title()+"✨ tr id@th\n" \
                    +mimic["setkey"].title()+"✨ tr th@id\n" \
                    +mimic["setkey"].title()+"✨ gift\n" \
                    +mimic["setkey"].title()+"✨ kick\n" \
                    +mimic["setkey"].title()+"✨ miclist\n" \
                    +mimic["setkey"].title()+"✨ tagall\n" \
                    +mimic["setkey"].title()+"✨ tagall1-tagall5\n" \
                    +mimic["setkey"].title()+"✨ banlist\n" \
                    +mimic["setkey"].title()+"✨ blocklist\n" \
                    +mimic["setkey"].title()+"✨ On\n" \
                    +mimic["setkey"].title()+"✨ Off\n" \
                    +mimic["setkey"].title()+"✨ contact <on/off>\n" \
                    +mimic["setkey"].title()+"✨ pro-all <on/off>\n" \
                    +mimic["setkey"].title()+"✨ cancel <on/off>\n" \
                    +mimic["setkey"].title()+"✨ qr <on/off>\n" \
                    +mimic["setkey"].title()+"✨ inv <on/off>\n" \
                    +mimic["setkey"].title()+"✨ protect <on/off>\n" \
                    +mimic["setkey"].title()+"✨ share <on/off>\n" \
                    +mimic["setkey"].title()+"✨ welcomemessage <on/off>\n" \
                    +mimic["setkey"].title()+"✨ talkban <on/off>\n" \
                    +mimic["setkey"].title()+"✨ jam <on/off>\n" \
                    +mimic["setkey"].title()+"✨ leave <on/off>\n" \
                    +mimic["setkey"].title()+"✨ namelock <on/off>\n" \
                    +mimic["setkey"].title()+"✨ respon <on/off>\n" \
                    +mimic["setkey"].title()+"✨ sambutan <on/off>\n" \
                    +mimic["setkey"].title()+"✨ notag <on/off>\n" \
                    +mimic["setkey"].title()+"✨ simisimi <on/off>\n" \
                    +mimic["setkey"].title()+"✨ sider <on/off>\n" \
                    +mimic["setkey"].title()+"✨ cek out\n" \
                    +mimic["setkey"].title()+"✨ cek in\n" \
                    +mimic["setkey"].title()+"✨ setkey\n" \
                    +mimic["setkey"].title()+"✨ mycpu\n" \
                    +mimic["setkey"].title()+"✨ mykernel\n" \
                    +mimic["setkey"].title()+"✨ mysystem\n" \
                    +mimic["setkey"].title()+"✨ kick1-5 @\n" \
                    +mimic["setkey"].title()+"✨ pending\n" \
                    +mimic["setkey"].title()+"✨ nk @\n" \
                    +mimic["setkey"].title()+"✨ psd5\n" \
                    #+mimic["setkey"].title()+" cloneown\n" \
                    #+mimic["setkey"].title()+" clone-clone10\n" \
                    +mimic["setkey"].title()+"✨ friend1-friend5\n" \
                    +mimic["setkey"].title()+"✨ 1-5\n" \
                    +mimic["setkey"].title()+"✨ o1-o5\n" \
                    +mimic["setkey"].title()+"✨ k1-k5\n" \
                    +mimic["setkey"].title()+"✨ k1-k5 bye\n" \
                    +mimic["setkey"].title()+"✨ gcancel1-gcancel5\n" \
                    +mimic["setkey"].title()+"✨ set\n" \
                    +mimic["setkey"].title()+"✨ mayhemme\n" \
                    +mimic["setkey"].title()+"✨ mayhem\n" \
                    +mimic["setkey"].title()+"✨ reboot\n" \
                    +mimic["setkey"].title()+"✨ owner.bot\n" \
                    +mimic["setkey"].title()+"✨ runtime\n" \
                    +mimic["setkey"].title()+"✨ debug speed\n" \
                    +mimic["setkey"].title()+"✨ speed\n" \
                    +mimic["setkey"].title()+"✨ getname @\n" \
                    +mimic["setkey"].title()+"✨ getbio @\n" \
                    +mimic["setkey"].title()+"✨ getcontact @\n" \
                    +mimic["setkey"].title()+"✨ getprofile @\n" \
                    +mimic["setkey"].title()+"✨ getinfo @\n" \
                    #+mimic["setkey"].title()+"✨ checkdata\n" \
                    +mimic["setkey"].title()+"✨ kalender\n" \
                    +mimic["setkey"].title()+"✨ facebook\n" \
                    +mimic["setkey"].title()+"✨ google:\n" \
                    +mimic["setkey"].title()+"✨ playstore\n" \
                    +mimic["setkey"].title()+"✨ sound welcome\n" \
                    +mimic["setkey"].title()+"✨ /apakah <teks>\n" \
                    +mimic["setkey"].title()+"✨ /hari <teks>\n" \
                    +mimic["setkey"].title()+"✨ /berapa <teks>\n" \
                    +mimic["setkey"].title()+"✨ /berapakah <teks>\n" \
                    +mimic["setkey"].title()+"✨ /kapan <teks>\n" \
                    +mimic["setkey"].title()+"✨ fancytext: <nama nya apa>\n" \
                    +mimic["setkey"].title()+"✨ coppy on1 @ - coppy on5 @\n" \
                    +mimic["setkey"].title()+"✨ kibaran\n" \
                    #+mimic["setkey"].title()+" clone-clone10\n" \
                    +mimic["setkey"].title()+"✨ about\n\nSelfbot\n   " + profile.displayName + "\n   Support:\n   􀬁􀆆􏿿 ▩▣ᴘ͓̽͟͟s͓̽͟͟ᴅ͓̽͟͟ ᴛ͓̽͟͟ᴇ͓̽͟͟ᴀ͓̽͟͟ᴍ͓̽͟͟ ʙ͓̽͟͟ᴏ͓̽͟͟ᴛ͓̽͟͟ ▣▩􀬁􀆆􏿿\ntroops are silent team bot")
 #==========COPY PROFILE
            elif msg.text.lower() == mimic["setkey"]+'copy' or msg.text.lower() == mimic["setkey"]+' copy':
                ki.sendText(msg.to,"「Copy Profil」\n"+ "Commands:\n" \
					+mimic["setkey"].title()+" copy on <@|~> \n" \
					+mimic["setkey"].title()+" copy off \n" \
					+mimic["setkey"].title()+" copy setdefault ")
            elif msg.text.lower() == mimic["setkey"]+'steal' or msg.text.lower() == mimic["setkey"]+' steal':
                ki.sendText(msg.to,"「Steal」\n"+ "Usage:" + mimic["setkey"].title()+"get <type> [@\*]\nType: pict,cover")
            elif msg.text.lower() == mimic["setkey"]+'copy setdefault' or msg.text.lower() == mimic["setkey"]+' setdefault':
                ki.sendText(msg.to,"「Backup Profil」\nSukses Setdefault\nDisplayName:" + backup.displayName + "\n「Status」\n" + backup.statusMessage + "\n「Picture」")
                ki.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + backup.pictureStatus)
            elif msg.text.lower() == mimic["setkey"]+'copy off' or msg.text.lower() == mimic["setkey"]+' copy off':
                    try:
                       ki.updateDisplayPicture(backup.pictureStatus)
                       ki.updateProfile(backup)
                       ki.sendText(msg.to,"「Backup Profil」\nSukses Backup\nDisplayName:" + backup.displayName + "\n「Status」\n" + backup.statusMessage + "\n「Picture」")
                       ki.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + backup.pictureStatus)
                    except Exception as e:
                       ki.sendText(msg.to, str(e))
            elif msg.text.lower().startswith(mimic["setkey"]+'copy on ') or msg.text.lower().startswith(mimic["setkey"]+' copy on ') or msg.text.lower().startswith(mimic["setkey"]+'copy on') or msg.text.lower().startswith(mimic["setkey"]+' copy on'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki.cloneContactProfile(target)
                            group = ki.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            ki.sendText(msg.to,"Sukses Copy\nDisplayName:" + group.displayName + "\n「Status」\n" + group.statusMessage + "\n「Picture」")
                            ki.sendImageWithURL(msg.to,contact)
                        except:
                            ki.cloneContactProfile(target)
                else:
                    ki.sendText(msg.to,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" coppy on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'coppy on1 ') or msg.text.lower().startswith(mimic["setkey"]+' coppy on1 ') or msg.text.lower().startswith(mimic["setkey"]+'coppy on1') or msg.text.lower().startswith(mimic["setkey"]+' coppy on1'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki1.cloneContactProfile(target)
                            group = ki1.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            ki1.sendText(msg.to,"Sukses Copy\nDisplayName:" + group.displayName + "\n「Status」\n" + group.statusMessage + "\n「Picture」")
                            ki1.sendImageWithURL(msg.to,contact)
                        except:
                            ki1.cloneContactProfile(target)
                else:
                    ki1.sendText(msg.to,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" coppy on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'coppy on2 ') or msg.text.lower().startswith(mimic["setkey"]+' coppy on2 ') or msg.text.lower().startswith(mimic["setkey"]+'coppy on2') or msg.text.lower().startswith(mimic["setkey"]+' coppy on2'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki2.cloneContactProfile(target)
                            group = ki2.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            ki2.sendText(msg.to,"Sukses Copy\nDisplayName:" + group.displayName + "\n「Status」\n" + group.statusMessage + "\n「Picture」")
                            ki2.sendImageWithURL(msg.to,contact)
                        except:
                            ki2.cloneContactProfile(target)
                else:
                    ki2.sendText(msg.to,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" coppy on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'coppy on3 ') or msg.text.lower().startswith(mimic["setkey"]+' coppy on3 ') or msg.text.lower().startswith(mimic["setkey"]+'coppy on3') or msg.text.lower().startswith(mimic["setkey"]+' coppy on3'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki3.cloneContactProfile(target)
                            group = ki3.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            ki3.sendText(msg.to,"Sukses Copy\nDisplayName:" + group.displayName + "\n「Status」\n" + group.statusMessage + "\n「Picture」")
                            ki3.sendImageWithURL(msg.to,contact)
                        except:
                            ki3.cloneContactProfile(target)
                else:
                    ki3.sendText(msg.to,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" coppy on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'coppy on4 ') or msg.text.lower().startswith(mimic["setkey"]+' coppy on4 ') or msg.text.lower().startswith(mimic["setkey"]+'coppyon4') or msg.text.lower().startswith(mimic["setkey"]+' coppy on4'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki4.cloneContactProfile(target)
                            group = ki4.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            ki4.sendText(msg.to,"Sukses Copy\nDisplayName:" + group.displayName + "\n「Status」\n" + group.statusMessage + "\n「Picture」")
                            ki4.sendImageWithURL(msg.to,contact)
                        except:
                            ki4.cloneContactProfile(target)
                else:
                    ki4.sendText(msg.to,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" coppy on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'coppy on5 ') or msg.text.lower().startswith(mimic["setkey"]+' coppy on5 ') or msg.text.lower().startswith(mimic["setkey"]+'coppy on5') or msg.text.lower().startswith(mimic["setkey"]+' coppy on5'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki5.cloneContactProfile(target)
                            group = ki5.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            ki5.sendText(msg.to,"Sukses Copy\nDisplayName:" + group.displayName + "\n「Status」\n" + group.statusMessage + "\n「Picture」")
                            ki5.sendImageWithURL(msg.to,contact)
                        except:
                            ki5.cloneContactProfile(target)
                else:
                    ki5.sendText(msg.to,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" coppy on <@|~>")
 #==========STEAL PROFILE
            elif msg.text.lower().startswith(mimic["setkey"]+'get cover ') or msg.text.lower().startswith(mimic["setkey"]+' get cover ') or msg.text.lower().startswith(mimic["setkey"]+'get cover') or msg.text.lower().startswith(mimic["setkey"]+' get cover'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            contact = ki.getContact(target)
                            cu = ki.channel.getCover(target)
                            path = str(cu)
                            ki.sendImageWithURL(msg.to, path)
                        except:
                            group = ki.getContact(target)
                            ki.sendText(msg.to, group.displayName + " Covernya Eror")
                else:
                    if msg.toType == 2:
                        try:
                            group = ki.getGroup(msg.to)
                            contact = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            ki.sendImageWithURL(msg.to,contact)
                        except:
                            group = ki.getGroup(msg.to)
                            ki.sendText(msg.to, group.displayName + " Profilenya Eror")
                    else:
                        try:
                            contact = ki.getContact(msg.to)
                            cu = ki.channel.getCover(msg.to)
                            path = str(cu)
                            ki.sendImageWithURL(msg.to, path)
                        except:
                            group = ki.getContact(msg.to)
                            ki.sendText(msg.to, group.displayName + " Covernya Eror")
            elif msg.text.lower().startswith(mimic["setkey"]+'getpictstatus ') or msg.text.lower().startswith(mimic["setkey"]+' getpictstatus ') or msg.text.lower().startswith(mimic["setkey"]+'getpictstatus') or msg.text.lower().startswith(mimic["setkey"]+' getpictstatus'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    mi = ki.getContact(key1)
                    ki.sendText(msg.to, "http://dl.profile.line-cdn.net/"  + mi.pictureStatus)
                else:
                    if msg.toType == 2:
                        try:
                            group = ki.getGroup(msg.to)
                            contact = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            ki.sendText(msg.to,contact)
                        except:
                            group = ki.getGroup(msg.to)
                            ki.sendText(msg.to, group.displayName + " Profilenya Eror")
                    else:
                        try:
                            group = ki.getContact(msg.to)
                            contact = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            ki.sendText(msg.to,contact)
                        except:
                            group = ki.getContact(msg.to)
                            ki.sendText(msg.to, group.displayName + " Profilenya Eror")
            elif msg.text.lower().startswith(mimic["setkey"]+'get pict ') or msg.text.lower().startswith(mimic["setkey"]+' get pict '):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            group = ki.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            ki.sendImageWithURL(msg.to,contact)
                        except:
                            group = ki.getContact(target)
                            ki.sendText(msg.to, group.displayName + " Profilenya Eror")
                else:
                    if msg.text.lower().startswith(mimic["setkey"]+' get pict '):
                        foo = mimic["setkey"]+' get pict '
                        key = len(foo)
                        key1 = msg.text[key:]
                        wiki = key1.replace("","")
                        gid = ki.getGroupIdsJoined()
                        for i in gid:
                            h = ki.getGroup(i).name
                            gna = ki.getGroup(i)
                            if h == wiki:
                                ki.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + gna.pictureStatus)
                    else:
                        foo = mimic["setkey"]+'get pict '
                        key = len(foo)
                        key1 = msg.text[key:]
                        wiki = key1.replace("","")
                        gid = ki.getGroupIdsJoined()
                        for i in gid:
                            h = ki.getGroup(i).name
                            gna = ki.getGroup(i)
                            if h == wiki:
                                ki.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + gna.pictureStatus)
            elif msg.text.lower().startswith(mimic["setkey"]+'accept ') or msg.text.lower().startswith(mimic["setkey"]+' accept '):
                if msg.text.lower().startswith(mimic["setkey"]+' accept '):
                    foo = mimic["setkey"]+' accept  '
                    key = len(foo)
                    key1 = msg.text[key:]
                    wiki = key1.replace("","")
                    gid = ki.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        h = ki.getGroup(i).name
                        gna = ki.getGroup(i)
                        _list += gid.name
                        if h == wiki:
                            ki.acceptGroupInvitation(i)
                        else:
                            pass
                        ki.sendText(msg.to,"Accept Group Invitation From Group: " + _list)
                else:
                    foo = mimic["setkey"]+'accept '
                    key = len(foo)
                    key1 = msg.text[key:]
                    wiki = key1.replace("","")
                    gid = ki.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        h = ki.getGroup(i).name
                        gna = ki.getGroup(i)
                        _list += gna.name
                        if h == wiki:
                            ki.acceptGroupInvitation(i)
                        else:
                            pass
                        ki.sendText(msg.to,"Accept Group Invitation From Group: " + _list)
            elif msg.text.lower().startswith(mimic["setkey"]+'runtime') or msg.text.lower().startswith(mimic["setkey"]+'runtime'):
                eltime = time.time() - mulai
                van = "「Psd bot activity」\n"+waktu(eltime)
                ki.sendText(msg.to,van)
            elif "getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ki.getContact(key1)
                cu = ki.channel.getCover(key1)
                try:
                    ki.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    ki.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif "getprofile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ki.getContact(key1)
                cu = ki.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    ki.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    ki.sendText(msg.to,"Profile Picture " + contact.displayName)
                    ki.sendImageWithURL(msg.to,image)
                    ki.sendText(msg.to,"Cover " + contact.displayName)
                    ki.sendImageWithURL(msg.to,path)
                except:
                    pass


            elif "getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = ki.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                ki.sendMessage(msg)

            elif "ppc" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ki.getContact(key1)
                cu = ki.channel.getCover(key1)
                try:
                    ki.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    ki.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))


            elif "getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ki.getContact(key1)
                cu = ki.channel.getCover(key1)
                try:
                    ki.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    ki.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
            elif msg.text.lower().startswith(mimic["setkey"]+'getid ') or msg.text.lower().startswith(mimic["setkey"]+' getid '):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    mi = ki.getContact(key1)
                    contact = "http://dl.profile.line-cdn.net/" + mi.pictureStatus
                    cu = ki.channel.getCover(key1)
                    path = str(cu)
                    ki.sendText(msg.to,"「Display Name」\n" + mi.displayName + "\n「Mid」\n" + key1 + "\n「Status」\n" + mi.statusMessage)
                    ki.sendImageWithURL(msg.to, path)
                    ki.sendImageWithURL(msg.to, contact)
                else:
                     if msg.text.lower().startswith(mimic["setkey"]+' getid '):
                         foo = mimic["setkey"]+' getid  '
                         key = len(foo)
                         key1 = msg.text[key:]
                         wiki = key1.replace("","")
                         gid = ki.getGroupIdsJoined()
                         for i in gid:
                             h = ki.getGroup(i).name
                             gna = ki.getGroup(i)
                             if h == wiki:
                                 try:
                                     GS = gna.creator.mid
                                     msg = Message()
                                     msg.to = msg.to
                                     msg.contentType = 13
                                     msg.contentMetadata = {'mid': GS}
                                     gCreator = gna.creator.displayName
                                 except:
                                     W = gna.members[0].mid
                                     msg = Message()
                                     msg.to = msg.to
                                     msg.contentType = 13
                                     msg.contentMetadata = {'mid': W}
                                     gCreator = gna.members[0].displayName
                                 if gna.invitee is None:
                                     sinvitee = "0"
                                 else:
                                     sinvitee = str(len(gna.invitee))
                                 if gna.preventJoinByTicket == True:
                                     u = "Disable"
                                 else:
                                     u = "line://ti/g/" + ki.reissueGroupTicket(i)
                                 contacts = ("「Group Name」\n" + str(gna.name) + "\n\n「Group ID」\n" + i + "\n\n「Group Creator」\n" + gCreator + "\n\nAnggota:" + str(len(gna.members)) + "\nInvitation:" + sinvitee + "\nTicket:" + u )
                                 ki.sendText(msg.to,contacts)
                                 ki.sendMessage(msg)
                     else:
                         foo = mimic["setkey"]+'getid '
                         key = len(foo)
                         key1 = msg.text[key:]
                         wiki = key1.replace("","")
                         gid = ki.getGroupIdsJoined()
                         for i in gid:
                             h = ki.getGroup(i).name
                             gna = ki.getGroup(i)
                             if h == wiki:
                                 try:
                                     GS = gna.creator.mid
                                     M = Message()
                                     M.to = msg.to
                                     M.contentType = 13
                                     M.contentMetadata = {'mid': GS}
                                     gCreator = gna.creator.displayName
                                 except:
                                     W = gna.members[0].mid
                                     M = Message()
                                     M.to = msg.to
                                     M.contentType = 13
                                     M.contentMetadata = {'mid': W}
                                     gCreator = gna.members[0].displayName
                                 if gna.invitee is None:
                                     sinvitee = "0"
                                 else:
                                     sinvitee = str(len(gna.invitee))
                                 if gna.preventJoinByTicket == True:
                                     u = "Disable"
                                 else:
                                     u = "line://ti/g/" + ki.reissueGroupTicket(i)
                                 contacts = ("「Group Name」\n" + str(gna.name) + "\n\n「Group ID」\n" + i + "\n\n「Group Creator」\n" + gCreator + "\n\nAnggota:" + str(len(gna.members)) + "\nInvitation:" + sinvitee + "\nTicket:" + u )
                                 ki.sendText(msg.to,contacts)
                                 ki.sendMessage(M)
            elif msg.text.lower().startswith(mimic["setkey"]+'micall') or msg.text.lower().startswith(mimic["setkey"]+' micall'):
                if msg.text.lower().startswith(mimic["setkey"]+' micall'):
                    foo = mimic["setkey"]+' micall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    nk0 = key1.replace("","")
                    _name = nk0
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                           targets.append(s.mid)
                    targets.remove(mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 mimic["target"][target] = True
                             except:
                                 ki.sendText(msg.to,"Error")
                else:
                    foo = mimic["setkey"]+'micall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    nk0 = key1.replace("","")
                    _name = nk0
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                           targets.append(s.mid)
                    targets.remove(mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 mimic["target"][target] = True
                             except:
                                 ki.sendText(msg.to,"Error")
            elif msg.text.lower().startswith(mimic["setkey"]+'unbanall') or msg.text.lower().startswith(mimic["setkey"]+' unbanall'):
                if msg.text.lower().startswith(mimic["setkey"]+' unbanall'):
                    foo = mimic["setkey"]+' unbanall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    nk0 = key1.replace("","")
                    _name = nk0
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                           targets.append(s.mid)
                    targets.remove(mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 del wait["blacklist"][target]
                                 f=codecs.open('st2__b.json','w','utf-8')
                                 json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                             except:
                                 pass
                else:
                    foo = mimic["setkey"]+'unbanall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    nk0 = key1.replace("","")
                    _name = nk0
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                           targets.append(s.mid)
                    targets.remove(mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 del wait["blacklist"][target]
                                 f=codecs.open('st2__b.json','w','utf-8')
                                 json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                             except:
                                 pass
            elif msg.text.lower().startswith(mimic["setkey"]+'banall') or msg.text.lower().startswith(mimic["setkey"]+' banall'):
                if msg.text.lower().startswith(mimic["setkey"]+' banall'):
                    foo = mimic["setkey"]+' banall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    nk0 = key1.replace("","")
                    _name = nk0
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                           targets.append(s.mid)
                    targets.remove(mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 wait["blacklist"][target] = True
                                 f=codecs.open('st2__b.json','w','utf-8')
                                 json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                             except:
                                 pass
                else:
                    foo = mimic["setkey"]+'banall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    nk0 = key1.replace("","")
                    _name = nk0
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                           targets.append(s.mid)
                    targets.remove(mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 wait["blacklist"][target] = True
                                 f=codecs.open('st2__b.json','w','utf-8')
                                 json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                             except:
                                 pass
            elif msg.text.lower().startswith(mimic["setkey"]+'teamall') or msg.text.lower().startswith(mimic["setkey"]+' teamall'):
                if msg.text.lower().startswith(mimic["setkey"]+' teamall'):
                    foo = mimic["setkey"]+' teamall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    nk0 = key1.replace("","")
                    _name = nk0
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                           targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 wait["bots"][target] = True
                                 f=codecs.open('bots.json','w','utf-8')
                                 json.dump(wait["bots"], f, sort_keys=True, indent=4,ensure_ascii=False)
                             except:
                                 pass
                else:
                    foo = mimic["setkey"]+'teamall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    nk0 = key1.replace("","")
                    _name = nk0
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                           targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 wait["bots"][target] = True
                                 f=codecs.open('bots.json','w','utf-8')
                                 json.dump(wait["bots"], f, sort_keys=True, indent=4,ensure_ascii=False)
                             except:
                                 pass
            elif msg.text.lower().startswith(mimic["setkey"]+'unteamall') or msg.text.lower().startswith(mimic["setkey"]+' unteamall'):
                if msg.text.lower().startswith(mimic["setkey"]+' unteamall'):
                    foo = mimic["setkey"]+' unteamall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    _name = key1.replace("","")
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                           targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 del wait["bots"][target]
                                 f=codecs.open('bots.json','w','utf-8')
                                 json.dump(wait["bots"], f, sort_keys=True, indent=4,ensure_ascii=False)
                             except:
                                 ki.sendText(msg.to,"")
                else:
                    foo = mimic["setkey"]+'unteamall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    _name = key1.replace("","")
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                           targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 del wait["bots"][target]
                                 f=codecs.open('bots.json','w','utf-8')
                                 json.dump(wait["bots"], f, sort_keys=True, indent=4,ensure_ascii=False)
                             except:
                                 ki.sendText(msg.to,"")
            elif msg.text.lower().startswith(mimic["setkey"]+'ban ') or msg.text.lower().startswith(mimic["setkey"]+' ban '):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            wait["blacklist"][target] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            group = ki.getContact(target)
                            ki.sendText(msg.to,group.displayName + " Succes Add to Blacklist")
                        except:
                            ki.sendText(msg.to,"Error")
                else:
                    pass
            elif msg.text.lower().startswith(mimic["setkey"]+'unban ') or msg.text.lower().startswith(mimic["setkey"]+' unban '):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del wait["blacklist"][target]
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            group = ki.getContact(target)
                            ki.sendText(msg.to,group.displayName + " Delete From Blacklist")
                        except:
                            group = ki.getContact(target)
                            ki.sendText(msg.to,group.displayName +" Not In Blacklist")
                else:
                    wait["dblacklist"] = True
                    ki.sendText(msg.to,"Send a contact to unban")
            elif msg.text.lower().startswith(mimic["setkey"]+'talkban ') or msg.text.lower().startswith(mimic["setkey"]+' talkban ') or msg.text.lower().startswith(mimic["setkey"]+'talkban') or msg.text.lower().startswith(mimic["setkey"]+' talkban'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            wait["talkblacklist"][target] = True
                            group = ki.getContact(target)
                            ki.sendText(msg.to,group.displayName + " Succes Add to Talkban")
                        except:
                            ki.sendText(msg.to,"Error")
                else:
                    wait["talkwblacklist"] = True
                    ki.sendText(msg.to,"Send a contact to talkban")
            elif msg.text.lower().startswith(mimic["setkey"]+'untalkban ') or msg.text.lower().startswith(mimic["setkey"]+' untalkban ') or msg.text.lower().startswith(mimic["setkey"]+'untalkban') or msg.text.lower().startswith(mimic["setkey"]+' untalkban'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del wait["talkblacklist"][target]
                            group = ki.getContact(target)
                            ki.sendText(msg.to,group.displayName + " Delete From Talkban")
                        except:
                            group = ki.getContact(target)
                            ki.sendText(msg.to,group.displayName + " Not In Talkban")
                else:
                    wait["talkdblacklist"] = True
                    ki.sendText(msg.to,"Send a contact to untalkban")
            elif msg.text.lower() == mimic["setkey"]+'ban:repeat' or msg.text.lower() == mimic["setkey"]+' ban:repeat':
                wait["twblacklist"] = True
                ki.sendText(msg.to,"Send a contact to ban")
            elif msg.text.lower() == mimic["setkey"]+'ban' or msg.text.lower() == mimic["setkey"]+' ban':
                wait["wblacklist"] = True
                ki.sendText(msg.to,"Send a contact to ban")
            elif msg.text.lower() == mimic["setkey"]+'unban' or msg.text.lower() == mimic["setkey"]+' unban':
                wait["dblacklist"] = True
                ki.sendText(msg.to,"Send a contact to unban")
            elif msg.text.lower() == mimic["setkey"]+'unban:repeat' or msg.text.lower() == mimic["setkey"]+' unban:repeat':
                wait["tdblacklist"] = True
                ki.sendText(msg.to,"Send a contact to unban")
            elif msg.text.lower() == mimic["setkey"]+'abort' or msg.text.lower() == mimic["setkey"]+' abort':
                wait["twblacklist"] = False
                wait["tdblacklist"] = False
                ki.sendText(msg.to,"「Abort」\nAbort operation♪")
            elif msg.text.lower().startswith(mimic["setkey"]+'mimic add ') or msg.text.lower().startswith(mimic["setkey"]+' mimic add ') or msg.text.lower().startswith(mimic["setkey"]+'mimic add') or msg.text.lower().startswith(mimic["setkey"]+' mimic add'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            mimic["target"][target] = True
                            group = ki.getContact(target)
                            ki.sendText(msg.to,"「Mimic」\n" + group.displayName + " Add To Mimic List")
                            ki.sendMessageWithMention(msg.to,target)
                            break
                        except:
                            fail.sendText(msg.to,"")
                            break
                else:
                    ki.sendText(msg.to,"「Mimic」\nYou need to mention a user♪")
            elif msg.text.lower().startswith(mimic["setkey"]+'mimic del ') or msg.text.lower().startswith(mimic["setkey"]+' mimic del ') or msg.text.lower().startswith(mimic["setkey"]+'mimic del') or msg.text.lower().startswith(mimic["setkey"]+' mimic del'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del mimic["target"][target]
                            group = ki.getContact(target)
                            ki.sendText(msg.to,"「Mimic」\n" + group.displayName + " Delete From Mimic List")
                            break
                        except:
                            group = ki.getContact(target)
                            ki.sendText(msg.to,"「Mimic」\n" + group.displayName + " Not in Mimic List")
                            break
                else:
                    ki.sendText(msg.to,"「Mimic」\nYou need to mention a user♪")
            elif msg.text.lower().startswith(mimic["setkey"]+'invite ') or msg.text.lower().startswith(mimic["setkey"]+' invite '):
                if msg.text.lower().startswith(mimic["setkey"]+' invite '):
                    foo = mimic["setkey"]+' invite '
                    key = len(foo)
                    key1 = msg.text[key:]
                    contact = ki.getContact(key1)
                    ki.findAndAddContactsByMid(key1)
                    ki.inviteIntoGroup(msg.to, [key1])
                else:
                    foo = mimic["setkey"]+'invite '
                    key = len(foo)
                    key1 = msg.text[key:]
                    contact = ki.getContact(key1)
                    ki.findAndAddContactsByMid(key1)
                    ki.inviteIntoGroup(msg.to, [key1])
            elif msg.text.lower() == mimic["setkey"]+' instagram' or msg.text.lower() == mimic["setkey"]+'instagram':
                ki.sendText(msg.to,"「Instagram」\nUsage:" + mimic["setkey"].title()+" instagram <username>")
            elif msg.text.lower().startswith(mimic["setkey"]+'instagram ') or msg.text.lower().startswith(mimic["setkey"]+' instagram '):
                if msg.text.lower().startswith(mimic["setkey"]+' instagram '):
                    foo = mimic["setkey"]+' instagram '
                    key = len(foo)
                    key1 = msg.text[key:]
                    instagram = key1.replace("","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "PSD INSTAGRAM INFO\n"
                    details = "\nPSD INSTAGRAM INFO"
                    ki.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    ki.sendImageWithURL(msg.to, text1[0])
                else:
                    foo = mimic["setkey"]+'instagram '
                    key = len(foo)
                    key1 = msg.text[key:]
                    instagram = key1.replace("","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "PSD INSTAGRAM INFO\n"
                    details = "\nPSD INSTAGRAM INFO"
                    ki.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    ki.sendImageWithURL(msg.to, text1[0])
            elif msg.text.lower() == mimic["setkey"]+' youtube' or msg.text.lower() == mimic["setkey"]+'youtube':
                ki.sendText(msg.to,"「Youtube」\nUsage:" + mimic["setkey"].title()+" youtube <payung teduh - akad>")
            elif msg.text.lower().startswith(mimic["setkey"]+'youtube') or msg.text.lower().startswith(mimic["setkey"]+' youtube'):
                if msg.text.lower().startswith(mimic["setkey"]+' youtube'):
                    query = msg.text.split(" ")
                    try:
                        if len(query) == 3:
                            isi = yt(query[2])
                            hasil = isi[int(query[1])-1]
                            ki.sendText(msg.to, hasil)
                        else:
                            isi = yt(query[1])
                            ki.sendText(msg.to, isi[0])
                    except Exception as e:
                        ki.sendText(msg.to, str(e))
                else:
                    query = msg.text.split(" ")
                    try:
                        if len(query) == 3:
                            isi = yt(query[2])
                            hasil = isi[int(query[1])-1]
                            ki.sendText(msg.to, hasil)
                        else:
                            isi = yt(query[1])
                            ki.sendText(msg.to, isi[0])
                    except Exception as e:
                        ki.sendText(msg.to, str(e))
            elif msg.text.lower() == mimic["setkey"]+' image' or msg.text.lower() == mimic["setkey"]+'image':
                ki.sendText(msg.to,"「Google Image」\nUsage:" + mimic["setkey"].title()+" image <sarada>")
            elif msg.text.lower() == mimic["setkey"]+' about' or msg.text.lower() == mimic["setkey"]+'about':
                today = date.today()
                future = date(2018,01,25)
                days = (str(future - today))
                comma = days.find(",")
                days = days[:comma]
                ki.sendText(msg.to,"「About」\n✡ agus squad ✡\n ▩▣ᴘ͓̽͟͟s͓̽͟͟ᴅ͓̽͟͟ ᴛ͓̽͟͟ᴇ͓̽͟͟ᴀ͓̽͟͟ᴍ͓̽͟͟ ʙ͓̽͟͟ᴏ͓̽͟͟ᴛ͓̽͟͟ ▣▩ 'Self' Edition♪\n「Subscription」\nExpired: 2018-01,25" + "\nIn days: " + days + "\nKey:"+mimic["setkey"] + "\n\n「Contact」\n・ LINE: line://ti/p/~agustri1990")
            elif msg.text.lower() == mimic["setkey"]+' get pict' or msg.text.lower() == mimic["setkey"]+'get pict':
                if msg.toType == 2:
                    try:
                        group = ki.getGroup(msg.to)
                        contact = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                        ki.sendImageWithURL(msg.to,contact)
                    except:
                        group = ki.getGroup(msg.to)
                        ki.sendText(msg.to, group.displayName + " Profilenya Eror")
                else:
                    try:
                        group = ki.getContact(msg.to)
                        contact = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                        ki.sendImageWithURL(msg.to,contact)
                    except:
                        group = ki.getContact(msg.to)
                        ki.sendText(msg.to, group.displayName + " Profilenya Eror")
            elif msg.text.lower() == mimic["setkey"]+' getinfo' or msg.text.lower() == mimic["setkey"]+'getinfo':
                if msg.toType == 2:
                        contact = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                        ki.sendImageWithURL(msg.to,contact)
                        ki.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        ki.kepo1(msg.to,"")
                        ki.kepoContact(msg.to,"")
                else:
                    ki.kepo(msg.to,"")
                    ki.kepoContact1(msg.to,"")
            elif msg.text.lower().startswith(mimic["setkey"]+'image ') or msg.text.lower().startswith(mimic["setkey"]+' image '):
                if msg.text.lower().startswith(mimic["setkey"]+' image '):
                    foo = mimic["setkey"]+' image '
                    key = len(foo)
                    key1 = msg.text[key:]
                    wiki = key1.replace("","")
                    url = 'https://www.google.com/search?hl=en&biw=1366&bih=659&tbm=isch&sa=1&ei=vSD9WYimHMWHvQTg_53IDw&q=' + wiki
                    raw_html =  (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    try:
                        start = timeit.timeit()
                        ki.sendImageWithURL(msg.to,path)
                        ki.sendText(msg.to, "「Google Image」\nType: Search Image\nTime taken: %s" % (start) +"\nTotal Image Links = "+str(len(items)))
                    except Exception as e:
                        ki.sendText(msg.to, str(e))
                else:
                    foo = mimic["setkey"]+'image '
                    key = len(foo)
                    key1 = msg.text[key:]
                    wiki = key1.replace("","")
                    url = 'https://www.google.com/search?hl=en&biw=1366&bih=659&tbm=isch&sa=1&ei=vSD9WYimHMWHvQTg_53IDw&q=' + wiki
                    raw_html =  (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    try:
                        start = timeit.timeit()
                        ki.sendImageWithURL(msg.to,path)
                        ki.sendText(msg.to, "「Google Image」\nType: Search Image\nTime taken: %s" % (start) +"\nTotal Image Links = "+str(len(items)))
                    except Exception as e:
                        ki.sendText(msg.to, str(e))
            elif msg.text.lower().startswith(mimic["setkey"]+'say@id ') or msg.text.lower().startswith(mimic["setkey"]+' say@id '):
                if msg.text.lower().startswith(mimic["setkey"]+' say@id '):
                    foo = mimic["setkey"]+' say@id '
                    key = len(foo)
                    key1 = msg.text[key:]
                    wiki = key1.replace("","")
                    tts = gTTS(text=wiki, lang='id')
                    tts.save('nzet.mp3')
                    ki.sendAudio(msg.to,'nzet.mp3')
                else:
                    foo = mimic["setkey"]+'say@id '
                    key = len(foo)
                    key1 = msg.text[key:]
                    wiki = key1.replace("","")
                    tts = gTTS(text=wiki, lang='id')
                    tts.save('nzet.mp3')
                    ki.sendAudio(msg.to,'nzet.mp3')
            elif msg.text.lower() == mimic["setkey"]+' wikipedia' or msg.text.lower() == mimic["setkey"]+'wikipedia':
                ki.sendText(msg.to,"「Wikipedia」\nUsage:" + mimic["setkey"].title()+" wikipedia <naruto>")
            elif msg.text.lower().startswith(mimic["setkey"]+'wikipedia ') or msg.text.lower().startswith(mimic["setkey"]+' wikipedia '):
                if msg.text.lower().startswith(mimic["setkey"]+' wikipedia '):
                  try:
                      foo = mimic["setkey"]+' wikipedia '
                      key = len(foo)
                      key1 = msg.text[key:]
                      wiki = key1.replace("","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      ki.sendText(msg.to, pesan)
                  except:
                      try:
                          foo = mimic["setkey"]+' wikipedia '
                          key = len(foo)
                          key1 = msg.text[key:]
                          wiki = key1.replace("","")
                          wikipedia.set_lang("en")
                          pesan="Title ("
                          pesan+=wikipedia.page(wiki).title
                          pesan+=")\n\n"
                          pesan+=wikipedia.summary(wiki, sentences=1)
                          pesan+="\n"
                          pesan+=wikipedia.page(wiki).url
                          ki.sendText(msg.to, pesan)
                      except:
                          try:
                              pesan="Text Banyak Silahkan Click link ini\n"
                              pesan+=wikipedia.page(wiki).url
                              ki.sendText(msg.to, pesan)
                          except Exception as e:
                              ki.sendText(msg.to, str(e))
                else:
                  try:
                      foo = mimic["setkey"]+'wikipedia '
                      key = len(foo)
                      key1 = msg.text[key:]
                      wiki = key1.replace("","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      ki.sendText(msg.to, pesan)
                  except:
                      try:
                          foo = mimic["setkey"]+'wikipedia '
                          key = len(foo)
                          key1 = msg.text[key:]
                          wiki = key1.replace("","")
                          wikipedia.set_lang("en")
                          pesan="Title ("
                          pesan+=wikipedia.page(wiki).title
                          pesan+=")\n\n"
                          pesan+=wikipedia.summary(wiki, sentences=1)
                          pesan+="\n"
                          pesan+=wikipedia.page(wiki).url
                          ki.sendText(msg.to, pesan)
                      except:
                          try:
                              pesan="Text Banyak Silahkan Click link ini\n"
                              pesan+=wikipedia.page(wiki).url
                              ki.sendText(msg.to, pesan)
                          except Exception as e:
                              ki.sendText(msg.to, str(e))
            elif msg.text.lower() == mimic["setkey"]+' lyric' or msg.text.lower() == mimic["setkey"]+'lyric':
                ki.sendText(msg.to,"「Lyric」\nUsage:" + mimic["setkey"].title()+" lyric <nella kharisma - jaran goyang>")
            elif msg.text.lower().startswith(mimic["setkey"]+'lyric ') or msg.text.lower().startswith(mimic["setkey"]+' lyric '):
                if msg.text.lower().startswith(mimic["setkey"]+' lyric '):
                    foo = mimic["setkey"]+' lyric '
                    key = len(foo)
                    key1 = msg.text[key:]
                    songname = key1.replace('','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        ki.sendText(msg.to, hasil)
                else:
                    foo = mimic["setkey"]+'lyric '
                    key = len(foo)
                    key1 = msg.text[key:]
                    songname = key1.replace('','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        ki.sendText(msg.to, hasil)
            elif msg.text.lower() == mimic["setkey"]+' music' or msg.text.lower() == mimic["setkey"]+'music':
                ki.sendText(msg.to,"「Music」\nUsage:" + mimic["setkey"].title()+" music <nella kharisma - jaran goyang>")
            elif msg.text.lower() == mimic["setkey"]+' say@id' or msg.text.lower() == mimic["setkey"]+'say@id':
                ki.sendText(msg.to,"「Text To Speech」\nUsage:" + mimic["setkey"].title()+" say@id <query>")
            elif msg.text.lower().startswith(mimic["setkey"]+'music ') or msg.text.lower().startswith(mimic["setkey"]+' music '):
                if msg.text.lower().startswith(mimic["setkey"]+' music '):
                    foo = mimic["setkey"]+' music '
                    key = len(foo)
                    key1 = msg.text[key:]
                    songname = key1.replace('','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        ki.sendText(msg.to, hasil)
                        ki.sendText(msg.to, "Please Wait for audio...")
                        ki.sendAudioWithURL(msg.to, song[4])
                else:
                    foo = mimic["setkey"]+'music '
                    key = len(foo)
                    key1 = msg.text[key:]
                    songname = key1.replace('','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        ki.sendText(msg.to, hasil)
                        ki.sendText(msg.to, "Please Wait for audio...")
                        ki.sendAudioWithURL(msg.to, song[4])
 #          Settings on off
            elif msg.text.lower() == mimic["setkey"]+' autoadd' or msg.text.lower() == mimic["setkey"]+'autoadd':
                if wait['autoAdd'] == True:
                    if wait["autoaddpesan"] == '':
                        msgs="「Auto Add」\nAdd Back: True♪\nAdd Message: False♪\n\n\n"
                    else:
                        msgs="「Auto Add」\nAdd Back: True♪\nAdd Message: True♪"
                        msgs+="\n" + wait['autoaddpesan'] + "\n\n"
                else:
                    if wait["autoaddpesan"] == '':
                        msgs="「Auto Add」\nAdd Back: False♪\nAdd Message: False♪\n\n\n"
                    else:
                        msgs="「Auto Add」\nAdd Back: False♪\nAdd Message: True♪"
                        msgs+="\n" + wait['autoaddpesan'] + "\n\n"
                ki.sendText(msg.to, msgs + "Commands:\n" \
					+mimic["setkey"].title()+" autoadd on\n" \
					+mimic["setkey"].title()+" autoadd off\n" \
					+mimic["setkey"].title()+" autoadd msg set\n" \
					+mimic["setkey"].title()+" autoadd msg clear")
            elif msg.text.lower() == mimic["setkey"]+' autoadd on' or msg.text.lower() == mimic["setkey"]+'autoadd on':
                if wait['autoAdd'] == True:
                    msgs="「Auto Add」\nAuto Add already ENABLED♪"
                else:
                    msgs="「Auto Add」\nAuto Add set to ENABLED♪"
                    wait['autoAdd']=True
                ki.sendText(msg.to, msgs)
            elif msg.text.lower() == mimic["setkey"]+' autoadd off' or msg.text.lower() == mimic["setkey"]+'autoadd off':
                if wait['autoAdd'] == False:
                    msgs="「Auto Add」\nAuto Add already DISABLED♪\nNote: Auto add message is not affected♪"
                else:
                    msgs="「Auto Add」\nAuto Add set to DISABLED♪\nNote: Auto add message is not affected♪"
                    wait['autoAdd']=False
                ki.sendText(msg.to, msgs)
            elif msg.text.lower().startswith(mimic["setkey"]+'autoadd msg set\n'):
                foo = mimic["setkey"]+'autoadd msg set\n'
                key = len(foo)
                print(key)
                key1 = msg.text[key:]
                wait["autoaddpesan"] = key1
                ki.sendText(msg.to,"「Auto Add」\nAuto add message has been set to:\n" + wait["autoaddpesan"])
            elif msg.text.lower() == mimic["setkey"]+' autoadd msg clear' or msg.text.lower() == mimic["setkey"]+'autoadd msg clear':
                autoadd = wait["autoaddpesan"]
                msgs="「Auto Add」\nAuto add message DISABLED♪\nMessage backup:"
                msgs+="\n" + autoadd
                ki.sendText(msg.to, msgs)
                wait["autoaddpesan"] = ""
            elif msg.text.lower() == mimic["setkey"]+' mimic' or msg.text.lower() == mimic["setkey"]+'mimic':
                if mimic["target"] == {}:
                    ki.sendText(msg.to,"「Mimic」\nCurrently not mimicking anyone♪\n\nCommands:\n" + mimic["setkey"]+" mimic on\n" +  mimic["setkey"]+" mimic off\n" + mimic["setkey"]+" mimic add <@|~>\n" + mimic["setkey"]+" mimic del <@|~>")
                else:
                    nZetFriend = ki.getContacts(mimic["target"])
                    ki.sendText(msg.to, "Please wait...")
                    num=1
                    msgs="「Mimic」\nMimicking:"
                    for ids in nZetFriend:
                        msgs+="\n%i. %s♪" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n「Total %i Mimicking」\n" % len(mimic["target"])
                    ki.sendText(msg.to, msgs + "Commands:\n" +  mimic["setkey"]+" mimic on\n" +  mimic["setkey"]+" mimic off\n" + mimic["setkey"]+" mimic add <@|~>\n" + mimic["setkey"]+" mimic del <@|~>")
            elif msg.text.lower() == 'setkey':
                if mimic["setkey"] == '':
                    ki.sendText(msg.to,"Your Key: DISABLED♪\nSetkey set - Set Your Key\nSetkey off - Disable Your Key\nSetkey reset - Reset Your Key")
                else:
                    ki.sendText(msg.to,"Your Key: " + mimic["setkey"].title() + "\nSetKey: - Set Your Key\nSetkey Off - Disable Your Key\nSetkey Reset - Reset Your Key")
            elif msg.text.lower() == mimic["setkey"]+' mimic on' or msg.text.lower() == mimic["setkey"]+'mimic on':
                if mimic["status"] == True:
                    msgs="「Mimic」\nMimic already ENABLED♪"
                else:
                    msgs="「Mimic」\nMimic set to ENABLED♪"
                    mimic["status"]=True
                ki.sendText(msg.to, msgs)
            elif msg.text.lower() == mimic["setkey"]+' mimic off' or msg.text.lower() == mimic["setkey"]+'mimic off':
                if mimic["status"] == False:
                    msgs="「Mimic」\nMimic already DISABLED♪"
                else:
                    msgs="「Mimic」\nMimic set to DISABLED♪"
                    mimic["status"]=False
                ki.sendText(msg.to, msgs)
            elif msg.text.lower() == mimic["setkey"]+'date':
                ki.sendText(msg.to, " Tanggal " + datetime.now().strftime('%d/%m/%y Jam Is %H:%M:%S') )
            elif msg.text.lower() == mimic["setkey"]+' autojoin' or msg.text.lower() == mimic["setkey"]+'autojoin':
                if wait['autoJoin'] == True:
                        msgs="「Auto Join」\nState: ENABLED♪\n"
                else:
                        msgs="「Auto Join」\nState: DISABLED♪\n"
                ki.sendText(msg.to, msgs + "Commands:\n" \
					+mimic["setkey"].title()+" autojoin on \n" \
					+mimic["setkey"].title()+" autojoin off ")
            elif msg.text.lower() == mimic["setkey"]+' autojoin on' or msg.text.lower() == mimic["setkey"]+'autojoin on':
                if wait['autoJoin'] == True:
                    msgs="「Auto Join」\nAuto Join already set to ENABLED♪"
                else:
                    msgs="「Auto Join」\nAuto Join has been set to ENABLED♪"
                    wait['autoJoin']=True
                ki.sendText(msg.to, msgs)
            elif msg.text.lower() == mimic["setkey"]+' autojoin off' or msg.text.lower() == mimic["setkey"]+'autojoin off':
                if wait['autoJoin'] == False:
                    msgs="「Auto Join」\nAuto Auto Join already set to DISABLED♪"
                else:
                    msgs="「Auto Join」\nAuto Join has been set to DISABLED♪"
                    wait['autoJoin']=False
                ki.sendText(msg.to, msgs)
            elif msg.text.lower().startswith(mimic["setkey"]+'hitung'):
                bb = "╠・ @x \n"
                print(len(bb))
                aa = "╔═══════════════\n" + bb
                print(len(aa))
            elif msg.text.lower() == mimic["setkey"]+' me' or msg.text.lower() == mimic["setkey"]+'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                ki.sendMessage(msg)
            elif msg.text.lower() == mimic["setkey"]+' bot' or msg.text.lower() == mimic["setkey"]+'bot':
                if Botsa == []:
                    ki.sendText(msg.to,"Nothing in the blacklist")
                else:
                    ki.sendText(msg.to,"╠・PSD BOT TEAM・═══════════════")
                    mc = ""
                    for mi_d in Botsa:
                        msg.contentType = 13
		        msg.contentMetadata = {'mid': mi_d}
		        ki.sendMessage(msg)
            elif msg.text.lower() == mimic["setkey"]+'ourl' or msg.text.lower() == mimic["setkey"]+' ourl':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    ki.updateGroup(group)
                else:
                        ki.sendText(msg.to,"It can not be used outside the group")
            elif msg.text.lower() == mimic["setkey"]+'ourl1':
                if msg.toType == 2:
                    group = ki1.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    ki1.updateGroup(group)
                else:
                        ki1.sendText(msg.to,"It can not be used outside the group")
            elif msg.text.lower() == mimic["setkey"]+'ourl2':
                if msg.toType == 2:
                    group = ki2.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    ki2.updateGroup(group)
                else:
                        ki2.sendText(msg.to,"It can not be used outside the group")
            elif msg.text.lower() == mimic["setkey"]+'ourl3':
                if msg.toType == 2:
                    group = ki3.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    ki3.updateGroup(group)
                else:
                        ki3.sendText(msg.to,"It can not be used outside the group")
            elif msg.text.lower() == mimic["setkey"]+'ourl4':
                if msg.toType == 2:
                    group = ki4.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    ki4.updateGroup(group)
                else:
                        ki4.sendText(msg.to,"It can not be used outside the group")
            elif msg.text.lower() == mimic["setkey"]+'ourl5':
                if msg.toType == 2:
                    group = ki5.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    ki5.updateGroup(group)
                else:
                        ki5.sendText(msg.to,"It can not be used outside the group")
            elif msg.text.lower() == mimic["setkey"]+'curl' or msg.text.lower() == mimic["setkey"]+' curl':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    ki.updateGroup(group)
                else:
                        ki.sendText(msg.to,"It can not be used outside the group")
            elif msg.text.lower() == mimic["setkey"]+'invite:gcreator' or msg.text.lower() == mimic["setkey"]+' invite:gcreator':
                if msg.toType == 2:
                       ginfo = ki.getGroup(msg.to)
                       try:
                           gcmid = ginfo.creator.mid
                           ki.inviteIntoGroup(msg.to,[gcmid])
                       except:
                           gcmid = "Error"
                           ki.inviteIntoGroup(msg.to,[gcmid])
            elif msg.text.lower() == mimic["setkey"]+'bot:gcreator' or msg.text.lower() == mimic["setkey"]+' bot:gcreator':
                if msg.toType == 2:
                       ginfo = ki1.getGroup(msg.to)
                       try:
                           gcmid = ginfo.creator.mid
                           ki1.inviteIntoGroup(msg.to,[gcmid])
                       except:
                           gcmid = "Error"
                           ki1.inviteIntoGroup(msg.to,[gcmid])
            elif msg.text.lower() == mimic["setkey"]+'bio' or msg.text.lower() == mimic["setkey"]+' bio':
                    profile = ki.getProfile()
                    ki.sendText(msg.to, profile.statusMessage)
            elif msg.text.lower() == mimic["setkey"]+'pictstatus' or msg.text.lower() == mimic["setkey"]+' pictstatus':
                    profile = ki.getProfile()
                    ki.sendText(msg.to, "http://dl.profile.line-cdn.net/"  + profile.pictureStatus)
            elif msg.text.lower() == mimic["setkey"]+'pp' or msg.text.lower() == mimic["setkey"]+' pp':
                    profile = ki.getProfile()
                    ki.sendImageWithURL(msg.to, "http://dl.profile.line-cdn.net/"  + profile.pictureStatus)
            elif msg.text.lower() == mimic["setkey"]+'sampul' or msg.text.lower() == mimic["setkey"]+' sampul':
                    h = ki.getHome(mid)
                    objId = h["result"]["homeInfo"]["objectId"]
                    ki.sendImageWithURL(msg.to, "http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + mid + "&oid=" + objId)
            elif msg.text.lower() == mimic["setkey"]+'sp' or msg.text.lower() == mimic["setkey"]+' sp':
                start = time.time()
                ki.sendText(msg.to, "「Debug」\nType: speed\ngratis aing mah..")
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "「Debug」\nType: speed\nTime taken: %s" % (elapsed_time))
            #elif msg.text.lower() == mimic["setkey"]+'clone' or msg.text.lower() == mimic["setkey"]+' clone':
            #    ki.cloneContact(nZetsu)
            elif msg.text.lower() == mimic["setkey"]+'mid' or msg.text.lower() == mimic["setkey"]+' mid':
                ki.sendText(msg.to,msg.from_)
            elif msg.text.lower().startswith(mimic["setkey"]+'allbio:'):
                if msg.text.lower().startswith(mimic["setkey"]+' allbio:'):
                    foo = mimic["setkey"]+' allbio:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki1.getProfile()
                        profile.statusMessage = string
                        ki1.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki2.getProfile()
                        profile.statusMessage = string
                        ki2.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki3.getProfile()
                        profile.statusMessage = string
                        ki3.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki4.getProfile()
                        profile.statusMessage = string
                        ki4.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki5.getProfile()
                        profile.statusMessage = string
                        ki5.updateProfile(profile)
                        ki.sendText(msg.to,"Bio berubah menjadi:\n" + string + "")
                else:
                    foo = mimic["setkey"]+'allbio:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki1.getProfile()
                        profile.statusMessage = string
                        ki1.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki2.getProfile()
                        profile.statusMessage = string
                        ki2.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki3.getProfile()
                        profile.statusMessage = string
                        ki3.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki4.getProfile()
                        profile.statusMessage = string
                        ki4.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki5.getProfile()
                        profile.statusMessage = string
                        ki5.updateProfile(profile)
                        ki.sendText(msg.to,"Bio berubah menjadi:\n" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+' tr id@en '):
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = str(msg.text.lower().replace(mimic["setkey"]+' tr id@en ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.sendText(msg.to,"TRANSLATENYA\n" + "" + kata + "\nTERJEMAHANNYA\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+' tr ja@id '):
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = str(msg.text.lower().replace(mimic["setkey"]+' tr ja@id ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.sendText(msg.to,"TRANSLATENYA\n" + "" + kata + "\nTERJEMAHANNYA\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+' tr en@id '):
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = str(msg.text.lower().replace(mimic["setkey"]+' tr en@id ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.sendText(msg.to,"TRANSLATENYA\n" + "" + kata + "\nTERJEMAHANNYA\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+' tr th@id '):
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = str(msg.text.lower().replace(mimic["setkey"]+' tr th@id ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.sendText(msg.to,"TRANSLATENYA\n" + "" + kata + "\nTERJEMAHANNYA\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+' tr id@jp '):
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = str(msg.text.lower().replace(mimic["setkey"]+' tr id@jp ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.sendText(msg.to,"TRANSLATENYA\n" + "" + kata + "\nTERJEMAHANNYA\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+' tr id@th '):
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = str(msg.text.lower().replace(mimic["setkey"]+' tr id@th ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.sendText(msg.to,"TRANSLATENYA\n" + "" + kata + "\nTERJEMAHANNYA\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+'tr id@en '):
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = str(msg.text.lower().replace(mimic["setkey"]+'tr id@en ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.sendText(msg.to,"TRANSLATENYA\n" + "" + kata + "\nTERJEMAHANNYA\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+'tr ja@id '):
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = str(msg.text.lower().replace(mimic["setkey"]+'tr ja@id ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.sendText(msg.to,"TRANSLATENYA\n" + "" + kata + "\nTERJEMAHANNYA\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+'tr en@id '):
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = str(msg.text.lower().replace(mimic["setkey"]+'tr en@id ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.sendText(msg.to,"TRANSLATENYA\n" + "" + kata + "\nTERJEMAHANNYA\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+'tr th@id '):
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = str(msg.text.lower().replace(mimic["setkey"]+'tr th@id ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.sendText(msg.to,"TRANSLATENYA\n" + "" + kata + "\nTERJEMAHANNYA\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+'tr id@jp '):
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = str(msg.text.lower().replace(mimic["setkey"]+'tr id@jp ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.sendText(msg.to,"TRANSLATENYA\n" + "" + kata + "\nTERJEMAHANNYA\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+'tr id@th '):
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = str(msg.text.lower().replace(mimic["setkey"]+'tr id@th ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.sendText(msg.to,"TRANSLATENYA\n" + "" + kata + "\nTERJEMAHANNYA\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+'myname:') or msg.text.lower().startswith(mimic["setkey"]+' myname:'):
                if msg.text.lower().startswith(mimic["setkey"]+' myname:'):
                    foo = mimic["setkey"]+'myname:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500000:
                        profile = ki.getProfile()
                        profile.displayName = string
                        ki.updateProfile(profile)
                        ki.sendText(msg.to,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'myname:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500000:
                        profile = ki.getProfile()
                        profile.displayName = string
                        ki.updateProfile(profile)
                        ki.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'tl:') or msg.text.lower().startswith(mimic["setkey"]+' tl:'):
                if msg.text.lower().startswith(mimic["setkey"]+' tl:'):
                    foo = mimic["setkey"]+' tl:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    tl_text = key1
                    ki.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+ki.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
                else:
                    foo = mimic["setkey"]+'tl:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    tl_text = key1
                    ki.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+ki.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text.lower().startswith(mimic["setkey"]+'gn ') or msg.text.lower().startswith(mimic["setkey"]+' gn '):
                if msg.text.lower().startswith(mimic["setkey"]+' gn '):
                    foo = mimic["setkey"]+' gn '
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode("utf-8")) <= 500:
                        profile = ki.getGroup(msg.to)
                        profile.name = string
                        ki.updateGroup(profile)
                        ki.sendText(msg.to,"GroupName change to " + string + " success")
                else:
                    foo = mimic["setkey"]+'gn '
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode("utf-8")) <= 500:
                        profile = ki.getGroup(msg.to)
                        profile.name = string
                        ki.updateGroup(profile)
                        ki.sendText(msg.to,"GroupName change to " + string + " success")
            elif msg.text.lower().startswith(mimic["setkey"]+'mybio:') or msg.text.lower().startswith(mimic["setkey"]+' mybio:'):
                if msg.text.lower().startswith(mimic["setkey"]+' mybio:'):
                    foo = mimic["setkey"]+' mybio:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki.getProfile()
                        profile.statusMessage = string
                        ki.updateProfile(profile)
                        ki.sendText(msg.to,"Update Bio" + string + "")
                else:
                    foo = mimic["setkey"]+'mybio:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki.getProfile()
                        profile.statusMessage = string
                        ki.updateProfile(profile)
                        ki.sendText(msg.to,"Update Bio" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name1:') or msg.text.lower().startswith(mimic["setkey"]+' name1:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name1:'):
                    foo = mimic["setkey"]+' name1:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki1.getProfile()
                        profile.displayName = string
                        ki1.updateProfile(profile)
                        ki1.sendText(msg.to,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name1:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki1.getProfile()
                        profile.displayName = string
                        ki1.updateProfile(profile)
                        ki1.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name2:') or msg.text.lower().startswith(mimic["setkey"]+' name2:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name2:'):
                    foo = mimic["setkey"]+' name2:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki2.getProfile()
                        profile.displayName = string
                        ki2.updateProfile(profile)
                        ki2.sendText(msg.to,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name2:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki2.getProfile()
                        profile.displayName = string
                        ki2.updateProfile(profile)
                        ki2.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name3:') or msg.text.lower().startswith(mimic["setkey"]+' name3:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name3:'):
                    foo = mimic["setkey"]+' name3:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki3.getProfile()
                        profile.displayName = string
                        ki3.updateProfile(profile)
                        ki3.sendText(msg.to,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name3:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki3.getProfile()
                        profile.displayName = string
                        ki3.updateProfile(profile)
                        ki3.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name4:') or msg.text.lower().startswith(mimic["setkey"]+' name4:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name4:'):
                    foo = mimic["setkey"]+' name4:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki4.getProfile()
                        profile.displayName = string
                        ki4.updateProfile(profile)
                        ki4.sendText(msg.to,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name4:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki4.getProfile()
                        profile.displayName = string
                        ki4.updateProfile(profile)
                        ki4.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "Gcancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        ki.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        ki.sendText(msg.to,["members"] + "Kelompok berikut yang diundang akan ditolak secara otomatis")
                except:
                        ki.sendText(msg.to,"Nilai tidak benar")
            elif msg.text.lower().startswith(mimic["setkey"]+'mayhem') or msg.text.lower().startswith(mimic["setkey"]+' mayhem'):
                if msg.text.lower().startswith(mimic["setkey"]+' mayhem'):
                    foo = mimic["setkey"]+' mayhem'
                    key = len(foo)
                    key1 = msg.text[key:]
                    _name = key1.replace("","")
                    gs = ki.getGroup(msg.to)
                    ki.sendText(msg.to,"「 Mayhem 」\nMayhem is STARTING♪\n'abort' to abort ♪""")
                    ki.sendText(msg.to,"「 Mayhem 」\n %i victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/" % len(gs.members))
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    for target in targets:
                        if not target in Bots:
                            try:
                                random.choice(P1).kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"「 Mayhem 」\nMayhem is STARTING♪\n'abort' to abort ♪""")
                                ki.sendText(msg.to,"「 Mayhem 」\n %i victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/" % len(gs.members))
                else:
                    foo = mimic["setkey"]+'mayhem'
                    key = len(foo)
                    key1 = msg.text[key:]
                    _name = key1.replace("","")
                    gs = ki.getGroup(msg.to)
                    ki.sendText(msg.to,"「 Mayhem 」\nMayhem is STARTING♪\n'abort' to abort ♪""")
                    ki.sendText(msg.to,"「 Mayhem 」\n %i victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/" % len(gs.members))
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    for target in targets:
                        if not target in Bots:
                            try:
                                random.choice(P1).kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"「 Mayhem 」\nMayhem is STARTING♪\n'abort' to abort ♪""")
                                ki.sendText(msg.to,"「 Mayhem 」\n %i victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/" % len(gs.members))
            elif msg.text.lower().startswith(mimic["setkey"]+'mayhemme') or msg.text.lower().startswith(mimic["setkey"]+' mayhemme'):
                if msg.text.lower().startswith(mimic["setkey"]+' mayhem'):
                    foo = mimic["setkey"]+' mayhem'
                    key = len(foo)
                    key1 = msg.text[key:]
                    _name = key1.replace("","")
                    gs = ki.getGroup(msg.to)
                    ki.sendText(msg.to,"「 Mayhemme 」\nMayhemme is STARTING♪\n'abort' to abort ♪""")
                    ki.sendText(msg.to,"「 Mayhemme 」\n %i victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/" % len(gs.members))
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    for target in targets:
                        if not target in Bots:
                            try:
                                ki.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"「 Mayhemme 」\nMayhemme is STARTING♪\n'abort' to abort ♪""")
                                ki.sendText(msg.to,"「 Mayhemme 」\n %i victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/" % len(gs.members))
                else:
                    foo = mimic["setkey"]+'mayhemme'
                    key = len(foo)
                    key1 = msg.text[key:]
                    _name = key1.replace("","")
                    gs = ki.getGroup(msg.to)
                    ki.sendText(msg.to,"「 Mayhemme 」\nMayhemme is STARTING♪\n'abort' to abort ♪""")
                    ki.sendText(msg.to,"「 Mayhemme 」\n %i victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/" % len(gs.members))
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    for target in targets:
                        if not target in Bots:
                            try:
                                ki.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"「 Mayhemme 」\nMayhemme is STARTING♪\n'abort' to abort ♪""")
                                ki.sendText(msg.to,"「 Mayhemme 」\n %i victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/" % len(gs.members))
#------------------------------------------------------
            elif msg.text.lower() == mimic["setkey"]+'set' or msg.text.lower() == mimic["setkey"]+' set':
                md = ""
                if mimic["status"] == True: md+="🔑 Mimic:on \n"
                else:md+="🔐 Mimic:off \n"
                if wait["talkban"] == True: md+="🔑 Talkban:on \n"
                else:md+="🔐 Talkban:off \n"
                if msg.to in wait['pname']: md+="🔑 Namelock:on \n"
                else:md+="🔐 Namelock:off \n"
                if wait["timeline"] == True: md+="🔑 Share:on \n"
                else:md+="🔐 Share:off \n"
                if msg.to in nzetWellcome: md+="🔑 Welcomemessage:on \n"
                else:md+="🔐 Welcomemessage:off \n"
                if msg.to in nzetProtection: md+="🔑 Protection:on \n"
                else:md+="🔐 Protection:off \n"
                if msg.to in nzetUrl: md+="🔑 Link Protect:on \n"
                else:md+="🔐 Link Protect:off \n"
                if msg.to in nzetAutoInvite: md+="🔑 Invitation Protect:on \n"
                else:md+="🔐 Invitation Protect:off \n"
                if msg.to in autoCancel: md+="🔑 Cancel Protect:on \n"
                else:md+="🔐 Cancel Protect:off \n"
                if wait["contact"] == True: md+="🔑 Contact:on \n"
                else: md+="🔐 Contact:off \n"
                if wait["autoJoin"] == True: md+="🔑 Join:on \n"
                else: md +="🔐 Join:off \n"
                if wait["autoAdd"] == True: md+="🔑 Autoadd:on \n"
                else: md +="🔐 Autoadd:off \n"
                if wait["autoCancel"]["on"] == True:md+="🔑 Auto cancel:" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "🔐 Auto cancel:off \n"
                if wait["leaveRoom"] == True: md+="🔑 Auto leave:on \n"
                else: md+="🔐 Auto leave:off \n"
                if wait["detectMention"] == True: md+="🔑 Detect mode:on \n"
                else:md+="🔐 Detect mode:off \n"
                if wait["kickMention"] == True: md+="🔑 Mention:on \n"
                else:md+="🔐 Mention:off \n"
                if wait["sambutan"] == True: md+="🔑 Sambutan mode:on \n"
                else:md+="🔐 Sambutan mode:off \n"
               # if settings["simiSimi"] == True: md+="🔑 Simisimi mode:on \n"
                #else:md+="🔐 Simisimi mode:off \n"
                ki.sendText(msg.to,"「✨ PSD Setting ✨」\n\n" + md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                ki.sendMessage(msg)
            elif msg.text.lower() == mimic["setkey"]+'lurking' or msg.text.lower() == mimic["setkey"]+' lurking':
                    print "Getting Read and Unread Data..."
                    if msg.to in wait2['readPoint']:
                        ki.sendText(msg.to, "╔════════════════\n║SIDER IN GROUP\n╠════════════════%s\n║\n╚════════════════" % (wait2['readMember'][msg.to]))
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['ROM'][msg.to] = {}
                        ki.sendText(msg.to, "Mencari Sider Otomatis")
                    else:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['ROM'][msg.to] = {}
                        ki.sendText(msg.to, "Mencari Sider Bosku")
#-----------------------------------------------------------------
            elif msg.text.lower() == mimic["setkey"]+'sider on' or msg.text.lower() == mimic["setkey"]+' sider on':
#       if msg.from_ in Creator:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                ki.sendText(msg.to,"「 sider enable 」\nSider is STARTING♪")
                
            elif msg.text.lower() == mimic["setkey"]+'sider off' or msg.text.lower() == mimic["setkey"]+' sider off':
#       if msg.from_ in Creator:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    ki.sendText(msg.to, "「 sider disable 」\nSider is STARTING♪")
                else:
                    ki.sendText(msg.to, "「 sider disable 」\ncheck status sider enable")
#-----------------------------------------------------------------
            elif msg.text.lower() == mimic["setkey"]+'owner.bot' or msg.text.lower() == mimic["setkey"]+' owner.bot':
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'uebb6976ce05240ce3d9e0216234868f4'}
                ki.sendMessage(msg)
            elif msg.text.lower() == mimic["setkey"]+'gcreator' or msg.text.lower() == mimic["setkey"]+' gcreator':
                try:
                    group = ki.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    ki.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    ki.sendMessage(M)
                    ki.sendText(msg.to,"Karena pencipta tidak ada saat ini, saya menunjukkan pengguna yang pertama kali masuk ke akun yang ada")
            elif msg.text.lower() == mimic["setkey"]+'groups' or msg.text.lower() == mimic["setkey"]+' groups':
                nZetFriends = ki.getGroupIdsJoined()
                ki.sendText(msg.to, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in nZetFriends:
                    nzet = ki.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, nzet.name, len(nzet.members))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(nZetFriends)
                ki.sendText(msg.to, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups1' or msg.text.lower() == mimic["setkey"]+' groups1':
                nZetFriends = ki1.getGroupIdsJoined()
                ki1.sendText(msg.to, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in nZetFriends:
                    nzet = ki1.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, nzet.name, len(nzet.members))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(nZetFriends)
                ki1.sendText(msg.to, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups3' or msg.text.lower() == mimic["setkey"]+' groups3':
                nZetFriends = ki3.getGroupIdsJoined()
                ki3.sendText(msg.to, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in nZetFriends:
                    nzet = ki3.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, nzet.name, len(nzet.members))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(nZetFriends)
                ki3.sendText(msg.to, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups4' or msg.text.lower() == mimic["setkey"]+' groups4':
                nZetFriends = ki4.getGroupIdsJoined()
                ki4.sendText(msg.to, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in nZetFriends:
                    nzet = ki4.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, nzet.name, len(nzet.members))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(nZetFriends)
                ki4.sendText(msg.to, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups5' or msg.text.lower() == mimic["setkey"]+' groups5':
                nZetFriends = ki5.getGroupIdsJoined()
                ki5.sendText(msg.to, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in nZetFriends:
                    nzet = ki5.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, nzet.name, len(nzet.members))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(nZetFriends)
                ki5.sendText(msg.to, msgs)
            elif msg.text.lower() == mimic["setkey"]+'pending' or msg.text.lower() == mimic["setkey"]+' pending':
                nZetFriends = ki.getGroupIdsInvited()
                ki.sendText(msg.to, "Please wait...")
                num=1
                msgs="「User Group Pending」"
                for ids in nZetFriends:
                    nzet = ki.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, nzet.name, len(nzet.members))
                    num=(num+1)
                msgs+="\n「☼ Total %i Pending ☼」 " % len(nZetFriends)
                ki.sendText(msg.to, msgs)
            elif msg.text.lower() == mimic["setkey"]+'mcheck' or msg.text.lower() == mimic["setkey"]+' mcheck':
                nZetFriend = ki.getContacts(wait["blacklist"])
                ki.sendText(msg.to, "Please wait...")
                num=1
                msgs="「User Black List」"
                for ids in nZetFriend:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Black List ☼」 " % len(wait["blacklist"])
                ki.sendText(msg.to, msgs) 
            elif msg.text.lower() == mimic["setkey"]+'clear mimic' or msg.text.lower() == mimic["setkey"]+' clear mimic':
                nZetFriend = ki.getContacts(mimic["target"])
                for ids in nZetFriend:
                    mimic["target"] = {}
                cd = Message()
                cd.to = msg.to
                cd.text = "「☼ Delete All Mimic List ☼」"
                ki.sendMessage(cd)
            elif msg.text.lower() == mimic["setkey"]+'tcheck' or msg.text.lower() == mimic["setkey"]+' tcheck':
                nZetFriend = ki.getContacts(wait["talkblacklist"])
                ki.sendText(msg.to, "Please wait...")
                num=1
                msgs="「User Talkban List」"
                for ids in nZetFriend:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Talkban List ☼」 " % len(wait["talkblacklist"])
                ki.sendText(msg.to, msgs)
            elif msg.text.lower() == mimic["setkey"]+'team' or msg.text.lower() == mimic["setkey"]+' team':
                nZetFriend = ki.getContacts(wait["bots"])
                ki.sendText(msg.to, "Please wait...")
                num=1
                msgs="「User Team List」"
                for ids in nZetFriend:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Team ☼」 " % len(wait["bots"])
                ki.sendText(msg.to, msgs)
            elif msg.text.lower() == mimic["setkey"]+'friend' or msg.text.lower() == mimic["setkey"]+' friend':
                nZetFriend = ki.getAllContactIds()
                ki.sendText(msg.to, "Please wait...")
                kontakNzet = ki.getContacts(nZetFriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakNzet:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」" % len(kontakNzet)
                ki.sendText(msg.to, msgs)
            elif msg.text.lower() == mimic["setkey"]+'group id' or msg.text.lower() == mimic["setkey"]+' group id':
                gid = ki.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "%s: #%s\n" % (ki.getGroup(i).name,i)
                ki.sendText(msg.to,h)
            elif msg.text.lower() == mimic["setkey"]+' gcancel' or msg.text.lower() == mimic["setkey"]+'gcancel':
                gid = ki.getGroupIdsInvited()
                for i in gid:
                    ki.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki.sendMessage(cd)
            elif msg.text.lower() == mimic["setkey"]+'clear ban' or msg.text.lower() == mimic["setkey"]+' clear ban':
                nZetFriend = ki.getContacts(wait["blacklist"])
                for ids in nZetFriend:
                    wait["blacklist"] = {}
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                cd = Message()
                cd.to = msg.to
                cd.text = "「☼ Delete All Black List ☼」"
                ki.sendMessage(cd)
            elif msg.text.lower() == mimic["setkey"]+'clear team' or msg.text.lower() == mimic["setkey"]+' clear team':
                nZetFriend = ki.getContacts(wait["bots"])
                for ids in nZetFriend:
                    wait["bots"] = {}
                    f=codecs.open('bots.json','w','utf-8')
                    json.dump(wait["bots"], f, sort_keys=True, indent=4,ensure_ascii=False)
                cd = Message()
                cd.to = msg.to
                cd.text = "「☼ Delete All Team List ☼」"
                ki.sendMessage(cd)
            elif msg.text.lower().startswith(mimic["setkey"]+'pesan set:') or msg.text.lower().startswith(mimic["setkey"]+' pesan set:'):
                if msg.text.lower().startswith(mimic["setkey"]+' pesan set:'):
                    foo = mimic["setkey"]+' pesan set:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    wait["message"] = key1
                    ki.sendText(msg.to,"「Welcome Message」\nWelcome Message has been set to:\n"+wait["message"])
                else:
                    foo = mimic["setkey"]+'pesan set:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    wait["message"] = key1
                    ki.sendText(msg.to,"「Welcome Message」\nWelcome Message has been set to:\n"+wait["message"])
            elif msg.text.lower().startswith(mimic["setkey"]+'spam add:') or msg.text.lower().startswith(mimic["setkey"]+' spam add:'):
                if msg.text.lower().startswith(mimic["setkey"]+' spam add:'):
                    foo = mimic["setkey"]+' spam add:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    wait["spam"] = key1
                    ki.sendText(msg.to,"「Spam Message」\nSpam Message has been set to:\n"+wait["spam"])
                else:
                    foo = mimic["setkey"]+'spam add:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    wait["spam"] = key1
                    ki.sendText(msg.to,"「Spam Message」\nSpam Message has been set to:\n"+wait["spam"])
            elif msg.text.lower().startswith('setkey set ') or msg.text.lower().startswith(' setkey set '):
                if msg.text.lower().startswith(' setkey set '):
                    foo = ' setkey set '
                    key = len(foo)
                    key1 = msg.text[key:]
                    mimic["setkey"] = key1
                    ki.sendText(msg.to,"「Setkey」\nSetkey has been set to: "+mimic["setkey"].title())
                else:
                    foo = 'setkey set '
                    key = len(foo)
                    key1 = msg.text[key:]
                    mimic["setkey"] = key1
                    ki.sendText(msg.to,"「Setkey」\nSetkey has been set to: "+mimic["setkey"].title())
            elif msg.text.lower() == 'setkey off':
                mimic["setkey"] = ""
                ki.sendText(msg.to,"Key has been set to DISABLED♪")
            elif msg.text.lower() == 'setkey reset':
                mimic["setkey"] = "zet"
                ki.sendText(msg.to,"Key has been set to "+mimic["setkey"].title())
            elif msg.text.lower().startswith(mimic["setkey"]+'spam:') or msg.text.lower().startswith(mimic["setkey"]+' spam:'):
                if msg.text.lower().startswith(mimic["setkey"]+' spam:'):
                    foo = mimic["setkey"]+' spam:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    num = int(key1)
                    for var in range(0,num):
                        ki.sendText(msg.to, wait["spam"].title())
                else:
                    foo = mimic["setkey"]+'spam:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    num = int(key1)
                    for var in range(0,num):
                        ki.sendText(msg.to, wait["spam"].title())
            elif msg.text.lower().startswith(mimic["setkey"]+'welcomemessage pict set ') or msg.text.lower().startswith(mimic["setkey"]+' welcomemessage pict set '):
                if msg.text.lower().startswith(' Welcomemessage pict set:'):
                    foo = mimic["setkey"]+' welcomemessage pict set '
                    key = len(foo)
                    key1 = msg.text[key:]
                    mimic["pap"] = key1
                    ki.sendText(msg.to,"Welcome Message Picture has been set to")
                    ki.sendImageWithURL(msg.to,mimic["pap"])
                else:
                    foo = mimic["setkey"]+'welcomemessage pict set '
                    key = len(foo)
                    key1 = msg.text[key:]
                    mimic["pap"] = key1
                    ki.sendText(msg.to,"Welcome Message Picture has been set to")
                    ki.sendImageWithURL(msg.to,mimic["pap"])
            elif msg.text.lower().startswith(mimic["setkey"]+'clock:') or msg.text.lower().startswith(mimic["setkey"]+' clock:'):
                if msg.text.lower().startswith(mimic["setkey"]+' clock:'):
                    foo = mimic["setkey"]+' clock:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        wait["cName"] = string
                        ki42.sendText(msg.to,"Update Clock Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'clock:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    tulisan = jmlh * (teks+"\n")
                    if len(string.decode('utf-8')) <= 500:
                        wait["cName"] = string
                        ki42.sendText(msg.to,"Update Clock Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'spam ') or msg.text.lower().startswith(mimic["setkey"]+' spam '):
                if msg.text.lower().startswith(mimic["setkey"]+' spam '):
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    foo = mimic["setkey"]+' spam '
                    key = len(foo)
                    key1 = msg.text[key:]
                    teks = key1.replace("" + str(txt[1])+" "+str(jmlh)+ " ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 10000:
                            for x in range(jmlh):
                                ki.sendText(msg.to, teks)
                            else:
                                ki.sendText(msg.to, '')
                    elif txt[1] == "off":
                        if jmlh <= 10000:
                                ki.sendText(msg.to, tulisan)
                        else:
                                ki.sendText(msg.to, '')
                else:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    foo = mimic["setkey"]+'spam '
                    key = len(foo)
                    key1 = msg.text[key:]
                    teks = key1.replace("" + str(txt[1])+" "+str(jmlh)+ " ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 10000:
                            for x in range(jmlh):
                                ki.sendText(msg.to, teks)
                            else:
                                ki.sendText(msg.to, '')
                    elif txt[1] == "off":
                        if jmlh <= 10000:
                                ki.sendText(msg.to, tulisan)
                        else:
                                ki.sendText(msg.to, '')
            elif msg.text.lower() == mimic["setkey"]+'welcomemessage pict' or msg.text.lower() == mimic["setkey"]+' welcomemessage pict':
                ki.sendImageWithURL(msg.to,mimic["pap"])
            elif msg.text.lower() == mimic["setkey"]+'pesan cek' or msg.text.lower() == mimic["setkey"]+' pesan cek':
                    ki.sendText(msg.to, wait["message"])
            elif msg.text.lower() == mimic["setkey"]+'spam cek' or msg.text.lower() == mimic["setkey"]+' spam cek':
                    ki.sendText(msg.to, wait["spam"].title())
            elif msg.text.lower() == mimic["setkey"]+'url' or msg.text.lower() == mimic["setkey"]+' url':
                if msg.toType == 2:
                    g = ki.getGroup(msg.to)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        ki.updateGroup(g)
                else:
                        ki.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text.lower() == mimic["setkey"]+'sambutan on' or msg.text.lower() == mimic["setkey"]+' sambutan on':
                if wait["sambutan"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"「sambutan」\nState: ENABLE♪")
                else:
                    wait["sambutan"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"「sambutan」\nState: ENABLE♪")

            elif msg.text.lower() == mimic["setkey"]+'sambutan off' or msg.text.lower() == mimic["setkey"]+' sambutan off':
                if wait["sambutan"] == False:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"「sambutan」\nState: DISABLE♪")
                else:
                    wait["sambutan"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"「sambutan」\nState: DISABLE♪")
            elif msg.text.lower() == mimic["setkey"]+'simisimi on' or msg.text.lower() == mimic["setkey"]+' simisimi on':
                settings["simiSimi"][msg.to] = True
                ki.sendText(msg.to,"「simisimi」\nState: ENABLE♪")
                
            elif msg.text.lower() == mimic["setkey"]+'simisimi off' or msg.text.lower() == mimic["setkey"]+' simisimi off':
                settings["simiSimi"][msg.to] = False
                ki.sendText(msg.to,"「simisimi」\nState: DISABLE♪")
           
            elif msg.text.lower() == mimic["setkey"]+'respon on' or msg.text.lower() == mimic["setkey"]+' respon on':
                wait["detectMention"] = True
                ki.sendText(msg.to,"「auto respon」\nState: ENABLE♪")
                
            elif msg.text.lower() == mimic["setkey"]+'respon off' or msg.text.lower() == mimic["setkey"]+' respon off':
                wait["detectMention"] = False
                ki.sendText(msg.to,"「auto respon」\nState: DISABLE♪")
            
            elif msg.text.lower() == mimic["setkey"]+'notag on' or msg.text.lower() == mimic["setkey"]+' notag on':
                wait["kickMention"] = True
                ki.sendText(msg.to,"「auto kick tag」\nState: ENABLE♪")
                
            elif msg.text.lower() == mimic["setkey"]+'notag off' or msg.text.lower() == mimic["setkey"]+' notag off':
                wait["kickMention"] = False
                ki.sendText(msg.to,"「auto kick tag」\nState: DISABLE♪")
            elif msg.text.lower() == mimic["setkey"]+'update' or msg.text.lower() == mimic["setkey"]+' update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"༺%H:%M༻")
                    profile = ki.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"Diperbarui")
                else:
                    ki.sendText(msg.to,"Silahkan Aktifkan Jam")
            elif msg.text.lower().startswith(mimic["setkey"]+'nk ') or msg.text.lower().startswith(mimic["setkey"]+' nk ') or msg.text.lower().startswith(mimic["setkey"]+'nk') or msg.text.lower().startswith(mimic["setkey"]+' nk'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                            try:
                                gs = ki.getGroup(msg.to)
                                gs.preventJoinByTicket = False
                                random.choice(P2).updateGroup(gs)
                                invsend = 0
                                Ticket = random.choice(P2).reissueGroupTicket(msg.to)
                                ki18.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ki18.kickoutFromGroup(msg.to,[target])
                                gs.preventJoinByTicket = True
                                ki18.updateGroup(gs)
                                ki18.sendText(gs)
                            except:
                                ki18.sendText(msg.to,"「Kick Mode Siri」\nYou have to mention a user♪")
                                ki18.leaveGroup(msg.to)
                else:
                    ki.sendText(msg.to,"「Kick Mode Siri」\nYou have to mention a user♪")
            elif msg.text.lower() == mimic["setkey"]+'welcome' or msg.text.lower() == mimic["setkey"]+' welcome':
                ginfo = ki.getGroup(msg.to)
                ki.sendImageWithURL(msg.to,mimic["pap"])
                ki.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                ki.sendMessage(msg)
            elif msg.text.lower().startswith(mimic["setkey"]+'gift ') or msg.text.lower().startswith(mimic["setkey"]+' gift ') or msg.text.lower().startswith(mimic["setkey"]+'gift') or msg.text.lower().startswith(mimic["setkey"]+' gift'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            group = ki.getContact(target)
                            ki.sendText(msg.to, group.displayName + " Check Your Gift")
                            msg.contentType = 9
                            msg.contentMetadata={'PRDTYPE': 'STICKER',
                                                 'STKVER': '1',
                                                 'MSGTPL': '5',
                                                 'STKPKGID': '1380280'}
                            msg.to = target
                            msg.text = None
                            ki.sendMessage(msg)
                        except:
                            pass
                else:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDTYPE': 'STICKER',
                                        'STKVER': '1',
                                        'MSGTPL': '5',
                                        'STKPKGID': '1380280'}
                    msg.text = None
                    ki.sendMessage(msg)
#-----------------------------------------------------------
            elif msg.text.lower().startswith(mimic["setkey"]+'kick1 ') or msg.text.lower().startswith(mimic["setkey"]+' kick1 ') or msg.text.lower().startswith(mimic["setkey"]+'kick1') or msg.text.lower().startswith(mimic["setkey"]+' kick1'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki1.kickoutFromGroup(msg.to,[target])
                        except Exception as e:
                            ki1.sendText(msg.to,str(e))
                else:
                    ki1.sendText(msg.to,"「Kick」\nYou need to mention a user♪")
            elif msg.text.lower().startswith(mimic["setkey"]+'kick2 ') or msg.text.lower().startswith(mimic["setkey"]+' kick2 ') or msg.text.lower().startswith(mimic["setkey"]+'kick2') or msg.text.lower().startswith(mimic["setkey"]+' kick2'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki2.kickoutFromGroup(msg.to,[target])
                        except Exception as e:
                            ki2.sendText(msg.to,str(e))
                else:
                    ki2.sendText(msg.to,"「Kick」\nYou need to mention a user♪")
            elif msg.text.lower().startswith(mimic["setkey"]+'kick3 ') or msg.text.lower().startswith(mimic["setkey"]+' kick3 ') or msg.text.lower().startswith(mimic["setkey"]+'kick3') or msg.text.lower().startswith(mimic["setkey"]+' kick3'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki3.kickoutFromGroup(msg.to,[target])
                        except Exception as e:
                            ki3.sendText(msg.to,str(e))
                else:
                    ki3.sendText(msg.to,"「Kick」\nYou need to mention a user♪")
            elif msg.text.lower().startswith(mimic["setkey"]+'kick4 ') or msg.text.lower().startswith(mimic["setkey"]+' kick4 ') or msg.text.lower().startswith(mimic["setkey"]+'kick4') or msg.text.lower().startswith(mimic["setkey"]+' kick4'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki4.kickoutFromGroup(msg.to,[target])
                        except Exception as e:
                            ki4.sendText(msg.to,str(e))
                else:
                    ki4.sendText(msg.to,"「Kick」\nYou need to mention a user♪")
            elif msg.text.lower().startswith(mimic["setkey"]+'kick5 ') or msg.text.lower().startswith(mimic["setkey"]+' kick5 ') or msg.text.lower().startswith(mimic["setkey"]+'kick5') or msg.text.lower().startswith(mimic["setkey"]+' kick5'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki5.kickoutFromGroup(msg.to,[target])
                        except Exception as e:
                            ki5.sendText(msg.to,str(e))
                else:
                    ki5.sendText(msg.to,"「Kick」\nYou need to mention a user♪")
            elif msg.text.lower().startswith(mimic["setkey"]+'makan ') or msg.text.lower().startswith(mimic["setkey"]+' makan ') or msg.text.lower().startswith(mimic["setkey"]+'makan') or msg.text.lower().startswith(mimic["setkey"]+' makan'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            random.choice(P1).kickoutFromGroup(msg.to,[target])
                        except Exception as e:
                            random.choice(P1).sendText(msg.to,str(e))
                else:
                    random.choice(P1).sendText(msg.to,"「makan」\nYou need to mention a user♪")
            elif msg.text.lower().startswith(mimic["setkey"]+'kick ') or msg.text.lower().startswith(mimic["setkey"]+' kick ') or msg.text.lower().startswith(mimic["setkey"]+'kick') or msg.text.lower().startswith(mimic["setkey"]+' kick'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki.kickoutFromGroup(msg.to,[target])
                        except Exception as e:
                            ki.sendText(msg.to,str(e))
                else:
                    ki.sendText(msg.to,"「Kick」\nYou need to mention a user♪")
            elif msg.text.lower() == 'responsename':
                profile = ki1.getProfile()
                text = profile.displayName + ""
                ki1.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName + ""
                ki2.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = profile.displayName + ""
                ki3.sendText(msg.to, text)
                profile = ki4.getProfile()
                text = profile.displayName + ""
                ki4.sendText(msg.to, text)
                profile = ki5.getProfile()
                text = profile.displayName + ""
                ki5.sendText(msg.to, text)
            elif msg.text.lower() == 'ping':
                ki1.sendText(msg.to,"Hooh 􀠁􀆩􏿿\nPSD TEAM BOT") 
                ki2.sendText(msg.to,"Hooh 􀠁􀆩􏿿\nPSD TEAM BOT") 
                ki3.sendText(msg.to,"Hooh 􀠁􀆩􏿿\nPSD TEAM BOT") 
                ki4.sendText(msg.to,"Hooh 􀠁􀆩􏿿\nPSD TEAM BOT") 
                ki5.sendText(msg.to,"Hooh 􀠁􀆩􏿿\nPSD TEAM BOT")
            elif msg.text.lower() == mimic["setkey"]+' miclist' or msg.text.lower() == mimic["setkey"]+'miclist':
             group = ki.getGroup(msg.to)
             nama = [contact.mid for contact in group.members]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                mimictag(msg.to, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                mimictag(msg.to, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                mimictag(msg.to, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                mimictag(msg.to, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                mimictag(msg.to, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                mimictag(msg.to, nm5)
#-------------------------------------------all protect start
            elif 'pro-all ' in msg.text.lower():
                spl = msg.text.lower().replace('pro-all ','')
                if spl == 'on':
                    if msg.to in autoCancel:
                        msgs="Cancel Invitation already on"
                    else:
                        autoCancel.append(msg.to)
                        msgs="Cancel Invitation set to on"
                    ki.sendText(msg.to,"「Cancel Invitation」\n" + msgs)
                elif spl == 'off':
                    if msg.to in autoCancel:
                        autoCancel.remove(msg.to)
                        msgs="Cancel Invitation already off"
                    else:
                        msgs="Cancel Invitation already off"
                    ki.sendText(msg.to,"「Cancel Invitation」\n" + msgs)
                if spl == 'on':
                    if msg.to in nzetProtection:
                        msgs="Protect already on"
                    else:
                        nzetProtection.append(msg.to)
                        msgs="Protect set to on"
                    ki.sendText(msg.to,"「Protect」\n" + msgs)
                elif spl == 'off':
                    if msg.to in nzetProtection:
                        nzetProtection.remove(msg.to)
                        msgs="Protect already off"
                    else:
                        msgs="Protect already off"
                    ki.sendText(msg.to,"「Protect」\n" + msgs)
                if spl == 'on':
                    if msg.to in nzetAutoInvite:
                        msgs="Invitation protect already on"
                    else:
                        nzetAutoInvite.append(msg.to)
                        msgs="Invitation protect set to on"
                    ki.sendText(msg.to,"「Protect Invitation」\n" + msgs)
                elif spl == 'off':
                    if msg.to in nzetAutoInvite:
                        nzetAutoInvite.remove(msg.to)
                        msgs="Invitation protect set to off"
                    else:
                        msgs="Invitation protect already off"
                    ki.sendText(msg.to,"「Protect Invitation」\n" + msgs)
                if spl == 'on':
                    if msg.to in nzetUrl:
                        msgs="Link protect already on"
                    else:
                        nzetUrl.append(msg.to)
                        msgs="Link protect set to on"
                    ki.sendText(msg.to,"「Protect Qr」\n" + msgs)
                elif spl == 'off':
                    if msg.to in nzetUrl:
                        nzetUrl.remove(msg.to)
                        msgs="Link protect set to off"
                    else:
                        msgs="Link protect already off"
                    ki.sendText(msg.to,"「Protect Qr」\n" + msgs)
                if spl == 'on':
                    if msg.to in wait['pname']:
                        msgs="「Name Lock」\nName Lock already ENABLED♪"
                    else:
                        msgs="「Name Lock」\nName Lock set to ENABLED♪"
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = ki.getGroup(msg.to).name
                    ki.sendText(msg.to, msgs)
                elif spl == 'off':
                    if msg.to in wait['pname']:
                        msgs="「Name Lock」\nName Lock set to DISABLED♪"
                        del wait['pname'][msg.to]
                    else:
                        msgs="「Name Lock」\nName Lock already DISABLED♪"
                    ki.sendText(msg.to, msgs)    
#-------------------------------------------all protect done
            elif 'contact ' in msg.text.lower():
                spl = msg.text.lower().replace('contact ','')
                if spl == 'on':
                    if wait['contact'] == True:
                        msgs="contact already on"
                    else:
                        msgs="contact set to on"
                        wait['contact']=True
                    ki.sendText(msg.to, msgs)
                elif spl == 'off':
                    if wait['contact'] == False:
                        msgs="contact already off"
                    else:
                        msgs="contact set to off"
                        wait['contact']=False
                    ki.sendText(msg.to, msgs)
            elif 'cancel ' in msg.text.lower():
                spl = msg.text.lower().replace('cancel ','')
                if spl == 'on':
                    if msg.to in autoCancel:
                        msgs="Cancel Invitation already on"
                    else:
                        autoCancel.append(msg.to)
                        msgs="Cancel Invitation set to on"
                    ki.sendText(msg.to,"「Cancel Invitation」\n" + msgs)
                elif spl == 'off':
                    if msg.to in autoCancel:
                        autoCancel.remove(msg.to)
                        msgs="Cancel Invitation already off"
                    else:
                        msgs="Cancel Invitation already off"
                    ki.sendText(msg.to,"「Cancel Invitation」\n" + msgs)
            elif 'welcomemessage ' in msg.text.lower():
                spl = msg.text.lower().replace('welcomemessage ','')
                if spl == 'on':
                    if msg.to in nzetWellcome:
                        msgs="Welcome Message already on"
                    else:
                        nzetWellcome.append(msg.to)
                        msgs="Welcome Message set to on"
                    ki.sendText(msg.to,"「Welcome Message」\n" + msgs)
                elif spl == 'off':
                    if msg.to in nzetWellcome:
                        nzetWellcome.remove(msg.to)
                        msgs="Welcome Message already off"
                    else:
                        msgs="Welcome Message already off"
                    ki.sendText(msg.to,"「Welcome Message」\n" + msgs)
            elif 'protect ' in msg.text.lower():
                spl = msg.text.lower().replace('protect ','')
                if spl == 'on':
                    if msg.to in nzetProtection:
                        msgs="Protect already on"
                    else:
                        nzetProtection.append(msg.to)
                        msgs="Protect set to on"
                    ki.sendText(msg.to,"「Protect」\n" + msgs)
                elif spl == 'off':
                    if msg.to in nzetProtection:
                        nzetProtection.remove(msg.to)
                        msgs="Protect already off"
                    else:
                        msgs="Protect already off"
                    ki.sendText(msg.to,"「Protect」\n" + msgs)
            elif 'inv ' in msg.text.lower():
                spl = msg.text.lower().replace('inv ','')
                if spl == 'on':
                    if msg.to in nzetAutoInvite:
                        msgs="Invitation protect already on"
                    else:
                        nzetAutoInvite.append(msg.to)
                        msgs="Invitation protect set to on"
                    ki.sendText(msg.to,"「Protect Invitation」\n" + msgs)
                elif spl == 'off':
                    if msg.to in nzetAutoInvite:
                        nzetAutoInvite.remove(msg.to)
                        msgs="Invitation protect set to off"
                    else:
                        msgs="Invitation protect already off"
                    ki.sendText(msg.to,"「Protect Invitation」\n" + msgs)
            elif 'qr ' in msg.text.lower():
                spl = msg.text.lower().replace('qr ','')
                if spl == 'on':
                    if msg.to in nzetUrl:
                        msgs="Link protect already on"
                    else:
                        nzetUrl.append(msg.to)
                        msgs="Link protect set to on"
                    ki.sendText(msg.to,"「Protect Qr」\n" + msgs)
                elif spl == 'off':
                    if msg.to in nzetUrl:
                        nzetUrl.remove(msg.to)
                        msgs="Link protect set to off"
                    else:
                        msgs="Link protect already off"
                    ki.sendText(msg.to,"「Protect Qr」\n" + msgs)
            elif 'jam ' in msg.text.lower():
                spl = msg.text.lower().replace('jam ','')
                if spl == 'on':
                    if wait['clock'] == True:
                        msgs="Jam already on"
                    else:
                        msgs="Jam set to on"
                        wait['clock']=True
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"༺%H:%M༻")
                        profile = ki.getProfile()
                        profile.displayName = wait["cName"] + nowT
                        ki.updateProfile(profile)
                    ki.sendText(msg.to, msgs)
                elif spl == 'off':
                    if wait['clock'] == False:
                        msgs="Jam already off"
                    else:
                        msgs="Jam set to off"
                        wait['clock']=False
                    ki.sendText(msg.to, msgs)
            elif 'talkban ' in msg.text.lower():
                spl = msg.text.lower().replace('talkban ','')
                if spl == 'on':
                    if wait['talkban'] == True:
                        msgs="「Talkban」\nTalkban already Not For chat"
                    else:
                        msgs="「Talkban」\nTalkban set to Not For chat"
                        wait['talkban']=True
                    ki.sendText(msg.to, msgs)
                elif spl == 'off':
                    if wait['talkban'] == False:
                        msgs="「Talkban」\nTalkban already Allow For chat"
                    else:
                        msgs="「Talkban」\nTalkban set to Allow For chat"
                        wait['talkban']=False
                    ki.sendText(msg.to, msgs)
            elif 'leave ' in msg.text.lower():
                spl = msg.text.lower().replace('leave ','')
                if spl == 'on':
                    if wait['leaveRoom'] == True:
                        msgs="「Auto Leave」\nAuto Leave Multichat already ENABLED♪"
                    else:
                        msgs="「Auto Leave」Auto Leave Multichat set to ENABLED♪"
                        wait['leaveRoom']=True
                    ki.sendText(msg.to, msgs)
                elif spl == 'off':
                    if wait['leaveRoom'] == False:
                        msgs="「Auto Leave」Auto Leave Multichat already DISABLED♪"
                    else:
                        msgs="「Auto Leave」Auto Leave Multichat set to DISABLED♪"
                        wait['leaveRoom']=False
                    ki.sendText(msg.to, msgs)
            elif 'share ' in msg.text.lower():
                spl = msg.text.lower().replace('share ','')
                if spl == 'on':
                    if wait['timeline'] == True:
                        msgs="「Share」\nShare already ENABLED♪"
                    else:
                        msgs="「Share」\nShare set to ENABLED♪"
                        wait['timeline']=True
                    ki.sendText(msg.to, msgs)
                elif spl == 'off':
                    if wait['timeline'] == False:
                        msgs="「Share」\nShare already DISABLED♪"
                    else:
                        msgs="「Share」\nShare set to DISABLED♪"
                        wait['timeline']=False
                    ki.sendText(msg.to, msgs)
            elif 'namelock ' in msg.text.lower():
                spl = msg.text.lower().replace('namelock ','')
                if spl == 'on':
                    if msg.to in wait['pname']:
                        msgs="「Name Lock」\nName Lock already ENABLED♪"
                    else:
                        msgs="「Name Lock」\nName Lock set to ENABLED♪"
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = ki.getGroup(msg.to).name
                    ki.sendText(msg.to, msgs)
                elif spl == 'off':
                    if msg.to in wait['pname']:
                        msgs="「Name Lock」\nName Lock set to DISABLED♪"
                        del wait['pname'][msg.to]
                    else:
                        msgs="「Name Lock」\nName Lock already DISABLED♪"
                    ki.sendText(msg.to, msgs)      
            elif msg.text.lower() == mimic["setkey"]+'blcheck' or msg.text.lower() == mimic["setkey"]+' blcheck':
                if wait["blacklist"] == {}:
                    ki.sendText(msg.to,"Nothing in the blacklist")
                else:
                    ki.sendText(msg.to,"Daftar Contact Yang Ke Ban")
                    mc = ""
                    for mi_d in wait["blacklist"]:
						msg.contentType = 13
						msg.contentMetadata = {'mid': mi_d}
						ki.sendMessage(msg)
            elif msg.text.lower() == mimic["setkey"]+'blocklist' or msg.text.lower() == mimic["setkey"]+' blocklist':
                blockedlist = ki.getBlockedContactIds()
                ki.sendText(msg.to, "Please wait...")
                kontak = ki.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                ki.sendText(msg.to, msgs)
            elif msg.text.lower() == mimic["setkey"]+'kill' or msg.text.lower() == mimic["setkey"]+' kill':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Daftar hitam pengguna tidak memiliki")
                        return
                    for jj in matched_list:
                        try:
                            random.choice(P1).kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif msg.text.lower() == mimic["setkey"]+' banlist' or msg.text.lower() == mimic["setkey"]+'banlist':
             group = ki.getGroup(msg.to)
             nama = [contact.mid for contact in group.members]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                bltag(msg.to, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                bltag(msg.to, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                bltag(msg.to, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                bltag(msg.to, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                bltag(msg.to, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                bltag(msg.to, nm5)
            elif msg.text.lower() == mimic["setkey"]+'cancel' or msg.text.lower() == mimic["setkey"]+' cancel':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
            elif msg.text.lower() == mimic["setkey"]+'all' or msg.text.lower() == mimic["setkey"]+' all':
                        G = ki.getGroup(msg.to)
                        ginfo = ki.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = ki.getGroup(msg.to)
                        ginfo = ki.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(P1).updateGroup(G)
                        G.preventJoinByTicket(G)
                        random.choice(P1).updateGroup(G)
                       
#-----------------------------------------------
            elif msg.text.lower() == mimic["setkey"]+'psd5' or msg.text.lower() == mimic["setkey"]+' psd5':
                        G = ki.getGroup(msg.to)
                        ginfo = ki.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = ki.getGroup(msg.to)
                        ginfo = ki.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki1.updateGroup(G)
                        G.preventJoinByTicket(G)
                        ki1.updateGroup(G)
            elif msg.text.lower() == mimic["setkey"]+'bye' or msg.text.lower() == mimic["setkey"]+' bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text.lower() == 'out':
                if msg.toType == 2:
                    ginfo = ki.getGroup(msg.to)
                    try:
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text.lower() == 'k1':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki1mid}
                       try:
                           ki1.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k2':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki2mid}
                       try:
                           ki2.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k3':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki3mid}
                       try:
                           ki3.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k4':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki4mid}
                       try:
                           ki4.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k5':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki5mid}
                       try:
                           ki5.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'myifc':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    ki.sendText(msg.to, botKernel + "\n\n􀬁􀆆􏿿PSD NetStatus􀬁􀆆􏿿")
            elif msg.text.lower() == 'mysystem':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    ki.sendText(msg.to, botKernel + "\n\n􀬁􀆆􏿿PSD MY SYSTEM INFO􀬁􀆆􏿿")
            elif msg.text.lower() == 'mykernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    ki.sendText(msg.to, botKernel + "\n\n􀬁􀆆􏿿PSD MY KERNEL INFO􀬁􀆆􏿿")
            elif msg.text.lower() == 'mycpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    ki.sendText(msg.to, botKernel + "\n\n􀬁􀆆􏿿PSD MY CPU INFO􀬁􀆆􏿿")
            elif msg.text.lower() == 'hore':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846756",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                ki.sendMessage(msg)
            elif msg.text.lower() == 'ok':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846755",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                ki.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "15134150",
                                     "STKPKGID": "1388272",
                                     "STKVER": "1" }
                ki.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "15659375",
                                     "STKPKGID": "1405277",
                                     "STKVER": "2" }
                ki.sendMessage(msg)
            elif msg.text.lower() == 'siap bos':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846757",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                ki.sendMessage(msg)
            elif msg.text.lower() == 'reboot':
                    print "[Command]Like executed"
                    try:
                        ki.sendText(msg.to,"Restart Program")
                        restart_program()
                    except:
                        ki.sendText(msg.to,"Restart Program")
                        restart_program()
                        pass
            elif "Getmid @" in msg.text:
                _name = msg.text.replace("Getmid @","")
                _nametarget = _name.rstrip(' ')
                gs = ki.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        ki.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "sound welcome" in msg.text:
                gs = ki.getGroup(msg.to)
                say = msg.text.replace("sound welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ki.sendAudio(msg.to,"hasil.mp3")
            elif "/apakah " in msg.text:
                apk = msg.text.replace("/apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ki.sendAudio(msg.to,"hasil.mp3") 
            elif "/hari " in msg.text:
                apk = msg.text.replace("/hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ki.sendAudio(msg.to,"hasil.mp3")
            elif "/berapa " in msg.text:
                apk = msg.text.replace("/berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ki.sendAudio(msg.to,"hasil.mp3")
            elif "/berapakah " in msg.text:
                apk = msg.text.replace("/berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ki.sendAudio(msg.to,"hasil.mp3")
            elif "/kapan " in msg.text:
                apk = msg.text.replace("/kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ki.sendAudio(msg.to,"hasil.mp3")
            elif "fancytext: " in msg.text:
                    txt = msg.text.replace("fancytext: ", "")
                    ki.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"
            elif "playstore " in msg.text.lower():
                tob = msg.text.lower().replace("playstore ","")
                ki.sendText(msg.to,"Sedang Mencari...")
                ki.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                ki.sendText(msg.to,"PSD SEACRH LINK G_PLAY")
                
            elif "google: " in msg.text:
                    a = msg.text.replace("google: ","")
                    b = urllib.quote(a)
                    ki.sendText(msg.to,"Sedang Mencari...")
                    ki.sendText(msg.to, "https://www.google.com/" + b)
                    ki.sendText(msg.to,"PSD GOOGLE SEACRH LINK")
            elif "gettoken " in msg.text:
                    a = msg.text.replace("gettoken ","")
                    b = urllib.quote(a)
                    c = ("http://101.255.95.249:6969/" + b)
                    ki.sendText(msg.to,"Sedang Mencari...")
                    ki.sendText(msg.to, "line://au/q/" % (url_or_issue,) + b)
                    ki.sendText(msg.to,"Wait dalam percobaan")
            elif "facebook " in msg.text:
                if msg.from_ in admin:
                    a = msg.text.replace("facebook ","")
                    b = urllib.quote(a)
                    ki.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Proses")
                    ki.sendText(msg.to, "https://www.facebook.com" + b)
                    ki.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Sukses")
            elif msg.text in ["kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                ki.sendText(msg.to, rst)
            elif msg.text in ["Kibaran","kibaran"]:
                msg.contentType = 13
                ki.sendText(msg.to,"💀❌ HEELLOOO❌💀\n💀❌CREW KAMI DATANG LAGI❌💀\n💀❌JANGAN PANIK. SWAT TIME DATANG KE GC KALIAN\nKARENA GC KALIAN SUDAH MASUK DAFTAR TARGET KAMI❌💀\n🔫✔NO BAPER\n🔫✔NO PANIK\n🔫✔NO KOMENT\n\n💀❌JIKA GC KALIAN GAK MAU DI REDAM GAK USAH RUSUH❌💀\n\n💀DAFTAR TARGET GRUP💀\n🔫✔GC RUSUH\n🔫✔GC JUDI\n🔫✔GC BOKEP\n🔫✔GC YANG GAK JELAS\n\n💀❌SALAM JABAT DARI KAMI❌💀\n🔫✔PASUKAN SWAT💀\n🔫✔SWAT TIME DENSUS 888💀")
                msg.contentMetadata = {'mid': 'u5632749448bbb855252abd700df49a4d'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u2719855833ba42f57eb2557af77a212c'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u9c7b5b178d6ffebb91480069ba51589d'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u1305316e98924396d427cedc82e39cb3'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'uccf536945fbcce0b9601d4130c1a01e8'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'uecc081d1c161543b48ea6ace7483df0b'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u6d8843b9fc9821a19290489b953b2a38'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u4d7588fb1fb01ab75a822553632523ea'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'ucdad7f8dadf94d0c2d176c15ab196187'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'ua1e5d96aad5ef23fdba1a8bc575897c4'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'ufad2246926073954fcbba280c4d129f6'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u1df456273cbd363a20472f4e46e67df8'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u64f224d0c079714ed31d876efde9f0e2'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u86059cef530f3dae3eda30851da6ceb1'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u2e1a160d44fdc587eefb8e866f34ecf7'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u8c8bc204b88ec44292b3aedebda987fa'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u18088c3b1a47f1583e7bd5200fd3297e'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u80898be4696557970c081bd6ccf3ac8d'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'ub8145bd7e0a25f9dea14faff5d2aa513'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'ua7620b05a09bcd3af63f5d3cb60e0884'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'ue66bcf8cf99dcd27ab56bbad37c190f9'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u94edd44ef324fe0685933190415bdc80'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'uea80ca7792aecad9afe416ccaa6485ad'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'ufa437f7639f090fd055f3883273fc2ae'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'ua27e820de4e53e1a078e254e263a815a'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u0924164985204dc0518c8cfab635dd75'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'uaca91893ddd29817b7d2e525e3942437'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u67416a17067a1b4306244fa63ed3a30b'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u85e9ec4d87197c325402e9a7df6b52bc'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'ud9c42b12cc9ca8f02fa732bbdc420781'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'uccacdef33144382397bda9a100a23123'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'ub6dad8e072ea87e9666d2968adb81e6a'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'ud99eeaabdf5412dc0c072f69aea3ed4a'}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': 'ufa6f239e444900063b5435fed3b5d7d5'}
                ki.sendMessage(msg)
		ki.sendText(msg.to,"💀❌JANGAN SAKIT HATI MINN LAU GC KALIAN KENA REDAM\nCUKUP SPAM LIKE OA AJA MINN❌💀\n💀❌RENAME MUKA TUKANG KIBAR KALAU GAK RATA❌💀\n❌TANGKIS WOOOOE JANGAN MLONGO KAYAK SAPI LHO❌\n❌PASTI RATA INI BOSS❌")
            elif msg.text.lower() in ["wkwkwk","wkwk","hahaha","haha"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '100',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text.lower() in ["hehehe","hehe"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '10',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text.lower() in ["galau"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '9',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text.lower() in ["you","kau","kamu"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '7',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text.lower() in ["marah","hadeuh","hadeh"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '6',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text.lower() in ["please","pliss","mohon","tolong"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '4',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text.lower() in ["haa","haaa","kaget"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '3',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text.lower() in ["lucu","ngakak","lol"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '110',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text.lower() in ["hmm","hmmm"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '101',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text.lower() in ["tidur"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '1',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text.lower() in ["gemes"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '2',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text.lower() in ["cantik","imut"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '5',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text.lower() in ["nyanyi","lalala"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '11',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text.lower() in ["gugup"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '8',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text.lower() in ["ok","oke","okay","oce","okee","sip","siph"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '13',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text.lower() in ["mantab","mantap","nice","keren"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '14',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text.lower() in ["ngejek"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '15',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text.lower() in ["nangis","sedih"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '16',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text.lower() in ["woi","kampret"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '102',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text.lower() in ["huft"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '104',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text.lower() == 'friend1':
                nZetFriend = ki1.getAllContactIds()
                ki1.sendText(msg.to, "Please wait...")
                kontakNzet = ki1.getContacts(nZetFriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakNzet:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakNzet)
                ki1.sendText(msg.to, msgs)
            elif msg.text.lower() == 'friend2':
                nZetFriend = ki2.getAllContactIds()
                ki2.sendText(msg.to, "Please wait...")
                kontakNzet = ki2.getContacts(nZetFriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakNzet:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakNzet)
                ki2.sendText(msg.to, msgs)
            elif msg.text.lower() == 'friend3':
                nZetFriend = ki3.getAllContactIds()
                ki3.sendText(msg.to, "Please wait...")
                kontakNzet = ki3.getContacts(nZetFriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakNzet:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakNzet)
                ki3.sendText(msg.to, msgs)
            elif msg.text.lower() == 'friend4':
                nZetFriend = ki4.getAllContactIds()
                ki4.sendText(msg.to, "Please wait...")
                kontakNzet = ki4.getContacts(nZetFriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakNzet:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakNzet)
                ki4.sendText(msg.to, msgs)
            elif msg.text.lower() == 'friend5':
                nZetFriend = ki5.getAllContactIds()
                ki5.sendText(msg.to, "Please wait...")
                kontakNzet = ki5.getContacts(nZetFriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakNzet:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakNzet)
                ki5.sendText(msg.to, msgs)
            elif msg.text.lower() == 'o1':
                gid = ki1.getGroupIdsJoined()
                for i in gid:
                    ki1.leaveGroup(i)
            elif msg.text.lower() == 'o2':
                gid = ki2.getGroupIdsJoined()
                for i in gid:
                    ki2.leaveGroup(i)
            elif msg.text.lower() == 'o3':
                gid = ki3.getGroupIdsJoined()
                for i in gid:
                    ki3.leaveGroup(i)
            elif msg.text.lower() == 'o4':
                gid = ki4.getGroupIdsJoined()
                for i in gid:
                    ki4.leaveGroup(i)
            elif msg.text.lower() == 'o5':
                gid = ki5.getGroupIdsJoined()
                for i in gid:
                    ki5.leaveGroup(i)
            elif msg.text.lower() == 'gcancel1':
                gid = ki1.getGroupIdsInvited()
                for i in gid:
                    ki1.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki1.sendMessage(cd)
            elif msg.text.lower() == 'gcancel2':
                gid = ki2.getGroupIdsInvited()
                for i in gid:
                    ki2.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki2.sendMessage(cd)
            elif msg.text.lower() == 'gcancel3':
                gid = ki3.getGroupIdsInvited()
                for i in gid:
                    ki3.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki3.sendMessage(cd)
            elif msg.text.lower() == 'gcancel4':
                gid = ki4.getGroupIdsInvited()
                for i in gid:
                    ki4.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki4.sendMessage(cd)
            elif msg.text.lower() == 'gcancel5':
                gid = ki5.getGroupIdsInvited()
                for i in gid:
                    ki5.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki5.sendMessage(cd)
            elif msg.text.lower() == mimic["setkey"]+' .' or msg.text.lower() == mimic["setkey"]+'.':
             group = ki.getGroup(msg.to)
             nama = [contact.mid for contact in group.members]
             nama.remove(mid)
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 100:
                   cium(msg.to, nama)
             if jml > 100 and jml < 600:
                   for i in range(0, 99):
                       nm1 += [nama[i]]
                   cium(msg.to, nm1)
                   for j in range(100, len(nama)-1):
                       nm2 += [nama[j]]
                   cium(msg.to, nm2)
                   for k in range(200, len(nama)-1):
                       nm3 += [nama[k]]
                   cium(msg.to, nm3)
                   for l in range(300, len(nama)-1):
                        nm4 += [nama[l]]
                   cium(msg.to, nm4)
                   for m in range(400, len(nama)-1):
                       nm5 += [nama[m]]
                   cium(msg.to, nm5)
                   for n in range(500, len(nama)-1):
                       nm6 += [nama[n]]
                   cium(msg.to, nm6)
#----------------------------------------------------------
            elif msg.text.lower() == 'tagall1':
             group = ki1.getGroup(msg.to)
             nama = [contact.mid for contact in group.members]
             nama.remove(ki1mid)
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium1(msg.to, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium1(msg.to, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium1(msg.to, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium1(msg.to, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium1(msg.to, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium1(msg.to, nm5)
            elif msg.text.lower() == 'tagall2':
             group = ki2.getGroup(msg.to)
             nama = [contact.mid for contact in group.members]
             nama.remove(ki2mid)
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium2(msg.to, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium2(msg.to, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium2(msg.to, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium2(msg.to, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium2(msg.to, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium2(msg.to, nm5)
            elif msg.text.lower() == 'tagall3':
             group = ki3.getGroup(msg.to)
             nama = [contact.mid for contact in group.members]
             nama.remove(ki3mid)
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium3(msg.to, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium3(msg.to, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium3(msg.to, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium3(msg.to, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium3(msg.to, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium3(msg.to, nm5)
            elif msg.text.lower() == 'tagall4':
             group = ki4.getGroup(msg.to)
             nama = [contact.mid for contact in group.members]
             nama.remove(ki4mid)
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium4(msg.to, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium4(msg.to, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium4(msg.to, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium4(msg.to, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium4(msg.to, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium4(msg.to, nm5)
            elif msg.text.lower() == 'tagall5':
             group = ki5.getGroup(msg.to)
             nama = [contact.mid for contact in group.members]
             nama.remove(ki5mid)
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium5(msg.to, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium5(msg.to, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium5(msg.to, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium5(msg.to, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium5(msg.to, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium5(msg.to, nm5)
            elif "Say " in msg.text:
				bctxt = msg.text.replace("Say ","")
				ki1.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
            elif msg.text.lower() == '1':
                        G = ki.getGroup(msg.to)
                        ginfo = ki.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = ki.getGroup(msg.to)
                        ginfo = ki.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki1.updateGroup(G)
            elif msg.text.lower() == '2':
                        G = ki.getGroup(msg.to)
                        ginfo = ki.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = ki.getGroup(msg.to)
                        ginfo = ki.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
            elif msg.text.lower() == '3':
                        G = ki.getGroup(msg.to)
                        ginfo = ki.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = ki.getGroup(msg.to)
                        ginfo = ki.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
            elif msg.text.lower() == '4':
                        G = ki.getGroup(msg.to)
                        ginfo = ki.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = ki.getGroup(msg.to)
                        ginfo = ki.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
            elif msg.text.lower() == '5':
                        G = ki.getGroup(msg.to)
                        ginfo = ki.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = ki.getGroup(msg.to)
                        ginfo = ki.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
            elif msg.text.lower() == 'k1 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(msg.to)
                    try:
                        ki1.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text.lower() == 'k2 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text.lower() == 'k3 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text.lower() == 'k4 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(msg.to)
                    try:
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text.lower() == 'k5 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(msg.to)
                    try:
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#----------------------------------------------- 
#-----------------------------------------------
        if op.type == 19:
            try:
                if mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki1.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki1.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki1.updateGroup(G)
                        Ticket = ki1.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki1.updateGroup(G)
                    except:
                        try:
                            G = ki2.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki2.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki2.updateGroup(G)
                            Ticket = ki2.reissueGroupTicket(op.param1)
                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki2.updateGroup(G)
                        except:
                            try:
                                G = ki3.getGroup(op.param1)
                                wait["blacklist"][op.param2] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ki3.kickoutFromGroup(op.param1,[op.param2])
                                G.preventJoinByTicket = False
                                ki3.updateGroup(G)
                                Ticket = ki3.reissueGroupTicket(op.param1)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G.preventJoinByTicket = True
                                ki3.updateGroup(G)
                            except:
                                pass
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki1mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki2.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki2.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        ki1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    except:
                        try:
                            G = ki3.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki3.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki3.updateGroup(G)
                            Ticket = ki3.reissueGroupTicket(op.param1)
                            ki1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki3.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki2mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki3.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki3.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        except:
                            G = ki4.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki4.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki4.updateGroup(G)
                            Ticket = ki4.reissueGroupTicket(op.param1)
                            ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki4.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki3mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki4.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki4.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    except:
                        try:
                            G = ki5.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki5.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki5.reissueGroupTicket(op.param1)
                            ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki5.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki4mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki5.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki5.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    except:
                        try:
                            G = ki6.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki6.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki6.updateGroup(G)
                            Ticket = ki6.reissueGroupTicket(op.param1)
                            ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki6.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki5mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki6.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki6.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                    except:
                        try:
                            G = ki7.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki7.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki7.updateGroup(G)
                            Ticket = ki7.reissueGroupTicket(op.param1)
                            ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki7.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki6mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki7.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki7.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                    except:
                        try:
                            G = ki8.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki8.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki8.updateGroup(G)
                            Ticket = ki8.reissueGroupTicket(op.param1)
                            ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki8.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki7mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki8.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki8.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                    except:
                        try:
                            G = ki9.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki9.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki9.updateGroup(G)
                            Ticket = ki9.reissueGroupTicket(op.param1)
                            ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki9.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki8mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki9.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki9.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                    except:
                        try:
                            G = ki10.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki10.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki10.updateGroup(G)
                            Ticket = ki10.reissueGroupTicket(op.param1)
                            ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki10.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki9mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki10.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki10.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)
                    except:
                        try:
                            G = ki11.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki11.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki11.updateGroup(G)
                            Ticket = ki11.reissueGroupTicket(op.param1)
                            ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki11.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki10mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki11.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki11.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki11.updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki11.updateGroup(G)
                    except:
                        try:
                            G = ki12.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki12.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki12.updateGroup(G)
                            Ticket = ki12.reissueGroupTicket(op.param1)
                            ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki12.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki11mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki12.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki12.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki12.updateGroup(G)
                        Ticket = ki12.reissueGroupTicket(op.param1)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki12.updateGroup(G)
                    except:
                        try:
                            G = ki13.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki13.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki13.updateGroup(G)
                            Ticket = ki13.reissueGroupTicket(op.param1)
                            ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki13.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki12mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki13.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki13.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki13.updateGroup(G)
                        Ticket = ki13.reissueGroupTicket(op.param1)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki13.updateGroup(G)
                    except:
                        try:
                            G = ki14.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki14.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki14.updateGroup(G)
                            Ticket = ki14.reissueGroupTicket(op.param1)
                            ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki14.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki13mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki14.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki14.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki14.updateGroup(G)
                        Ticket = ki14.reissueGroupTicket(op.param1)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki14.updateGroup(G)
                    except:
                        try:
                            G = ki15.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki15.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki15.updateGroup(G)
                            Ticket = ki15.reissueGroupTicket(op.param1)
                            ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki15.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki14mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki15.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki15.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki15.updateGroup(G)
                        Ticket = ki15.reissueGroupTicket(op.param1)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki15.updateGroup(G)
                    except:
                        try:
                            G = ki16.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki16.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki16.updateGroup(G)
                            Ticket = ki16.reissueGroupTicket(op.param1)
                            ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki16.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki15mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki16.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki16.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki16.updateGroup(G)
                        Ticket = ki16.reissueGroupTicket(op.param1)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki16.updateGroup(G)
                    except:
                        try:
                            G = ki17.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki17.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki17.updateGroup(G)
                            Ticket = ki17.reissueGroupTicket(op.param1)
                            ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki17.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki16mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki17.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki17.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki17.updateGroup(G)
                        Ticket = ki17.reissueGroupTicket(op.param1)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki17.updateGroup(G)
                    except:
                        try:
                            G = ki18.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki18.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki18.reissueGroupTicket(op.param1)
                            ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki18.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki17mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki18.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki18.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki18.updateGroup(G)
                        Ticket = ki18.reissueGroupTicket(op.param1)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki18.updateGroup(G)
                    except:
                        try:
                            G = ki20.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki20.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki20.updateGroup(G)
                            Ticket = ki20.reissueGroupTicket(op.param1)
                            ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki20.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki18mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki20.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki20.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki20.updateGroup(G)
                        Ticket = ki20.reissueGroupTicket(op.param1)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki20.updateGroup(G)
                    except:
                        try:
                            G = ki21.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki21.updateGroup(G)
                            Ticket = ki21.reissueGroupTicket(op.param1)
                            ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki21.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki20mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki21.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki21.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki21.updateGroup(G)
                        Ticket = ki21.reissueGroupTicket(op.param1)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki21.updateGroup(G)
                    except:
                        try:
                            G = ki22.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki22.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki22.updateGroup(G)
                            Ticket = ki22.reissueGroupTicket(op.param1)
                            ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki22.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki21mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki22.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki22.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki22.updateGroup(G)
                        Ticket = ki22.reissueGroupTicket(op.param1)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki22.updateGroup(G)
                    except:
                        try:
                            G = ki23.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki23.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki23.reissueGroupTicket(op.param1)
                            ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki23.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki22mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki23.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki23.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki23.updateGroup(G)
                        Ticket = ki23.reissueGroupTicket(op.param1)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki23.updateGroup(G)
                    except:
                        try:
                            G = ki24.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki24.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki24.updateGroup(G)
                            Ticket = ki24.reissueGroupTicket(op.param1)
                            ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki24.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki23mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki24.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki24.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki24.updateGroup(G)
                        Ticket = ki24.reissueGroupTicket(op.param1)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki24.updateGroup(G)
                    except:
                        try:
                            G = ki25.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki25.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki25.updateGroup(G)
                            Ticket = ki25.reissueGroupTicket(op.param1)
                            ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki25.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki24mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki25.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki25.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki25.updateGroup(G)
                        Ticket = ki25.reissueGroupTicket(op.param1)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki25.updateGroup(G)
                    except:
                        try:
                            G = ki26.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki26.updateGroup(G)
                            Ticket = ki26.reissueGroupTicket(op.param1)
                            ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki26.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki25mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki26.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki26.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki26.updateGroup(G)
                        Ticket = ki26.reissueGroupTicket(op.param1)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki26.updateGroup(G)
                    except:
                        try:
                            G = ki27.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki27.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki27.updateGroup(G)
                            Ticket = ki27.reissueGroupTicket(op.param1)
                            ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki27.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki26mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki27.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki27.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki27.updateGroup(G)
                        Ticket = ki27.reissueGroupTicket(op.param1)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki27.updateGroup(G)
                    except:
                        try:
                            G = ki28.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki28.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki28.updateGroup(G)
                            Ticket = ki28.reissueGroupTicket(op.param1)
                            ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki28.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki27mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki28.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki28.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki28.updateGroup(G)
                        Ticket = ki28.reissueGroupTicket(op.param1)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki28.updateGroup(G)
                    except:
                        try:
                            G = ki29.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki29.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki29.updateGroup(G)
                            Ticket = ki29.reissueGroupTicket(op.param1)
                            ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki29.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki28mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki29.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki29.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki29.updateGroup(G)
                        Ticket = ki29.reissueGroupTicket(op.param1)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki29.updateGroup(G)
                    except:
                        try:
                            G = ki30.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki30.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki30.updateGroup(G)
                            Ticket = ki30.reissueGroupTicket(op.param1)
                            ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki30.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki29mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki30.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki30.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki30.updateGroup(G)
                        Ticket = ki30.reissueGroupTicket(op.param1)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki30.updateGroup(G)
                    except:
                        try:
                            G = ki31.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki31.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki31.updateGroup(G)
                            Ticket = ki31.reissueGroupTicket(op.param1)
                            ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki31.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki30mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki31.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki31.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki31.updateGroup(G)
                        Ticket = ki31.reissueGroupTicket(op.param1)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki31.updateGroup(G)
                    except:
                        try:
                            G = ki32.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki32.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki32.updateGroup(G)
                            Ticket = ki32.reissueGroupTicket(op.param1)
                            ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki32.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki31mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki32.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki32.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki32.updateGroup(G)
                        Ticket = ki32.reissueGroupTicket(op.param1)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki32.updateGroup(G)
                    except:
                        try:
                            G = ki33.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki33.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki33.reissueGroupTicket(op.param1)
                            ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki33.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki32mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki33.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki33.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki33.updateGroup(G)
                        Ticket = ki33.reissueGroupTicket(op.param1)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki33.updateGroup(G)
                    except:
                        try:
                            G = ki34.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki34.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki34.updateGroup(G)
                            Ticket = ki34.reissueGroupTicket(op.param1)
                            ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki34.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki33mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki34.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki34.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki34.updateGroup(G)
                        Ticket = ki34.reissueGroupTicket(op.param1)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki34.updateGroup(G)
                    except:
                        try:
                            G = ki35.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki35.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki35.updateGroup(G)
                            Ticket = ki35.reissueGroupTicket(op.param1)
                            ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki35.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki34mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki35.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki35.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki35.updateGroup(G)
                        Ticket = ki35.reissueGroupTicket(op.param1)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki35.updateGroup(G)
                    except:
                        try:
                            G = ki36.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki36.updateGroup(G)
                            Ticket = ki36.reissueGroupTicket(op.param1)
                            ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki36.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki35mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki36.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki36.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki36.updateGroup(G)
                        Ticket = ki36.reissueGroupTicket(op.param1)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki36.updateGroup(G)
                    except:
                        try:
                            G = ki37.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki37.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki37.updateGroup(G)
                            Ticket = ki37.reissueGroupTicket(op.param1)
                            ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki37.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki36mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki37.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki37.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki37.updateGroup(G)
                        Ticket = ki37.reissueGroupTicket(op.param1)
                        ki36.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki37.updateGroup(G)
                    except:
                        try:
                            G = ki38.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki38.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki38.updateGroup(G)
                            Ticket = ki38.reissueGroupTicket(op.param1)
                            ki36.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki38.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki36.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki37mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki38.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki38.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki38.updateGroup(G)
                        Ticket = ki38.reissueGroupTicket(op.param1)
                        ki37.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki38.updateGroup(G)
                    except:
                        try:
                            G = ki39.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki39.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki39.updateGroup(G)
                            Ticket = ki39.reissueGroupTicket(op.param1)
                            ki37.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki39.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki37.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki38mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki39.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki39.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki30.updateGroup(G)
                        Ticket = ki30.reissueGroupTicket(op.param1)
                        ki39.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki30.updateGroup(G)
                    except:
                        try:
                            G = ki40.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki40.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki40.updateGroup(G)
                            Ticket = ki40.reissueGroupTicket(op.param1)
                            ki38.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki40.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki38.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki39mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki40.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki40.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki40.updateGroup(G)
                        Ticket = ki40.reissueGroupTicket(op.param1)
                        ki39.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki40.updateGroup(G)
                    except:
                        try:
                            G = ki41.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki41.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki41.updateGroup(G)
                            Ticket = ki41.reissueGroupTicket(op.param1)
                            ki39.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki41.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki39.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki40mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki41.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki41.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki41.updateGroup(G)
                        Ticket = ki41.reissueGroupTicket(op.param1)
                        ki40.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki41.updateGroup(G)
                    except:
                        try:
                            G = ki42.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki42.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki42.updateGroup(G)
                            Ticket = ki42.reissueGroupTicket(op.param1)
                            ki40.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki42.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki40.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki41mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki42.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki42.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki42.updateGroup(G)
                        Ticket = ki42.reissueGroupTicket(op.param1)
                        ki41.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki42.updateGroup(G)
                    except:
                        try:
                            G = ki1.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki1.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki1.updateGroup(G)
                            Ticket = ki1.reissueGroupTicket(op.param1)
                            ki41.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki1.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki41.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki42mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki.kickoutFromGroup(op.param1,[op.param2])						
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        ki42.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    except:
                        try:
                            G = ki1.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki1.kickoutFromGroup(op.param1,[op.param2])						
                            G.preventJoinByTicket = False
                            ki1.updateGroup(G)
                            Ticket = ki1.reissueGroupTicket(op.param1)
                            ki42.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventJoinByTicket = True
                            ki1.updateGroup(G)
                        except:
                            pass
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if Bots in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            wait["blacklist"][op.param2] = True
                        except:
                            pass


            except:
                pass
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if op.param1 in nzetProtection:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(P1).kickoutFromGroup(op.param1,[op.param2])
			G = ki.getGroup(op.param1)
			G.preventJoinByTicket = True
			random.choice(P1).updateGroup(G)
		   except:
			try:
			    random.choice(P2).kickoutFromGroup(op.param1,[op.param2])
			    G = ki.getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(P2).updateGroup(G)
			except:
			    ki.kickoutFromGroup(op.param1,[op.param2])
			    G = ki.getGroup(op.param1)
			    G.preventJoinByTicket = True
			    ki.updateGroup(G)
			    pass
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if op.param1 in nzetWellcome:
		if op.param2 not in Bots:
		   try:
		    ginfo = ki.getGroup(op.param1)
		    random.choice(P1).sendImageWithURL(op.param1,mimic["pap"])
		    random.choice(P1).sendText(op.param1,wait['message'].title())
		    random.choice(P1).sendText(op.param1,"Group Creator " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
		    msg = Message()
		    msg.to = op.param1
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': ginfo.creator.mid}
		    random.choice(P1).sendMessage(msg)
		   except:
			try:
			    ginfo = ki.getGroup(op.param1)
			    random.choice(P2).sendImageWithURL(op.param1,mimic["pap"])
			    random.choice(P2).sendText(op.param1,wait['message'].title())
			    random.choice(P2).sendText(op.param1,"Group Creator " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
			    msg = Message()
			    msg.to = op.param1
			    msg.contentType = 13
			    msg.contentMetadata = {'mid': ginfo.creator.mid}
			    random.choice(P2).sendMessage(msg)
			except:
			    ginfo = ki.getGroup(op.param1)
			    random.choice(P3).sendImageWithURL(op.param1,mimic["pap"])
			    random.choice(P3).sendText(op.param1,wait['message'].title())
			    random.choice(P3).sendText(op.param1,"Group Creator " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
			    msg = Message()
			    msg.to = op.param1
			    msg.contentType = 13
			    msg.contentMetadata = {'mid': ginfo.creator.mid}
			    random.choice(P3).sendMessage(msg)
			    pass
	    else:
		pass
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif op.param1 in nzetUrl:
		   try:
		    wait ["blacklist"][op.param2] = True
		    f=codecs.open('st2__b.json','w','utf-8')
		    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    random.choice(P2).updateGroup(G)
		    random.choice(P2).kickoutFromGroup(op.param1,[op.param2])
		   except:
		    wait ["blacklist"][op.param2] = True
		    f=codecs.open('st2__b.json','w','utf-8')
		    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(P1).kickoutFromGroup(op.param1,[op.param2])
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif op.param1 in wait['pname']:
		   try:
		    wait["blacklist"][op.param2] = True
		    f=codecs.open('st2__b.json','w','utf-8')
		    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
		    G = ki.getGroup(op.param1)
		    G.name = wait['pro_name'][op.param1]
		    random.choice(P1).updateGroup(G)
		   except:
		    wait["blacklist"][op.param2] = True
		    f=codecs.open('st2__b.json','w','utf-8')
		    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
		    G = ki.getGroup(op.param1)
		    G.name = wait['pro_name'][op.param1]
		    ki.updateGroup(G)
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif op.param1 in nzetProtection:
		    wait ["blacklist"][op.param2] = True
		    random.choice(P1).kickoutFromGroup(op.param1,[op.param2])
		else:
		    ki.sendText(op.param1,"")
	    else:
		ki.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif op.param1 in nzetAutoInvite:
		    wait ["blacklist"][op.param2] = True
		    f=codecs.open('st2__b.json','w','utf-8')
		    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
		    ki.cancelGroupInvitation(op.param1,[op.param3])
		    random.choice(P1).kickoutFromGroup(op.param1,[op.param2])
            if op.param2 not in Bots:
       	        if op.param2 in Bots:
       	           pass
                elif op.param1 in autoCancel:
                   ki.cancelGroupInvitation(op.param1,[contact.mid for contact in ki.getGroup(op.param1).invitee])
        if op.type == 5:
            if wait["autoAdd"] == True:
                ki.findAndAddContactsByMid(op.param1)
                if (wait["autoaddpesan"] in [""," ","\n",None]):
                    pass
                else:
                    ki.sendText(op.param1,str(wait["autoaddpesan"].title()))
            else:
                if (wait["autoaddpesan"] in [""," ","\n",None]):
                    pass
                else:
                    ki.sendText(op.param1,str(wait["autoaddpesan"].title()))
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = ki.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n╠・" + Name
                else:
                    ki.sendText
            except:
                pass
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                ki.sendText(msg.to, "" + data['result']['response'].encode('utf-8'))
                                
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = ki.getContact(msg.from_)
                     cName = contact.displayName
                     image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                     balas = ["Dont Tag Me!! Im Busy",cName + " Ngapain Ngetag?",cName + "  Yg Tag-Tag! Kalo Penting Langsung Pc Aja","-_-","owner.bot",".","me","agus lagi off", cName + " Kenapa Tag saya?","SPAM PC aja " + cName, " aku lagi sibuk pc oke " + cName, " Kamu siapa " + cName + "?", " Ada Perlu apa " + cName + "?","Tenggelamkan tuh yang suka tag pake BOT","Tersummon -_-","Pc aja kalo mau nikung mah😀😏"," dont tag me"," Koe ngtag ae spam tau"," Ngtag gw bayar siah"," owner.bot","owner.bot"]
                     ret_ = "" + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in admin:
                                  ki.sendText(msg.to,ret_)
                                  ki.sendImageWithURL(msg.to,image)
                                  break
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = ki.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag Me!! Im Busy",cName + " Ngapain Ngetag?",cName + " Yg Tag-Tag! Kalo Penting Langsung Pc Aja","-_-","team psd lagi off", cName + " Kenapa Tag saya?","SPAM PC aja " + cName, "Jangan Suka Tag gua " + cName, "Kamu siapa " + cName + "?", "Ada Perlu apa " + cName + "?","Tenggelamkan tuh yang suka tag pake BOT","Tersummon -_-"]
                     ret_ = "[Auto Respond] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in admin:
                                  ki.sendText(msg.to,ret_)
                                  ki.kickoutFromGroup(msg.to,[msg.from_])
                                  break
        if op.type == 17:
          if wait["sambutan"] == True:
            if op.param2 in admsa:
                return
            ginfo = ki.getGroup(op.param1)
            contact = ki.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            ki.sendText(op.param1,"Hallo " + ki.getContact(op.param2).displayName + "\nWelcome To ☞ " + str(ginfo.name) + " ☜")
            ki.sendImageWithURL(op.param1,image)
            print "MEMBER JOIN TO GROUP"
        if op.type == 15:
          if wait["sambutan"] == True:
            if op.param2 in admsa:
                return
            ki.sendText(op.param1,"Nah left baper kek nya " + ki.getContact(op.param2).displayName +  "\ngih yang jauh sonoh😎. . . (︵‵。)")
            print "MEMBER HAS LEFT THE GROUP"
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = ki.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        ki.sendText(op.param1, "「 psd check 」\n" + "☞ " + nick[0] + " ☜" + "\n「 sider enable 」\nkebanyakan ngintip nah")
                                    else:
                                        ki.sendText(op.param1, "「 psd check 」\n" + "☞ " + nick[1] + " ☜" + "\n「 sider enable 」\ncyduk yg cctv")
                                else:
                                    ki.sendText(op.param1, "「 psd check 」\n" + "☞ " + Name + " ☜" + "\n「 sider enable 」\nkaka ngintip yah")
                                    cium(op.param1,[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass                                                          
#------------------------------------------------------------------------------------
        if op.type == 59:
            pass


    except Exception as error:
        print error

def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"༺%H:%M༻")
                profile = ki.getProfile()
                profile.displayName = wait["cName"] + nowT
                ki.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def mimictag(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    matched_list = []
    for tag in mimic["target"]:
        matched_list+=filter(lambda str: str == tag, nm)
    cocoa = ""
    for mm in matched_list:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.displayName
    msg = Message()
    msg.to = to
    msg.text = "「Mention Mimic」 \n"+bb + "    「 Total: " + str(len(matched_list)) +  " Mimic List 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki.sendMessage(msg)
    except Exception as error:
       print error

def bltag(to, nama):
    aa = ""
    bb = ""
    strt = int(22)
    akh = int(22)
    nm = nama
    matched_list = []
    for tag in wait["blacklist"]:
        matched_list+=filter(lambda str: str == tag, nm)
    cocoa = ""
    for mm in matched_list:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.displayName
    msg = Message()
    msg.to = to
    msg.text = "「Mention Blacklist」\n"+bb + "    「 Total: " + str(len(matched_list)) +  " Blacklist 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki.sendMessage(msg)
    except Exception as error:
       print error

def cium(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "╠ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.displayName
    msg = Message()
    msg.to = to
    msg.text = "╔═══════════════\n"+bb + "╠════════════════\n║    Total:" + str(len(nm)) +  " Mention  \n╚════════════════"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki.sendMessage(msg)
    except Exception as error:
       print error

def cium1(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "╠ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki1.getProfile()
    text = profile.displayName
    msg = Message()
    msg.to = to
    msg.from_ = profile.mid
    msg.text = "╔═══════════════\n"+bb + "╠════════════════\n║    Total:" + str(len(nm)) +  " Mention  \n╚════════════════"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki1.sendMessage(msg)
    except Exception as error:
       print error

def cium2(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "╠ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki2.getProfile()
    text = profile.displayName
    msg = Message()
    msg.to = to
    msg.from_ = profile.mid
    msg.text = "╔═══════════════\n"+bb + "╠════════════════\n║    Total:" + str(len(nm)) +  " Mention  \n╚════════════════"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki2.sendMessage(msg)
    except Exception as error:
       print error

def cium3(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "╠ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki3.getProfile()
    text = profile.displayName
    msg = Message()
    msg.to = to
    msg.from_ = profile.mid
    msg.text = "╔═══════════════\n"+bb + "╠════════════════\n║    Total:" + str(len(nm)) +  " Mention  \n╚════════════════"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki3.sendMessage(msg)
    except Exception as error:
       print error

def cium4(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "╠ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki4.getProfile()
    text = profile.displayName
    msg = Message()
    msg.to = to
    msg.from_ = profile.mid
    msg.text = "╔═══════════════\n"+bb + "╠════════════════\n║    Total:" + str(len(nm)) +  " Mention  \n╚════════════════"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki4.sendMessage(msg)
    except Exception as error:
       print error

def cium5(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "╠ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki5.getProfile()
    text = profile.displayName
    msg = Message()
    msg.to = to
    msg.from_ = profile.mid
    msg.text = "╔═══════════════\n"+bb + "╠════════════════\n║    Total:" + str(len(nm)) +  " Mention  \n╚════════════════"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki5.sendMessage(msg)
    except Exception as error:
       print error

while True:
    try:
        Ops = ki.fetchOps(ki.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(ki.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            ki.Poll.rev = max(ki.Poll.rev, Op.revision)
            bot(Op)
