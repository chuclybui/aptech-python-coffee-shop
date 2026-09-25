import datetime

class CoffeeShop:
    def __init__(self, name):
      self.name = name
      
      self.menu = {}
      self.orders = []
      self.vip_customers = set()
      
    def add_to_menu(self, item, price):
      self.menu[item] = price
      print(f"Đã thêm/cập nhật món '{item}' với giá {price:,.0f} VNĐ.")
    
    def add_vip(self, phone_number):
      self.vip_customers.add(phone_number)
      print(f"Đã đăng ký {phone_number} thành khách hàng VIP.")
      
    def place_order(self, phone_number, items_list):
      valid_items = []
      total = 0
      for item in items_list:
        if item in self.menu:
          valid_items.append(item)
          total+=self.menu[item]
        else:
          print(f"Món '{item}' không tồn tại trong menu")
      if len(valid_items) == 0:
          print("Không có món hợp lệ để đặt hàng.")
          return
      if phone_number in self.vip_customers:
         discount = total * 0.10
         total-=discount
         print("Khách hàng VIP được giảm 10%.")
      current_time = datetime.datetime.now()
      
      order = {
        "phone": phone_number,
        "items": valid_items,
        "total": total,
        "time": current_time
      }
      
      self.orders.append(order)
      print("Đặt hàng thành công!")
      print(f"Tổng tiền: {total:,.0f} VNĐ")
      
    def get_unique_items_sold(self):
      unique_items = set()
      # for order in self.orders:
      #    for item in order["items"]:
      #      unique_items.add(item)
      # return unique_items
      for items in self.orders:
        unique_items.update(items["items"])
        
      return unique_items
           