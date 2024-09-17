def print_order(orders):
    for order in orders:
        name, item, quantity = order
        print(f"{name} ordered {quantity} {item}(s)")




def main():
    orders = [("Alice", "laptop", 1), ("Bob", "camera", 2)]
    print_order(orders)

if __name__ == "__main__":
    main()

