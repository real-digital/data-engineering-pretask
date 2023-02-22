def maximum_value(orders, maximum_load):
    """Find the best combination of items based on their value, given a list of orders and a maximum load.

    Args:
        orders (list): A list of dictionaries representing orders. Each order has a weight and a value.
        maximum_load (int): The maximum weight the cargo robot can carry.

    Returns:
        int: The maximum value that can be achieved without exceeding the maximum load.
    """
    # Sort the orders by value in descending order
    orders = sorted(orders, key=lambda x: x['value'], reverse=True)

    # Initialize the total value and total weight
    total_value = 0
    total_weight = 0

    # Iterate over the sorted orders
    for order in orders:
        # If adding the current order would not exceed the maximum load
        if total_weight + order['weight'] <= maximum_load:
            # Add the current order's value and weight to the total value and weight
            total_value += order['value']
            total_weight += order['weight']

    # Return the total value
    return total_value
