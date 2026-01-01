from telethon import TelegramClient, events, Button
from openpyxl import Workbook, load_workbook
from khayyam import JalaliDatetime
import asyncio
import os

# importing data from env
with open("./env/api_id.txt", "r", encoding="utf-8-sig") as api_id_file:
    API_ID = int(api_id_file.read().strip()) # get api id

with open("./env/api_hash.txt", "r") as api_hash_file:
    API_HASH = api_hash_file.read().strip() # get api hash

with open("./env/token.txt", "r") as token_file:
    TOKEN = token_file.read().strip() # get bot token

with open("./env/admin.txt", "r", encoding="utf-8-sig") as admin_chat_id:
    ADMINS = admin_chat_id.read().strip().split(",") # get admin id

# load excel file in set dir
user_data = set() # chat ids set var
FILE = "./data/users.xlsx"

# create excel file if not created before
if not os.path.exists(FILE) :
    wb = Workbook()
    ws = wb.active
    ws.title = "users_data"
    # write titels in file
    ws.append([
        "chat_id",
        "user_name",
        "first_name",
        "last_name"
        
    ])
    wb.save(FILE)
    wb.close()


# return date time
def date_ret():
    now = JalaliDatetime.now()
    time = now.strftime("%Y/%m/%d - %H:%M:%S")
    return time


# get chat id from excel file into set var
wb =  load_workbook(FILE)
ws = wb.active
for i in ws.iter_rows(min_row= 2, values_only= True):
    user_data.add(i[0])

print("loaded users chat ids")

# check data in excel and if not exist add id to file and set 
def add_data(set_var, file_dir, dict):
    if dict["chat_id"] not in set_var:
        wb = load_workbook(file_dir)
        ws = wb.active
        # writ to file
        ws.append([
            dict["chat_id"],
            dict["user_name"],
            dict["first_name"],
            dict["last_name"]
        ])
        
        set_var.add(dict["chat_id"])
        wb.save(file_dir)
        wb.close()

# creating app
client = TelegramClient(
    "./data/sepehr_bot",
    api_id= API_ID,
    api_hash= API_HASH
)

# main func
async def main(token, app, admin_id, date):
    # start app
    await app.start(bot_token= token)
    
    # send start data to admin
    for i in admin_id:
        await app.send_message(int(i), f"bot started in {date} succses")
    
    # keeping run the bot
    await app.run_until_disconnected()
    

# start message
@client.on(events.NewMessage(pattern= r"/start"))
async def start(event):
    sender = await event.get_sender()
    data ={
        "chat_id" : event.chat_id,
        "user_name" : sender.username,
        "first_name" : sender.first_name,
        "last_name" : sender.last_name
    }
    # use add data func to write to excel file
    add_data(user_data, FILE, data)
    print(f"start request from : {data['chat_id']}")
    
    await client.send_message(entity= event.chat_id, message= f"سلام {data['first_name']} عزیز، \n به ربات خدمات کامپیوتری سپهر خوش آمدید \n برای مشاهده خدمات از دستور /services استفاده کنید.")

# admin panel
@ client.on(events.NewMessage(pattern=r"/admin"))
async def adminPanel(event):
    # set buttom
    butt = client.build_reply_markup([
        Button.inline("ارسال پیام", data="send_to_all")
    ])
    if str(event.chat_id) in ADMINS:
        print(f"Confirmed admin login with chat ID: {event.chat_id} detected")
        sender = await event.get_sender()
        # set text
        text = f"""
        سلام مدیر عزیز ({sender.first_name})
        به پنل مدیریت ربات خوش آمدید

        📢 برای ارسال پیام به همه کاربران، از گزینه «ارسال پیام» استفاده کنید.
        """
        await client.send_message(entity= event.chat_id, message= text, buttons= butt)
    else:
        print(f"An unverified request with chat ID: {event.chat_id} was detected to log in to the admin panel")


# send servises
@client.on(events.NewMessage(pattern= r"/services"))
async def services(event):
    print(f"services reqest from : {event.chat_id}")
    
    # set butons
    butt = client.build_reply_markup([
        Button.inline("اخبار", data="news"),
        Button.url("اینستاگرام", "https://www.instagram.com/sepehr_._electronic/"),
        Button.url("ایرانخودرو", "https://ikcosales.ir/"),
        Button.inline("پرسش", data="ask")
    ])
    
    # set text for view
    text = """
    📌 سرویس‌های ربات شامل موارد زیر است:

    📰 برای مشاهده اخبار کافی‌نت، گزینه «اخبار» را انتخاب کنید.

    🚗 برای ورود به سایت اولویت‌بندی محصولات ایران‌خودرو، گزینه «ایران‌خودرو» را انتخاب کنید.

    ❓ برای طرح سؤال و ارتباط مستقیم با شعبه حضوری، گزینه «پرسش» را انتخاب کنید.

    📷 برای انتقال به صفحه اینستاگرام سپهر الکترونیک، از گزینه «اینستاگرام» استفاده کنید.
    """

    # send message
    await client.send_message(entity=event.chat_id, message=text, buttons=butt)
 
 
# send message to all 
@client.on(events.CallbackQuery(data="send_to_all"))
async def sendToAll(event):
    if str(event.chat_id) in ADMINS:
        # print log and get response
        print(f"admin {event.chat_id} want to send to all a message")
        async with client.conversation(event.chat_id) as conv:
            await conv.send_message("متن ارسالی خود را وارد کنید: ")
            response = await conv.get_response()
            # send message to all ids in user_data set var
            for ids in user_data:
                await client.send_message(entity=ids, message=response)
    
 
if __name__ == "__main__":
    asyncio.run(main(TOKEN, client, ADMINS, date_ret()))