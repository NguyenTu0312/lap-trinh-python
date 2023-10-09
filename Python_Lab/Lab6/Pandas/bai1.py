import pandas as pd
df = pd.read_csv("D:\PythonProject\Lab6\Pandas\Automobile_data.csv")

print(df)

# xuat 6 dong dau tien
print(df.head(6))

# xuat 7 don cuoi dung

print(df.tail(7))

# xuat ra man hinh ten cong ti co xe o to dat nhat
# df = df [['company','price']][df.price==df['price'].max()]
# print(df)
# xuat thog tin chi tiet cua tat ca cac xe thuoc hang toyota
car_Manufactures = df.groupby('company')
toyoyaDf = car_Manufactures.get_group("toyota")
print(toyoyaDf)

#Đếm số xe của từng hãng

#Hãy hiển thị giá xe cao nhất của mỗi hãng xe như sau


#Hiển thị giá xe trung bình của mỗi hãng xe