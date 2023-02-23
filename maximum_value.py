def maximum_value(orders, maximum_load):
    """Find the best combination of items based on their value, given a list of orders and a maximum load.

    Args:
        orders (list): A list of dictionaries representing orders. Each order has a weight and a value.
        maximum_load (int): The maximum weight the cargo robot can carry.

    Returns:
        int: The maximum value that can be achieved without exceeding the maximum load.
    """
    # Get the number of orders
    num_orders = len(orders)

    # Create a 2D table to store the maximum achievable value for each order and weight capacity.
    table = [[0] * (maximum_load + 1) for _ in range(num_orders + 1)]

    # Use dynamic programming to compute the maximum value that can be achieved
    for i in range(1, num_orders + 1):
        for j in range(1, maximum_load + 1):
            # If the weight of the current order is more than the weight capacity, skip this order
            if orders[i - 1]['weight'] > j:
                table[i][j] = table[i - 1][j]
            else:
                # Compute the maximum value that can be achieved by either including or excluding the current order.
                # Include the value of the current order if it fits in the remaining weight capacity.
                # Update the remaining weight capacity and compute the maximum value for the current weight capacity.
                # Choose the higher value between including and excluding the current order.
                table[i][j] = max(table[i - 1][j], table[i - 1][j - orders[i - 1]['weight']] + orders[i - 1]['value'])

    # Return the maximum value that can be achieved for the given weight capacity
    return table[num_orders][maximum_load]
