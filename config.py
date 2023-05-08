import motor.motor_asyncio

MONGODB_URL = "mongodb+srv://admin:677100oo@melody-mania.jyocpnq.mongodb.net/?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

#connect to database name
database = client['melody-mania']