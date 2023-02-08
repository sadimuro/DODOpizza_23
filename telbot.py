from aiogram import Bot, Dispatcher, types, executor
import config
import sqlite3

bot = Bot(token = config.token)
dp = Dispatcher(bot)

connect = sqlite3.connect("admin.db")
cursor = connect.cursor()
connect.execute("""CREATE TABLE IF NOT EXISTS order_info(
    name VARCHAR(200),
    surname VARCHAR(200),
    number INTEGER,
    address VARCHAR(200),
    food VARCHAR(200)
    );
    """)

connect.commit()


@dp.message_handler(commands= ['start'])
async def on_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text='Заказать'),
        types.KeyboardButton(text='Меню'),
        types.KeyboardButton(text='Админ')
        )
    


    cursor = connect.cursor()
    cursor.execute(f"SELECT info FROM order_info WHERE info = {'name', 'surname','number', 'address', 'food'};")
    res = cursor.fetchall()
    if res == []:
        cursor.execute(f"""INSERT INTO order_info VALUES ('{message.name}', 
                        '{message.surname}', '{message.number}', 
                        {message.address}, {message.food})""")
    connect.commit()
        
@dp.message_handler(text='Заказать')
async def order_info(message: types.Message):
    await message.answer("Перед заказом вы должны заполнить некоторые информации ")
    
    
    
@dp.message_handler(text='Меню')
async def frontend(message: types.Message):
    await message.answer(
        text= "InlineKeyboards bolush kerek"
    )
    
@dp.message_handler(text='Админ')
async def uxui(message: types.Message):
    await message.answer(
        text= "baza dannih koro alat turgan keyboard jasash kerek"
    )
    
  
   
executor.start_polling(dp)