from coffee_shop import CoffeeShop

shop = CoffeeShop("The Python Roastery")
while True:
    print("\n===================================")
    print(f"CHÀO MỪNG ĐẾN {shop.name.upper()}")
    print("===================================")
    print("1. Xem menu đồ uống")
    print("2. Thêm đồ uống mới vào menu")
    print("3. Đăng ký khách hàng VIP")
    print("4. Đặt hàng")
    print("5. Thống kê các món đã bán")
    print("6. Thoát chương trình")
    print("===================================")

    choice = input("Vui lòng chọn chức năng (1-6): ").strip()
    # ========================
    # 1.xem menu
    # ========================
    if choice =="1":
      print("\n---MENU ĐỒ UỐNG---")
      
      if len(shop.menu) == 0:
        print("Menu hiện đang trống")
      else:
        for item, price in shop.menu.items():
          print(f"-{item} : {price:,.0f} VNĐ")
    # ========================
    #2. Thêm món
    # ========================
    elif choice =="2":
      item = input("Nhập tên món: ").strip()
      
      try:
        price=float(input("Nhập giá món: "))
        
        if price <= 0:
          print("Giá tiền phải lớn hơn 0")
        else:
          shop.add_to_menu(item, price)
      except ValueError:
        print("Giá tiền không hợp lệ")
    # ========================
    #3. Đăng ký vip
    # ========================
    elif choice =="3":
      phone_number = input("Nhập số điện thoại: ").strip()
      
      shop.add_vip(phone_number)
    # ========================
    #4. Đặt hàng
    # ========================
    elif choice == 4:
      phone_number = input("Nhập số điện thoại: ").strip()
      
      items_input = input(
        "Nhập các món muốn đặt, cách nhau bới dấu phẩy: "
      )
      items_list = [
        item.trip()
        for item in items_input.split(",")
        if item.strip()
      ]
      shop.place_order(phone_number, items_list)
    # ========================
    #5. Thống kê món ăn
    # ========================
    elif choice == 5:
      solid_items = shop.get_unique_items_sold()
      print("\n--- CÁC MÓN ĐÃ BÁN ---")
      
      if len(solid_items) == 0:
         print("Chưa có món nào được bán.")
      else:
        print(solid_items)
        
    # ========================
    # 6. Thoát
    # ========================
    elif choice == 6:
        print("Cảm ơn bạn đã sử dụng chương trình!")
        print("Hẹn gặp lại!")
        break
    # ========================
    # Nhập sai lựa chọn
    # ========================
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 6.")